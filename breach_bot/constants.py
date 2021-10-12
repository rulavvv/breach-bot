"""
Constants
"""

from typing import NamedTuple


class UltSet(NamedTuple):
    text: str
    mp3file: str


LAUNCH_KEY = "ULT"
ULT_SETS = [
    UltSet("ぶっ飛べ!!!!", "voices/enemy_ult.mp3"),
    UltSet("行くぞ!!!!", "voices/friend_ult.mp3"),
    UltSet("OFF YOUR FEET!!!!", "voices/enemy_ult_eng.mp3"),
    UltSet("LETS GO!!!!", "voices/friend_ult_eng.mp3"),
]
WAIT_TIME = 0.1
ULT_N_STEPS = 7
ULT_NAME = "ローリングサンダー"
