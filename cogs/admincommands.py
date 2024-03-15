import discord
from discord.ext import commands
from src import settings

class AdminCommands(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot

  # LOAD COG USING PYTHON COG FILENAME
  @commands.command()
  @commands.has_permissions(administrator=True)
  async def load(self, ctx, cog : str):
    await self.bot.load_extension(f"cogs.{cog.lower()}")
    try:
      cog_load = discord.Embed(title=f"{cog.upper()}")
      cog_load.add_field(name="Carregado", value="")
      cog_load.set_thumbnail(url=settings.MAMACO)
      await ctx.send(embed=cog_load)
      await ctx.message.delete()
    except discord.HTTPException:
      pass
  
  # UNLOAD COG USING PYTHON COG FILENAME
  @commands.command()
  @commands.has_permissions(administrator=True)
  async def unload(self, ctx, cog : str):
    await self.bot.unload_extension(f"cogs.{cog.lower()}")
    try:
      cog_unload = discord.Embed(title=f"{cog.upper()}")
      cog_unload.add_field(name="Descarregado", value="")
      cog_unload.set_thumbnail(url=settings.MAMACO)
      await ctx.send(embed=cog_unload)
      await ctx.message.delete()
    except discord.HTTPException:
      pass
  
  # RELOAD COG USING PYTHON FILENAME
  @commands.command()
  @commands.has_permissions(administrator=True)
  async def reload(self, ctx, cog : str):
    await self.bot.reload_extension(f"cogs.{cog.lower()}")
    try:
      cog_reload = discord.Embed(title=f"{cog.upper()}")
      cog_reload.add_field(name="Recarregado", value="")
      cog_reload.set_thumbnail(url=settings.MAMACO)
      await ctx.send(embed=cog_reload)
      await ctx.message.delete()
    except discord.HTTPException:
      pass

  # GET ALL CHANNELS INFO FROM A GUILD
  @commands.command()
  @commands.has_permissions(administrator=True)
  async def listchannels(self, ctx):
    channel_type = "category"
    channel = discord.Embed(title="PROPRIEDADES DO CANAL")
    await ctx.send(ctx.guild.channels)
    for ch in ctx.guild.channels:
      if str(ch.type).lower() != channel_type:
        channel.add_field(name="Nome", value=f"{ch.name}")
        channel.add_field(name="ID", value=f"||{ch.id}||")
        channel.add_field(name="TYPE", value=f"{ch.type}")
    channel.set_thumbnail(url=settings.MAMACO)
    await ctx.send(embed=channel)
        
async def setup(bot):
  await bot.add_cog(AdminCommands(bot))