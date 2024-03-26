import discord
import openai
from discord.ext import commands
from src import settings
from helpconfig import chatgptai

logger = settings.logging.getLogger("bot")

class ChatGPTAI(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot
  
  # CHATGPT TEXT GENERATE RESPONSE FUNCTION
  def chatgpt_text_response(self, chat_prompt):
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
  
  # CHATGPT IMAGE GENERATE RESPONSE FUNCTION
  def chatgpt_image_response(self, chat_prompt):
    openai.api_key = settings.CHATGPT_API_SECRET
    openai.max_retries = 0
    gpt_response = openai.images.generate(
      model="dall-e-3",
      prompt=f"{chat_prompt}",
      n= 1,
      size= "1024x1024"
    )
    mamaco_response = gpt_response.data[0].url
    return mamaco_response
  
  # CHECK IS CHATGPT COMMAND IS BEING USED ON THE CORRECT CHATGPT CHANNELS
  def is_chatgpt_channel(ctx):
    return str(ctx.channel.id) in settings.CHATGTP_CHANNELS_ID
  
# ------------------------------------------- COMMANDS START HERE ------------------------------------------- #
  # CHATGPT TEXT GENERATION COMMAND
  @commands.command(
    name=chatgptai.TextGPTAI.NAME,
    description=chatgptai.TextGPTAI.DESCRIPTION,
    aliases=chatgptai.TextGPTAI.ALIASES,
    help=chatgptai.TextGPTAI.HELP,
    brief=chatgptai.TextGPTAI.BRIEF
  )
  @commands.check(is_chatgpt_channel)
  async def textgpt(self, ctx, *query : str):
    query = " ".join(query)
    response = self.chatgpt_text_response(chat_prompt=query)
    await ctx.send(response)

  # CHATGTP IMAGE GENERATION COMMAND
  @commands.command(
    name=chatgptai.ImageGPTAI.NAME,
    description=chatgptai.ImageGPTAI.DESCRIPTION,
    aliases=chatgptai.ImageGPTAI.ALIASES,
    help=chatgptai.ImageGPTAI.HELP,
    brief=chatgptai.ImageGPTAI.BRIEF
  )
  @commands.check(is_chatgpt_channel)
  async def imagegpt(self, ctx, *query : str):
    await ctx.send("Gerando imagem...")
    query = " ".join(query)
    response = self.chatgpt_image_response(chat_prompt=query)
    await ctx.send(response)

async def setup(bot):
  await bot.add_cog(ChatGPTAI(bot))