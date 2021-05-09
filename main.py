from discord.ext import commands
from colorama import init, deinit
import config
import helpers

init()

bot = commands.AutoShardedBot(
    command_prefix=config.prefix,
    case_insensitive=True,
    owner_id=config.owner,
    description=config.description
)

for extension in config.modules:
    try:
        bot.load_extension(extension)
        helpers.info(f'Loaded {extension}')
    except:
        helpers.warn(f'Failed to load {extension}')

bot.run(config.token)
deinit()