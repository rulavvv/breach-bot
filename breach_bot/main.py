"""
Main script
"""
import sys
import logging

import discord

from breach_bot.config import read_config_from_env
from breach_bot.constants import LAUNCH_KEY
from breach_bot.ult import ult

logger = logging.getLogger(__name__)
sh = logging.StreamHandler(sys.stdout)
sh.setLevel(logging.INFO)
logger.setLevel(logging.INFO)
logger.addHandler(sh)

client = discord.Client()
config = read_config_from_env()


@client.event
async def on_ready():
    logger.info(f"Launched as {client}")


# Check message for ULT
@client.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return

    if message.content == LAUNCH_KEY:
        await ult(message)


client.run(config.token)
