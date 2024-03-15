import discord
from discord.ext import commands
from helpconfig.defaultcommands import deletemessages

class DefaultCommands(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot

  # DELETE MESSAGES FROM THE CURRENT USER TEXT CHANNEL LIMIT 100
  @commands.command(
    description=deletemessages.DESCRIPTION,
    aliases=deletemessages.ALIASES,
    help=deletemessages.HELP,
    brief=deletemessages.BRIEF
  )
  async def deletemessages(self, ctx, num : int):
    await ctx.channel.purge(limit=num)
  
  # DELTE ALL MESSAGES FROM THE CURRENT USER TEXT CHANNEL
  @commands.command()
  async def purgemessages(self, ctx):
    await ctx.channel.purge(limit=None)

async def setup(bot):
  await bot.add_cog(DefaultCommands(bot))