import discord
from discord.ext import commands

class AdminCommands(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def load(self, ctx, cog : str):
    await self.bot.load_extension(f"cogs.{cog.lower()}")

  @commands.command()
  async def unload(self, ctx, cog : str):
    await self.bot.unload_extension(f"cogs.{cog.lower()}")

  @commands.command()
  async def reload(self, ctx, cog : str):
    await self.bot.reload_extension(f"cogs.{cog.lower()}")

async def setup(bot):
  await bot.add_cog(AdminCommands(bot))