"""
Main script
"""
import asyncio
import random
import sys
import logging
from asyncio import sleep

import discord

from breach_bot.config import read_config_from_env
from breach_bot.constants import ULT_SETS, ULT_NAME, ULT_N_STEPS, WAIT_TIME, LAUNCH_KEY

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


async def ult(message: discord.Message):

    logger.info(f"ULT called by {message.author}")

    # Do nothing if caller is not joining VC
    if message.author.voice is None:
        await message.add_reaction("🤫")
        return
    else:
        await message.add_reaction("🤯")

    channel = message.author.voice.channel
    members = [m for m in channel.members if not m.bot]
    logger.info(f"Original channel: {channel}")
    logger.info(f"Ulting members: {members}")

    # Random voice
    text, voice_file = random.choice(ULT_SETS)

    # Text
    await message.channel.send(text)

    # Scream
    author_vcc = await discord.VoiceChannel.connect(message.author.voice.channel)
    author_vcc.play(discord.FFmpegPCMAudio(voice_file))
    while author_vcc.is_playing():
        await sleep(WAIT_TIME)

    # Channel creation
    vcs: list[discord.VoiceChannel] = []
    for n in range(ULT_N_STEPS):
        try:
            vcs.append(
                (
                    new_vc := await message.guild.create_voice_channel(
                        f"({ULT_NAME} {n + 1})", category=message.author.voice.channel.category
                    )
                )
            )
            await asyncio.gather(*[m.move_to(new_vc) for m in members])
        except Exception:
            pass
        await sleep(WAIT_TIME)

    await asyncio.gather(*[m.move_to(channel) for m in members])

    # Disconnect from channel
    await author_vcc.disconnect(force=False)

    # Channel deletion
    for vc in vcs:
        if vc is not None:
            await vc.delete()
        await sleep(WAIT_TIME)


client.run(config.token)
