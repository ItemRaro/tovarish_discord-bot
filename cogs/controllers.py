import discord
import datetime
from discord.ext import commands
from discord.ext import tasks

# TIME AND TIMEZONE
timezone = datetime.timezone(datetime.timedelta(hours=-3), name="BRL")
# TIME TO EXECUTE A TASK DAILY
time = datetime.time(hour=3, minute=00, tzinfo=timezone)

class Controllers(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.message_deletion.start()

  # AUTO DELETE MESSAGES FROM A TEXTCHANNEL SPECIFIED BY CHANNEL ID
  @tasks.loop(time=time)
  async def message_deletion(self):
    self.channel_id = "1150227153833709578"
    for guild in self.bot.guilds:
      for channel in guild.channels:
        if str(channel.id) == self.channel_id:
          self.channel = channel
    await self.channel.purge(limit=None)

async def setup(bot):
  await bot.add_cog(Controllers(bot))