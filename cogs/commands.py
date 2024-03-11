import discord
from discord.ext import commands

class DefaultCommands(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def some(self, ctx, a : int, b : int):
    await ctx.send(f"{a} + {b} = {a+b}")

async def setup(bot):
  await bot.add_cog(DefaultCommands(bot))