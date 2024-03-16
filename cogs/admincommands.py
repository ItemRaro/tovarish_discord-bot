import discord
from discord.ext import commands
from helpconfig import admincommands

class AdminCommands(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot

  # SYNC SLASH COMMANDS
  @commands.command(
    description=admincommands.SyncSlashCommands.DESCRIPTION,
    aliases=admincommands.SyncSlashCommands.ALIASES,
    help=admincommands.SyncSlashCommands.HELP,
    brief=admincommands.SyncSlashCommands.BRIEF
  )
  @commands.has_permissions(administrator=True)
  async def sync(self, ctx):
    await self.bot.tree.sync()
    synced_embed = discord.Embed(
      colour=discord.Colour.green(),
      title="SLASHCOMMANDS"
      )
    synced_embed.add_field(
      name="Sincronizado ✅",
      value=""
      )
    await ctx.send(embed=synced_embed)
    try:
      await ctx.message.delete()
    except discord.HTTPException:
      pass

  # LOAD COG USING PYTHON COG FILENAME
  @commands.command(
    description=admincommands.CogLoad.DESCRIPTION,
    aliases=admincommands.CogLoad.ALIASES,
    help=admincommands.CogLoad.HELP,
    brief=admincommands.CogLoad.BRIEF
  )
  @commands.has_permissions(administrator=True)
  async def load(self, ctx, cog : str):
    await self.bot.load_extension(f"cogs.{cog.lower()}")
    cog_load = discord.Embed(
      colour=discord.Colour.green(),
      title=f"{cog.upper()}"
      )
    cog_load.add_field(
      name="Carregado ✅",
      value=""
      )
    await ctx.send(embed=cog_load)
    try:
      await ctx.message.delete()
    except discord.HTTPException:
      pass
  
  # UNLOAD COG USING PYTHON COG FILENAME
  @commands.command(
    description=admincommands.CogUnload.DESCRIPTION,
    aliases=admincommands.CogUnload.ALIASES,
    help=admincommands.CogUnload.HELP,
    brief=admincommands.CogUnload.BRIEF
)
  @commands.has_permissions(administrator=True)
  async def unload(self, ctx, cog : str):
    await self.bot.unload_extension(f"cogs.{cog.lower()}")
    cog_unload = discord.Embed(
      colour=discord.Colour.green(),
      title=f"{cog.upper()}"
      )
    cog_unload.add_field(
      name="Descarregado ✅",
      value=""
      )
    await ctx.send(embed=cog_unload)
    try:
      await ctx.message.delete()
    except discord.HTTPException:
      pass
  
  # RELOAD COG USING PYTHON FILENAME
  @commands.command(
    description=admincommands.CogReload.DESCRIPTION,
    aliases=admincommands.CogReload.ALIASES,
    help=admincommands.CogReload.HELP,
    brief=admincommands.CogReload.BRIEF
  )
  @commands.has_permissions(administrator=True)
  async def reload(self, ctx, cog : str):
    await self.bot.reload_extension(f"cogs.{cog.lower()}")
    cog_reload = discord.Embed(
      colour=discord.Colour.green(),
      title=f"{cog.upper()}"
      )
    cog_reload.add_field(
      name="Recarregado ✅",
      value=""
      )
    await ctx.send(embed=cog_reload)
    try:
      await ctx.message.delete()
    except discord.HTTPException:
      pass

  # GET ALL CHANNELS INFO FROM A GUILD
  @commands.hybrid_command(
    description=admincommands.ListChannels.DESCRIPTION,
    aliases=admincommands.ListChannels.ALIASES,
    help=admincommands.ListChannels.HELP,
    brief=admincommands.ListChannels.BRIEF
  )
  @commands.has_permissions(administrator=True)
  async def listchannels(self, ctx):
    channel_type = [
      "category",
      "voice",
      "text"
      ]
    textchannel_embed = discord.Embed(
      colour=discord.Colour.green(),
      title="PROPRIEDADES DOS CANAIS DE TEXTO"
      )
    voicechannel_embed = discord.Embed(
      colour=discord.Colour.green(),
      title="PROPRIEDADES DOS CANAIS DE VOZ"
      )
    for channel in ctx.guild.channels:
      if str(channel.type).lower() != channel_type[0]:
            if str(channel.type).lower() != channel_type[1]:
              textchannel_embed.add_field(
                name="",
                value=f"{channel.name}({channel.type})\t||{channel.id}||",
                inline=False
                )
            else:
              voicechannel_embed.add_field(
                name="",
                value=f"{channel.name}({channel.type})\t||{channel.id}||",
                inline=False
                )
    await ctx.send(embed=textchannel_embed)
    await ctx.send(embed=voicechannel_embed)
    try:
      await ctx.message.delete()
    except discord.HTTPException:
      pass
  
  @commands.command(
    description=admincommands.ListChannelsFrom.DESCRIPTION,
    aliases=admincommands.ListChannelsFrom.ALIASES,
    help=admincommands.ListChannelsFrom.HELP,
    brief=admincommands.ListChannelsFrom.BRIEF
  )
  @commands.has_permissions(administrator=True)
  async def listchannelsfrom(self, ctx, *guild_name):
    guild_name = " ".join(guild_name)
    channel_type = [
      "category",
      "voice",
      "text"
      ]
    textchannel_embed = discord.Embed(
      colour=discord.Colour.green(),
      title="PROPRIEDADES DOS CANAIS DE TEXTO"
      )
    voicechannel_embed = discord.Embed(
      colour=discord.Colour.green(),
      title="PROPRIEDADES DOS CANAIS DE VOZ"
      )
    for guild in self.bot.guilds:
      if str(guild.name) == guild_name:
        for channel in guild.channels:
          if str(channel.type).lower() != channel_type[0]:
            if str(channel.type).lower() != channel_type[1]:
              textchannel_embed.add_field(
                name="",
                value=f"{channel.name}({channel.type})\t||{channel.id}||",
                inline=False
                )
            else:
              voicechannel_embed.add_field(
                name="",
                value=f"{channel.name}({channel.type})\t||{channel.id}||",
                inline=False
                )
    await ctx.send(embed=textchannel_embed)
    await ctx.send(embed=voicechannel_embed)
    try:
      await ctx.message.delete()
    except discord.HTTPException:
      pass
        
async def setup(bot):
  await bot.add_cog(AdminCommands(bot))