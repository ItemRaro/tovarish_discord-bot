import discord
from src import settings
from src import help
from discord.ext import commands
from cogs.controllers import Controllers
from cogs.admincommands import AdminCommands
from cogs.music import Music
from cogs.errorhandler import ErrorHandler

logger = settings.logging.getLogger("bot")

def run():
  intents = settings.INTENTS
  intents.message_content = True
  intents.voice_states = True
  intents.presences = True

  bot = settings.BOT

  @bot.event
  async def on_ready():
    logger.info(f"\nBOT NAME = {bot.user} \t BOT ID = {bot.user.id}\t STATUS = {str(bot.status).upper()}")
    for guild in bot.guilds:
      logger.info(f"\nGUILD NAME = {guild.name} \t GUILD ID = {guild.id}\t STATUS = {guild.member_count} MEMBERS ONLINE")

    for cog_file in settings.COGS_DIR.glob("*.py"):
      if cog_file != "__init__.py":
        await bot.load_extension(f"cogs.{cog_file.name[:-3]}")

    # BOT PRESENCE UPDATE
    mamaco = discord.CustomActivity(name="🍌 Mamaco * !!help")
    await bot.change_presence(status=discord.Status.online, activity=mamaco)

  bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__ == "__main__":
  run()