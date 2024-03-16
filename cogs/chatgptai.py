import discord
import openai
from discord.ext import commands
from src import settings
from helpconfig import chatgptai

logger = settings.logging.getLogger("bot")

class ChatGPTAI(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot
  
  def chatgpt_response(self, chat_prompt):
    openai.api_key = settings.CHATGPT_API_SECRET
    openai.max_retries = 0
    gpt_response = openai.chat.completions.create(
      model="gpt-3.5-turbo-0125",
      messages=[
        {
          "role" : "user",
          "content" : f"{chat_prompt}"
        }
      ],
      temperature=1
    )
    mamaco_response = gpt_response.choices[0].message.content
    return mamaco_response
  
  @commands.command(
    name=chatgptai.ChatGPTAI.NAME,
    description=chatgptai.ChatGPTAI.DESCRIPTION,
    aliases=chatgptai.ChatGPTAI.ALIASES,
    help=chatgptai.ChatGPTAI.HELP,
    brief=chatgptai.ChatGPTAI.BRIEF
  )
  async def gpt(self, ctx, *query : str):
    query = " ".join(query)
    response = self.chatgpt_response(chat_prompt=query)
    await ctx.send(response)

async def setup(bot):
  await bot.add_cog(ChatGPTAI(bot))