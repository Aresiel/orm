"""
    This file is meant to be copied into `config.py` and filled with correct values.
"""

prefix = ""  # The command prefix
owner = 0  # The owner's id as an integer
description = ""  # A description of your bot
token = ""  # The discord bot token

extensions = [  # The list of extensions to load.
    "jishaku",
    "cogs.commands.utilities",
    "cogs.commands.animals",
    "cogs.events.error_handler"
]
