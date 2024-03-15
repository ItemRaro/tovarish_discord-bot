import os
import discord
from discord.ext import commands
import wavelink
from src import settings
from datetime import timedelta

# GLOBAL VARIABLES

logger = settings.logging.getLogger("music")
file_name = os.path.basename(__file__)

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
    logger.info(
      f"\nCOG NAME = {os.path.splitext(file_name)[0]} \t ID = {node.node.identifier} \t  STATUS = {str(node.node.status)[-9:]}"
      )
  
  @commands.Cog.listener()
  async def on_wavelink_track_start(self, now_playing : wavelink.TrackStartEventPayload):
    nowplaying_embed = discord.Embed(
      colour=discord.Colour.yellow(),
      title=f"{now_playing.track.title}",
      description=f"by {now_playing.track.author}"
      )
    nowplaying_embed.set_thumbnail(url=settings.MAMACO)
    nowplaying_embed.set_image(url=now_playing.track.artwork)
    await self.music_channel.send(embed=nowplaying_embed)

  # CHECKS IF PLAYER IS INACTIVE AND THEN DISCONNECTS
  @commands.Cog.listener()
  async def on_wavelink_inactive_player(self, player : wavelink.Player):
    self.connected = False
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
      tracks : int = await self.vc.queue.put_wait(search)
      embed = discord.Embed(
      colour=discord.Colour.yellow(),
      title=f"{search.name}"
      )
      embed.add_field(name=f"{tracks} músicas adicionadas a fila", value="")
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
        embed.add_field(name="adicionada a fila", value="")
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

  # PAUSE CURRENT PLAYING SONG
  @commands.command()
  async def pause(self, ctx) -> None:
    if not self.vc:
        return
    await self.vc.pause(True)
    paused_embed = discord.Embed(
      colour=discord.Colour.yellow(),
      title=f"Pausado",
      description=f"{self.vc.current.title}\nby {self.vc.current.author}"
      )
    paused_embed.set_thumbnail(url=settings.MAMACO)
    await ctx.send(embed=paused_embed)
    try:
      await ctx.message.delete()
    except discord.HTTPException:
      pass
  
  # RESUME CURRENT PLAYING SONG
  @commands.command()
  async def resume(self, ctx) -> None:
    if not self.vc:
        return
    await self.vc.pause(False)
    resumed_embed = discord.Embed(
      colour=discord.Colour.yellow(),
      title=f"Tocando",
      description=f"{self.vc.current.title}\nby {self.vc.current.author}"
      )
    resumed_embed.set_thumbnail(url=settings.MAMACO)
    await ctx.send(embed=resumed_embed)
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
    try:
      await ctx.message.delete()
    except discord.HTTPException:
      pass

  # STOPS CURRENT PLAYING MUSIC AND CLEARS THE QUEUE
  @commands.command()
  async def stop(self, ctx) -> None:
    self.connected = False
    await self.vc.disconnect()
    if not self.vc.queue.is_empty:
      await self.vc.queue.clear()
    try:
      await ctx.message.delete()
    except discord.HTTPException:
      pass

  # SHOW THE CURRENT MUSIC LIST
  @commands.command()
  async def queue(self, ctx) -> None:
    if not self.vc.queue.is_empty:
      counter = 0
      queue = []
      queue = self.vc.queue.copy()
      queue_embed = discord.Embed(
        colour=discord.Colour.yellow(),
        title="Próximas músicas"
        )
      for track_item in queue:
          counter = counter + 1
          track_info = track_item
          queue_embed.add_field(
            name=f"{counter} - {track_info.title} by {track_info.author} ({str(timedelta(seconds=track_info.length / 1000))[3:]}min)",
            value="", inline=False
            )
      queue_embed.set_thumbnail(url=settings.MAMACO)
      await ctx.send(embed=queue_embed)
    else:
      empty_embed = discord.Embed(
        colour=discord.Colour.yellow(),
        title="A fila está vazia"
        )
      empty_embed.set_thumbnail(url=settings.MAMACO)
      await ctx.send(embed=empty_embed)
    try:
      await ctx.message.delete()
    except discord.HTTPException:
      pass

  # DELETES A TRACK FROM THE QUEUE
  @commands.command()
  async def delete(self, ctx, track : int):
    if not self.vc.queue.is_empty and self.vc:
      del_track = self.vc.queue.get_at(track - 1)
      track_embed = discord.Embed(
        colour=discord.Colour.yellow(),
        title=f"{del_track.title}",
        description=f"by {del_track.author}"
        )
      track_embed.add_field(name="Foi removido da fila", value="")
      track_embed.set_thumbnail(url=settings.MAMACO)
      await ctx.send(embed=track_embed)
      await self.vc.queue.delete(del_track)
    try:
      await ctx.message.delete()
    except discord.HTTPException:
      pass
  
  # LEAVES VOICE CHANNEL
  @commands.command()
  async def bye(self, ctx) -> None:
    if self.vc.connected:
      self.connected = False
      await self.vc.disconnect()
    try:
      await ctx.message.delete()
    except discord.HTTPException:
      pass
  
  # RESETS BOT CONNECTION WITH VOICE CHANNEL
  @commands.command()
  async def reset(self, ctx) -> None:
    channel = ctx.author.voice.channel
    self.vc = await channel.connect(cls=wavelink.Player)
    self.connected = False
    await self.vc.disconnect()
    try:
      await ctx.message.delete()
    except discord.HTTPException:
      pass

async def setup(bot):
  music_bot = Music(bot)
  await bot.add_cog(music_bot)
  await music_bot.lavalink_connect()