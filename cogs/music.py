import os
import discord
from discord.ext import commands
import wavelink
from src import settings
from datetime import timedelta

# GLOBAL VARIABLES

logger = settings.logging.getLogger("music")
file_name = os.path.basename(__file__).upper()

class Music(commands.Cog):

  # CLASS VARIABLES
  
  vc : wavelink.Player = None
  connected = False
  music_channel = None

  def __init__(self, bot):
    self.bot = bot

  # LAVALINK CONNECTION
    
  async def lavalink_connect(self):
    node : wavelink.Node = wavelink.Node(
      uri = f"http://{settings.LAVALINK_HOSTNAME}:{settings.LAVALINK_PORT}",
      password = settings.LAVALINK_PASSWORD
    )
    await wavelink.Pool.connect(
      client = self.bot,
      nodes = [node]
    )

  # COG LOAD AND PLAYER STATUS
    
  @commands.Cog.listener()
  async def on_wavelink_node_ready(self, node : wavelink.NodeReadyEventPayload):
    logger.info(f"\nCOG NAME = {os.path.splitext(file_name)[0]} \t ID = {node.node.identifier} \t  STATUS = {str(node.node.status)[-9:]}")
  
  @commands.Cog.listener()
  async def on_wavelink_track_start(self, now_playing : wavelink.TrackStartEventPayload):
    embed = discord.Embed(
      colour=discord.Colour.yellow(),
      title=f"{now_playing.track.title}",
      description=f"by {now_playing.track.author}"
      )
    embed.set_thumbnail(url=settings.MAMACO)
    embed.set_image(url=now_playing.track.artwork)
    await self.music_channel.send(embed=embed)

  # CHECKS IF PLAYER IS INACTIVE AND THEN DISCONNECTS
  @commands.Cog.listener()
  async def on_wavelink_inactive_player(self, player : wavelink.Player):
    await player.channel.send(f"O mamaco está inativo por `{player.inactive_timeout}` segundos. Adeus!")
    await player.disconnect()

  # ADDS AND PLAYS MUSIC FROM THE QUEUE
  @commands.command()
  async def play(self, ctx, *query : str) -> None:
    # CONNECTS TO VOICE CHANNEL
    channel = ctx.author.voice.channel
    self.music_channel = ctx.message.channel
    if not self.connected:
      self.connected = True
      try:
        self.vc = await channel.connect(cls=wavelink.Player)
      except AttributeError:
        await ctx.send("Please join a voice channel first before using this command.")
        return
      except discord.ClientException:
        await ctx.send("I was unable to join this voice channel. Please try again.")
        return
    else:
      pass

    # ADDS MUSIC
    query=" ".join(query)
    search : wavelink.Search = await wavelink.Playable.search(query)
    if not search:
      await ctx.send("Música não encontrada. Tente novamente")
      return
    if isinstance(search, wavelink.Playlist):
      await self.vc.queue.put_wait(search)
      embed = discord.Embed(
      colour=discord.Colour.yellow(),
      title=f"Playlist {search.name}"
      )
      embed.set_footer(text="adicionada a fila")
      embed.set_thumbnail(url=settings.MAMACO)
      await ctx.send(embed=embed)
    else:
      if not self.vc.playing and self.vc.queue.is_empty:
        track : wavelink.Playable = search[0]
        await self.vc.queue.put_wait(track)
      else:
        track : wavelink.Playable = search[0]
        await self.vc.queue.put_wait(track)
        embed = discord.Embed(
        colour=discord.Colour.yellow(),
        title=f"{track.title}",
        description=f"by {track.author}"
        )
        embed.set_footer(text="adicionada a fila")
        embed.set_thumbnail(url=settings.MAMACO)
        await ctx.send(embed=embed)
   
    # PLAYS MUSIC
    if not self.vc.queue.is_empty:
      if not self.vc.playing:
        await self.vc.play(self.vc.queue.get(), volume=100)
        self.vc.autoplay = wavelink.AutoPlayMode.partial
        self.vc.inactive_timeout = 10
    else:
      await ctx.send("A fila está vazia")
    try:
      await ctx.message.delete()
    except discord.HTTPException:
      pass
  
  # SKIP CURRENT PLAYING SONG
  @commands.command()
  async def skip(self, ctx) -> None:
    if not self.vc:
        return
    await self.vc.skip(force=True)

  # STOPS CURRENT PLAYING MUSIC AND CLEARS THE QUEUE
  @commands.command()
  async def stop(self, ctx) -> None:
    channel = self.vc.channel
    if not self.vc.queue.is_empty:
      await self.vc.queue.clear()
    if self.vc.playing:
      await self.vc.stop()
    self.connected = False
    await self.vc.disconnect()
    await ctx.send(f"Saiu de {channel.name}")

  # # SHOW THE CURRENT MUSIC LIST
  @commands.command()
  async def queue(self, ctx) -> None:
      if not self.vc.queue.is_empty:
        queue = []
        queue = self.vc.queue.copy()
        embed = discord.Embed(title="Próximas músicas")
        for track_item in queue:
            track_info = track_item
            embed.add_field(name=f"{track_info.title} \
                            by {track_info.author} - {str(timedelta(seconds=track_info.length / 1000))[3:]}",
                            value="", inline=False)
        embed.set_thumbnail(url=settings.MAMACO)
        await ctx.send(embed=embed)
      else:
        embed = discord.Embed(title="A fila está vazia")
        embed.set_thumbnail(url=settings.MAMACO)
        await ctx.send(embed=embed)
  
  # LEAVES VOICE CHANNEL
  @commands.command()
  async def bye(self, ctx) -> None:
    channel = self.vc.channel
    if channel:
      self.connected = False
      await self.vc.disconnect()
    await ctx.send(f"Saiu de {channel.name}")
  
  # RESETS BOT CONNECTION WITH VOICE CHANNEL
  @commands.command()
  async def reset(self, ctx) -> None:
    channel = ctx.author.voice.channel
    self.vc = await channel.connect(cls=wavelink.Player)
    self.connected = False
    await self.vc.disconnect()


async def setup(bot):
  music_bot = Music(bot)
  await bot.add_cog(music_bot)
  await music_bot.lavalink_connect()