import discord
from discord.ext import commands
import wavelink
import src.settings as settings

# GLOBAL VARIABLES

logger = settings.logging.getLogger("music")

class MusicBOT(commands.Cog):

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

# COG LOAD STATUS
    
  @commands.Cog.listener()
  async def on_wavelink_node_ready(self, node : wavelink.Node):
    logger.info(f"{node} CONNECTED")

# BOT COMMANDS
    
  # JOINS AND PLAYS MUSIC
  @commands.command()
  async def play(self, ctx, music_tittle : str):
    self.channel = ctx.message.author.voice.channel
    #MUSIC SEARCH
    self.chosen_track = await wavelink.Playable.search(music_tittle)
    if self.chosen_track:
      self.current_track = self.chosen_track
    # CHANNEL CONNECT AND PLAY
      if self.channel:
        self.vc = self.channel.connect(cls=wavelink.Player)
        if self.current_track and self.vc:
          await self.vc.play(self.current_track)

async def setup(bot):
  music_bot = MusicBOT(bot)
  await bot.add_cog(music_bot)
  await music_bot.lavalink_connect()