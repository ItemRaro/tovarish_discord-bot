import discord
from discord.ext import commands

class DefaultCommands(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def deletemessages(self, ctx, num : int):
    await ctx.channel.purge(limit=num)
  
  @commands.command()
  async def purgemessages(self, ctx):
    await ctx.channel.purge()

async def setup(bot):
  await bot.add_cog(DefaultCommands(bot))