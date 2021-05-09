from discord.ext import commands
import helpers
import json
import discord


def setup(bot):
    bot.add_cog(Animals(bot))


class Animals(commands.Cog, name="Animals"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="Cat image!")
    async def cat(self, ctx):
        image = json.loads((await helpers.async_request("https://some-random-api.ml/img/cat")).text)['link']
        fact = json.loads((await helpers.async_request("https://some-random-api.ml/facts/cat")).text)['fact']
        embed = discord.Embed(
            title="Cat!",
            description=f'Fun fact: {fact}'
        ).set_image(url=image)
        await ctx.send(embed=embed)

    @commands.command(brief="Dog image!")
    async def dog(self, ctx):
        image = json.loads((await helpers.async_request("https://some-random-api.ml/img/dog")).text)['link']
        fact = json.loads((await helpers.async_request("https://some-random-api.ml/facts/dog")).text)['fact']
        embed = discord.Embed(
            title="Dog!",
            description=f'Fun fact: {fact}'
        ).set_image(url=image)
        await ctx.send(embed=embed)

    @commands.command(brief="Panda image!")
    async def panda(self, ctx):
        image = json.loads((await helpers.async_request("https://some-random-api.ml/img/panda")).text)['link']
        fact = json.loads((await helpers.async_request("https://some-random-api.ml/facts/panda")).text)['fact']
        embed = discord.Embed(
            title="Panda!",
            description=f'Fun fact: {fact}'
        ).set_image(url=image)
        await ctx.send(embed=embed)

    @commands.command(brief="Fox image!")
    async def fox(self, ctx):
        image = json.loads((await helpers.async_request("https://some-random-api.ml/img/fox")).text)['link']
        fact = json.loads((await helpers.async_request("https://some-random-api.ml/facts/fox")).text)['fact']
        embed = discord.Embed(
            title="Fox!",
            description=f'Fun fact: {fact}'
        ).set_image(url=image)
        await ctx.send(embed=embed)

    @commands.command(brief="Bird image!")
    async def bird(self, ctx):
        image = json.loads((await helpers.async_request("https://some-random-api.ml/img/bird")).text)['link']
        fact = json.loads((await helpers.async_request("https://some-random-api.ml/facts/bird")).text)['fact']
        embed = discord.Embed(
            title="Bird!",
            description=f'Fun fact: {fact}'
        ).set_image(url=image)
        await ctx.send(embed=embed)

    @commands.command(brief="Koala image!")
    async def koala(self, ctx):
        image = json.loads((await helpers.async_request("https://some-random-api.ml/img/koala")).text)['link']
        fact = json.loads((await helpers.async_request("https://some-random-api.ml/facts/koala")).text)['fact']
        embed = discord.Embed(
            title="Koala!",
            description=f'Fun fact: {fact}'
        ).set_image(url=image)
        await ctx.send(embed=embed)

    @commands.command(brief="Red Panda image!")
    async def red_panda(self, ctx):
        image = json.loads((await helpers.async_request("https://some-random-api.ml/img/red_panda")).text)['link']
        embed = discord.Embed(
            title="Red panda!"
        ).set_image(url=image)
        await ctx.send(embed=embed)
