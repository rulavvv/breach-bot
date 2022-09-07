import sys
import logging

import discord
from pyfiglet import Figlet

from breach_bot.constants import AA_KEY


BLACK = "█"
WHITE = "░"
VALO_WIDTH = 26
CHAR_WIDTH = 5

logger = logging.getLogger(__name__)
sh = logging.StreamHandler(sys.stdout)
sh.setLevel(logging.INFO)
logger.setLevel(logging.INFO)
logger.addHandler(sh)


async def get_aa(message: discord.Message):

    logger.info(f"aagen called by {message.author}")

    await message.add_reaction("😎")

    text = message.content[(len(AA_KEY) + 1) :]

    f = Figlet(font="clr5x6")
    row = ["" for _ in range(6)]
    for charactor in text:
        if charactor == " ":
            row = [r + WHITE for r in row]
        else:
            c = f.renderText(charactor).replace(" ", WHITE).replace("#", BLACK)
            c = [r[:-1] for r in c.split("\n")]
            row = [rr + cc for rr, cc in zip(row, c)]
    if (length := len(row[0])) > 26:
        message.channel.send("長すぎ")
        raise Exception(f"Too long word (word length must be shorter than {VALO_WIDTH // CHAR_WIDTH})")
    else:
        # padding
        needed_pad = VALO_WIDTH - length
        left_pad = -(-needed_pad // 2) * WHITE
        right_pad = (needed_pad // 2) * WHITE
        row = [left_pad + r + right_pad for r in row]

    result = "".join(row)
    await message.channel.send(result)
