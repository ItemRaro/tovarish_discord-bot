import os
import pathlib
import logging
import discord
from discord.ext import commands
from src.help import HelpCommand
from dotenv import load_dotenv
from logging.config import dictConfig

load_dotenv(dotenv_path="/app/.env")

# DISCORD CONNECTION CONFIGURATIONS

DISCORD_API_SECRET = os.getenv("DISCORD_TOVARISH_TOKEN")

INTENTS = discord.Intents.default()

BOT = commands.Bot(command_prefix="!!", intents=INTENTS, help_command=HelpCommand())

# PATHS TO BE LOADED FOR COGS AND OTHER

MAIN_DIR = pathlib.Path("/app")

COGS_DIR = MAIN_DIR / "cogs"

# LAVALINK CONNECTION CONFIGURATIONS

LAVALINK_HOSTNAME = "lavalink"

LAVALINK_PORT = "2333"

LAVALINK_PASSWORD = os.getenv("LAVALINK_API_PASSWD")

# OPENAI CHATGPT API CONNECTION CONFIGURATIONS

CHATGPT_API_SECRET = os.getenv("CHATGPT_API_TOKEN")

CHATGPT_API_ORG = "DiscordBOT"

CHATGPT_API_ORG_ID = os.getenv("CHATGPT_API_ORG_ID")

# CHANNELS CONFIGURATIONS

CHATGTP_CHANNELS_ID = [
  # COLETIVO FADOLAS
  "1144079257170083850"
]

MUSIC_CHANNELS_ID = [
  # GAMAHOUSE MUSIC CHANNEL
  "935261218187395102",
  # COLETIVO FADOLAS MUSIC CHANNEL
  "1150227153833709578",
  # BOT TEST MUSIC CHANNEL
  "1150077320741257216"
]

IMAGE_CHANNELS_ID = [
  # GAMAHOUSE IMAGE CHANNEL
  "823016254204936192",
  # COLETIVO FADOLAS IMAGE CHANNEL
  "1150225125191471125",
  # BOT TEST IMAGE CHANNEL
  "1150077352332763167"
]

# THUMBS URL

MAMACO = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRjcMpUkFdsZubWyUg9de0kL7dlNTE2j9SBgYVVRfmuDA&s"

# BOT LOGGING CONFIGURATIONS

LOGGIN_CONFIG = {
  "version": 1,
  "disabled_existing_loggers": False,
  "formatters": {
    "verbose": {
      "format": "%(levelname)-10s - %(asctime)s - %(module)-15s : %(message)s"
		},
    "standart": {
      "format": "%(asctime)s - %(module)-15s : %(message)s"
		}
	},
  "handlers": {
    "console": {
      "level": "DEBUG",
      "class": "logging.StreamHandler",
      "formatter": "standart"
		},
    "console2": {
      "level": "WARNING",
      "class": "logging.StreamHandler",
      "formatter": "standart"
		},
    "file": {
			"level": "INFO",
			"class": "logging.FileHandler",
			"filename": "logs/infos.log",
      "formatter": "verbose",
			"mode": "w"
		},
    "music": {
			"level": "INFO",
			"class": "logging.FileHandler",
			"filename": "logs/music.log",
      "formatter": "verbose",
			"mode": "w"
		}
	},
  "loggers": {
    "bot": {
      "handlers": ["console"],
      "level": "INFO",
      "propagate": False
		},
    "discord": {
      "handlers": ["console2", "file"],
      "level": "INFO",
      "propagate": False
		},
    "music": {
      "handlers": ["console", "music"],
      "level": "INFO",
      "propagate": False
		}
	}
}

dictConfig(LOGGIN_CONFIG)