import discord
from discord.ext import commands
from helpconfig import defaultcommands

class DefaultCommands(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot

# ------------------------------------------- COMMANDS START HERE ------------------------------------------- #

  # DELETE MESSAGES FROM THE CURRENT USER TEXT CHANNEL LIMIT 100
  @commands.command(
    description=defaultcommands.DeleteMessages.DESCRIPTION,
    aliases=defaultcommands.DeleteMessages.ALIASES,
    help=defaultcommands.DeleteMessages.HELP,
    brief=defaultcommands.DeleteMessages.BRIEF
  )
  async def deletemessages(self, ctx, num : int):
    await ctx.channel.purge(limit=num)
  
  # DELTE ALL MESSAGES FROM THE CURRENT USER TEXT CHANNEL
  @commands.command(
    description=defaultcommands.PurgeMessages.DESCRIPTION,
    aliases=defaultcommands.PurgeMessages.ALIASES,
    help=defaultcommands.PurgeMessages.HELP,
    brief=defaultcommands.PurgeMessages.BRIEF
  )
  async def purgemessages(self, ctx):
    await ctx.channel.purge(limit=None)

async def setup(bot):
  await bot.add_cog(DefaultCommands(bot))