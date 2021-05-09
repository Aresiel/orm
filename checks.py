import discord
from discord.ext import commands


def is_aresiel():
    def predicate(ctx):
        return ctx.message.author.id == 104933285506908160
    return commands.check(predicate)
