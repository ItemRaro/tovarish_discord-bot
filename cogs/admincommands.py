import discord
from discord.ext import commands
from src import settings

class AdminCommands(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot

  # SYNC SLASH COMMANDS
  @commands.command()
  @commands.has_permissions(administrator=True)
  async def sync(self, ctx):
    await self.bot.tree.sync()
    try:
      synced_embed = discord.Embed(
        colour=discord.Colour.green(),
        title="SLASHCOMMANDS"
        )
      synced_embed.add_field(
        name="Sincronizado ✅",
        value=""
        )
      await ctx.send(embed=synced_embed)
      await ctx.message.delete()
    except discord.HTTPException:
      pass

  # LOAD COG USING PYTHON COG FILENAME
  @commands.command()
  @commands.has_permissions(administrator=True)
  async def load(self, ctx, cog : str):
    await self.bot.load_extension(f"cogs.{cog.lower()}")
    try:
      cog_load = discord.Embed(
        colour=discord.Colour.green(),
        title=f"{cog.upper()}"
        )
      cog_load.add_field(
        name="Carregado ✅",
        value=""
        )
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
      cog_unload = discord.Embed(
        colour=discord.Colour.green(),
        title=f"{cog.upper()}"
        )
      cog_unload.add_field(
        name="Descarregado ✅",
        value=""
        )
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
      cog_reload = discord.Embed(
        colour=discord.Colour.green(),
        title=f"{cog.upper()}"
        )
      cog_reload.add_field(
        name="Recarregado ✅",
        value=""
        )
      await ctx.send(embed=cog_reload)
      await ctx.message.delete()
    except discord.HTTPException:
      pass

  # GET ALL CHANNELS INFO FROM A GUILD
  @commands.hybrid_command()
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
  
  @commands.command()
  @commands.has_permissions(administrator=True)
  async def forcelistchannels(self, ctx, *guild_name):
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
        
async def setup(bot):
  await bot.add_cog(AdminCommands(bot))