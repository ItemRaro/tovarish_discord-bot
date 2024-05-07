import discord
import datetime
from discord.ext import commands
from discord.ext import tasks
from src import settings

# TIME AND TIMEZONE
timezone = datetime.timezone(datetime.timedelta(hours=-3), name="BRL")
# TIME TO EXECUTE A TASK DAILY
time = datetime.time(hour=3, minute=00, tzinfo=timezone)

class Controllers(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.message_deletion.start()

# ------------------------------------------- AUTOMATION START HERE ------------------------------------------- #

  # AUTO DELETE MESSAGES FROM A TEXTCHANNEL SPECIFIED BY CHANNEL ID
  @tasks.loop(time=time)
  async def message_deletion(self):
    channel_id = "1150227153833709578"
    for guild in self.bot.guilds:
      for channel in guild.channels:
        if str(channel.id) == channel_id:
          await channel.purge(limit=None)

  # DELETE MESSAGES THAT ARE NOT IMAGES ON IMAGES CHANNELS
  @commands.Cog.listener()
  async def on_message(self, ctx):
    channel_id = ctx.channel.id
    message_content = ctx.content
    if message_content != "" and str(channel_id) in settings.IMAGE_CHANNELS_ID:
      try:
        await ctx.delete()
      except discord.HTTPException:
        pass

async def setup(bot):
  await bot.add_cog(Controllers(bot))