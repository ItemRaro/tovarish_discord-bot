import discord
from discord.ext import commands

class AdminCommands(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  @commands.has_permissions(administrator=True)
  async def load(self, ctx, cog : str):
    await self.bot.load_extension(f"cogs.{cog.lower()}")
    try:
      await ctx.send(f"{cog} carregado")
      await ctx.message.delete()
    except discord.HTTPException:
      pass

  @commands.command()
  @commands.has_permissions(administrator=True)
  async def unload(self, ctx, cog : str):
    await self.bot.unload_extension(f"cogs.{cog.lower()}")
    try:
      await ctx.send(f"{cog} descarregado")
      await ctx.message.delete()
    except discord.HTTPException:
      pass

  @commands.command()
  @commands.has_permissions(administrator=True)
  async def reload(self, ctx, cog : str):
    await self.bot.reload_extension(f"cogs.{cog.lower()}")
    try:
      await ctx.send(f"{cog} recarregado")
      await ctx.message.delete()
    except discord.HTTPException:
      pass

async def setup(bot):
  await bot.add_cog(AdminCommands(bot))