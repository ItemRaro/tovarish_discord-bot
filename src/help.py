import discord
from discord.ext import commands

class HelpCommand(commands.DefaultHelpCommand):
    
  async def send_pages(self):
    channel = self.get_destination()
    page_embed = discord.Embed(
      colour=discord.Colour.blurple(),
      title="Lista de Comandos",
      description=""
    )
    for page in self.paginator.pages:
      page_embed.description += page
    await channel.send(embed=page_embed)