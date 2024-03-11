import discord
from discord.ext import commands
import src.settings as settings

class ErrorHandler(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send("Erro!! Digite o número seguido por epaço e outro número. Ex: some 2 2")

async def setup(bot):
  await bot.add_cog(ErrorHandler(bot))