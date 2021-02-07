import discord
from discord.ext import commands
import random
import aiohttp


class MEme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def meme(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://meme-api.herokuapp.com/gimme/meme") as r:
                    data = await r.json()

                    embed = discord.Embed(title=data['title'])
                    embed.set_image(url=data['url'])

                    await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(MEme(bot))
