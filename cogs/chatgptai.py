import discord
import openai
from discord.ext import commands
from src import settings
from helpconfig import chatgptai

logger = settings.logging.getLogger("bot")

class ChatGPTAI(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot
  
  # CHATGPT GENERATE RESPONSE FUNCTION
  def chatgpt_response(self, chat_prompt):
    openai.api_key = settings.CHATGPT_API_SECRET
    openai.max_retries = 0
    gpt_response = openai.chat.completions.create(
      model="gpt-3.5-turbo",
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
  
  # CHECK IS CHATGPT COMMAND IS BEING USED ON THE CORRECT CHATGPT CHANNELS
  def is_chatgpt_channel(ctx):
    return str(ctx.channel.id) in settings.CHATGTP_CHANNELS_ID
  
# ------------------------------------------- COMMANDS START HERE ------------------------------------------- #
  
  @commands.command(
    name=chatgptai.ChatGPTAI.NAME,
    description=chatgptai.ChatGPTAI.DESCRIPTION,
    aliases=chatgptai.ChatGPTAI.ALIASES,
    help=chatgptai.ChatGPTAI.HELP,
    brief=chatgptai.ChatGPTAI.BRIEF
  )
  @commands.check(is_chatgpt_channel)
  async def gpt(self, ctx, *query : str):
    query = " ".join(query)
    response = self.chatgpt_response(chat_prompt=query)
    await ctx.send(response)

async def setup(bot):
  await bot.add_cog(ChatGPTAI(bot))