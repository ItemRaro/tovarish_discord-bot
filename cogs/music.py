import discord
from discord.ext import commands
import wavelink
import src.settings as settings
from datetime import timedelta

# GLOBAL VARIABLES

logger = settings.logging.getLogger("music")

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
    logger.info(f"{node.node}")
  
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

  # ADDS AND PLAYS MUSIC FROM THE QUEUE
  @commands.command()
  async def play(self, ctx, *query : str):
    # CONNECTS TO VOICE CHANNEL
    channel = ctx.message.author.voice.channel
    self.music_channel = ctx.message.channel
    if not self.connected:
      self.connected = True
      self.vc = await channel.connect(cls=wavelink.Player)
      await ctx.send(f"Entrou em {channel.name}.")
    else:
      pass

    # ADDS MUSIC
    query=" ".join(query)
    search : wavelink.Search = await wavelink.Playable.search(query)
    if not search:
      await ctx.send("Música não encontrada. Tente novamente")
      return
    if isinstance(search, wavelink.Playlist):
      tracks: int = await self.vc.queue.put_wait(search)
      await ctx.send(f"Playlist {search.name} {tracks} adicionado a fila")
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
  
  # STOPS CURRENT PLAYING MUSIC AND CLEARS THE QUEUE
  @commands.command()
  async def stop(self, ctx):
    channel = self.vc.channel
    await self.vc.queue.clear()
    if self.vc.playing:
      await self.vc.stop()
    else:
      await self.vc.disconnect()
    await ctx.send(f"Saiu de {channel.name}")

  # # SHOW THE CURRENT MUSIC LIST
  @commands.command()
  async def queue(self, ctx):
      if not self.vc.queue.is_empty:
        queue = []
        queue = self.vc.queue.copy()
        embed = discord.Embed(title="FILA")
        for track_item in queue:
            track_info = track_item
            embed.add_field(name=f"{track_info.title} by {track_info.author} - {str(timedelta(seconds=track_info.length / 1000))[3:]}", value="", inline=False)
            embed.set_thumbnail(url=settings.MAMACO)
        await ctx.send(embed=embed)
      else:
        await ctx.send("A fila está vazia")
  
  # LEAVES VOICE CHANNEL
  @commands.command()
  async def bye(self, ctx):
    channel = self.vc.channel
    if channel:
      await self.vc.disconnect()
    await ctx.send(f"Saiu de {channel.name}")
  
  # RESETS BOT CONNECTION WITH VOICE CHANNEL
  @commands.command()
  async def reset(self, ctx):
    channel = ctx.message.author.voice.channel
    self.vc = await channel.connect(cls=wavelink.Player)
    await self.vc.disconnect()


async def setup(bot):
  music_bot = Music(bot)
  await bot.add_cog(music_bot)
  await music_bot.lavalink_connect()