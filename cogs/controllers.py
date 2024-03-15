import discord
import datetime
from discord.ext import commands
from discord.ext import tasks

# TIME AND TIMEZONE

timezone = datetime.timezone(datetime.timedelta(hours=-3), name="BRL")

time = datetime.time(hour=16, minute=33, tzinfo=timezone)

class Controllers(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.message_deletion.start()

  def cog_unload(self):
    self.message_deletion.cancel()

  @tasks.loop(time=time)
  async def message_deletion(self):
    self.channel_id = "1150227153833709578"
    for guild in self.bot.guilds:
      for channel in guild.channels:
        if str(channel.id) == self.channel_id:
          self.channel = channel
    await self.channel.purge()

async def setup(bot):
  await bot.add_cog(Controllers(bot))