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
      permission_embed = discord.Embed(
        colour=discord.Colour.red(),
        title="ERRO"
        )
      permission_embed.add_field(
        name="Permissão negada",
        value=""
        )
      permission_embed.set_thumbnail(url=settings.MAMACO)
      await ctx.send(embed=permission_embed)
    
    # COMMAND EXISTENCE CHECK
    if isinstance(error, commands.CommandNotFound):
      error_embed = discord.Embed(
        colour=discord.Colour.red(),
        title="ERRO"
        )
      error_embed.add_field(
        name="Comando não existente",
        value=""
        )
      error_embed.set_thumbnail(url=settings.MAMACO)
      await ctx.send(embed=error_embed)
    
    # COMMAND ARGUMENTS CHECK
    if isinstance(error, commands.MissingRequiredArgument):
      error_embed = discord.Embed(
        colour=discord.Colour.red(),
        title="ERRO"
        )
      error_embed.add_field(
        name="Comando incompleto",
        value=""
        )
      error_embed.set_thumbnail(url=settings.MAMACO)
      await ctx.send(embed=error_embed)

    # COMMNAND EXTENSION LOAD CHECK
    if isinstance(error, commands.ExtensionError):
      error_embed = discord.Embed(
        colour=discord.Colour.red(),
        title="ERRO"
        )
      error_embed.add_field(
        name="Falha ao carregar a extensão",
        value=""
        )
      error_embed.set_thumbnail(url=settings.MAMACO)
      await ctx.send(embed=error_embed)

async def setup(bot):
  await bot.add_cog(ErrorHandler(bot))