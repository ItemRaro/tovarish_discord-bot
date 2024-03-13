import discord
import datetime
from discord.ext import commands
from discord.ext import tasks

# DATE AND TIME

utc = datetime.timezone.utc

# If no tzinfo is given then UTC is assumed.
time = datetime.time(hour=3, minute=00, tzinfo=utc)

class Controllers(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.message_deletion.start()

  @tasks.loop(time=time)
  async def message_deletion(self):
    ...

async def setup(bot):
  await bot.add_cog(Controllers(bot))