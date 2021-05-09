from discord.ext import commands
import config

bot = commands.AutoShardedBot(
    command_prefix=config.prefix,
    case_insensitive=True,
    owner_id=config.owner,
    description=config.description
)

for module in config.modules:
    bot.load_extension(module)

bot.run(config.token)