import discord
from discord.ext import commands
import random
import aiohttp


class CoolCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def wink(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get(
                        "https://some-random-api.ml/animu/wink") as r:
                    data = await r.json()

                    embed = discord.Embed(title="😉")
                    embed.set_image(url=data['link'])

                    await ctx.send(embed=embed)

    @commands.command()
    async def hug(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://some-random-api.ml/animu/hug") as r:
                    data = await r.json()

                    embed = discord.Embed(title="")
                    embed.set_image(url=data['link'])

                    await ctx.send(embed=embed)

    @commands.command()
    async def pat(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://some-random-api.ml/animu/pat") as r:
                    data = await r.json()

                    embed = discord.Embed(title="")
                    embed.set_image(url=data['link'])

                    await ctx.send(embed=embed)

    @commands.command()
    async def trigger(self, ctx, *, link):
        await ctx.send(
            f"Take Your Edited Link,||https://some-random-api.ml/canvas/triggered?avatar={link}||"
        )


def setup(bot):
    bot.add_cog(CoolCmd(bot))
