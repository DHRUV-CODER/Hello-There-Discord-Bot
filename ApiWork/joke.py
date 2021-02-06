import discord
from discord.ext import commands
import random
import aiohttp


class Joke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def joke(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get(
                        "https://official-joke-api.appspot.com/random_joke"
                ) as r:
                    data = await r.json()

                    embed = discord.Embed(title=data['setup'], color=0xccce84)
                    embed.add_field(name=":-", value=data['punchline'])

                    await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Joke(bot))
