import random
import aiohttp
from discord.ext import commands
import discord

class Images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cat(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("http://aws.random.cat/meow") as r:
                    data = await r.json()

                    embed = discord.Embed(title="")
                    embed.set_image(url=data['file'])

                    await ctx.send(embed=embed)

    @commands.command()
    async def dog(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://random.dog/woof.json") as r:
                    data = await r.json()

                    embed = discord.Embed(title="")
                    embed.set_image(url=data['url'])

                    await ctx.send(embed=embed)


    @commands.command()
    async def fox(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://randomfox.ca/floof/") as r:
                    data = await r.json()

                    embed = discord.Embed(title="")
                    embed.set_image(url=data['image'])

                    await ctx.send(embed=embed)

    @commands.command()
    async def panda(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://some-random-api.ml/img/panda") as r:
                    data = await r.json()

                    embed = discord.Embed(title="")
                    embed.set_image(url=data['link'])

                    await ctx.send(embed=embed) 



    @commands.command()
    async def bird(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://some-random-api.ml/img/birb") as r:
                    data = await r.json()

                    embed = discord.Embed(title="")
                    embed.set_image(url=data['link'])

                    await ctx.send(embed=embed)

    @commands.command()
    async def rp(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://some-random-api.ml/img/red_panda") as r:
                    data = await r.json()

                    embed = discord.Embed(title="")
                    embed.set_image(url=data['link'])

                    await ctx.send(embed=embed)      



                               
def setup(bot):
    bot.add_cog(Images(bot))
