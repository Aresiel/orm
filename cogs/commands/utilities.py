from discord.ext import commands
import helpers
import checks

def setup(bot):
    bot.add_cog(Utility(bot))


class Utility(commands.Cog, name="Utility"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="The bot's ping")
    async def ping(self, ctx):
        await ctx.send(f'Latency: {round(self.bot.latency * 1000)}ms')

    @commands.command(brief="For testing log levels")
    @commands.is_owner()
    async def test_log_levels(self, ctx):
        helpers.info("Test: Level INFO")
        helpers.warn("Test: Level WARN")
        helpers.error("Test: Level ERROR")
        helpers.critical("Test: Level CRITICAL")
