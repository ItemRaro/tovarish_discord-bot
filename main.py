import discord
from discord.ext import commands
from cogs.greetings import Greetings
from cogs.commands import DefaultCommands
from cogs.errorhandler import ErrorHandler
from src import settings

logger = settings.logging.getLogger("bot")

def run():
  intents = settings.INTENTS
  intents.message_content = True
  intents.voice_states = True
  intents.presences = True

  bot = settings.BOT

  @bot.event
  async def on_ready():
    logger.info(f"\nBOT ID = {bot.user.id}\nBOT NAME = {bot.user}")

    for cog_file in settings.COGS_DIR.glob("*.py"):
      if cog_file != "__init__.py":
        await bot.load_extension(f"cogs.{cog_file.name[:-3]}")


  bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__ == "__main__":
  run()