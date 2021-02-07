import discord
from discord.ext import commands
import random
import aiohttp


class Pokemon(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pm(self, ctx, *, pika):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get(
                        f"https://some-random-api.ml/pokedex?pokemon={pika}"
                ) as r:
                    data = await r.json(content_type=None)

                    embed = discord.Embed(title=f"**{pika}**")
                    embed.set_thumbnail(url=data['sprites']['normal'])
                    embed.add_field(name=f'**Description of {pika}**',
                                    value=data['description'],
                                    inline=False)
                    embed.add_field(name=f'**ID**',
                                    value=data['id'],
                                    inline=True)
                    embed.add_field(name=f'**species**',
                                    value=data['species'][0][1],
                                    inline=True)
                    embed.add_field(name=f'Hp',
                                    value=data['stats']['hp'],
                                    inline=True)
                    embed.add_field(name=f'Attack',
                                    value=data['stats']['attack'],
                                    inline=True)
                    embed.add_field(name=f'Defense',
                                    value=data['stats']['defense'],
                                    inline=True)
                    embed.add_field(name=f'Attack',
                                    value=data['stats']['sp_atk'],
                                    inline=True)
                    embed.add_field(name=f'Defend',
                                    value=data['stats']['sp_def'],
                                    inline=True)
                    embed.add_field(name=f'Speed',
                                    value=data['stats']['speed'],
                                    inline=True)
                    embed.add_field(name=f'Total',
                                    value=data['stats']['total'],
                                    inline=True)
                    embed.add_field(name=f'Gender',
                                    value=data['gender'][0],
                                    inline=True)
                    embed.add_field(name=f'Gender',
                                    value=data['gender'][1],
                                    inline=True)

                    await ctx.send(embed=embed)

    @commands.command()
    async def pikachu(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get(
                        "https://some-random-api.ml/img/pikachu") as r:
                    data = await r.json()

                    embed = discord.Embed(title="")
                    embed.set_image(url=data['link'])

                    await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Pokemon(bot))
