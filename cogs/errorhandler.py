import discord
from discord.ext import commands
import src.settings as settings

class ErrorHandler(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    # ADMINISTRATION CHECK
    if isinstance(error, commands.MissingPermissions):
      permission = discord.Embed(title="ERRO")
      permission.add_field(name="Permissão negada", value="")
      permission.set_thumbnail(url=settings.MAMACO)
      await ctx.send(embed=permission)
    
    # COMMAND EXISTENCE CHECK
    if isinstance(error, commands.CommandNotFound):
      error = discord.Embed(title="ERRO")
      error.add_field(name="Comando inválido", value="")
      error.set_thumbnail(url=settings.MAMACO)
      await ctx.send(embed=error)
    
    # COMMAND ARGUMENTS CHECK
    if isinstance(error, commands.MissingRequiredArgument):
      error = discord.Embed(title="ERRO")
      error.add_field(name="Comando incompleto", value="")
      error.set_thumbnail(url=settings.MAMACO)
      await ctx.send(embed=error)

async def setup(bot):
  await bot.add_cog(ErrorHandler(bot))