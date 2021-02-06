import discord
from discord.ext import commands
import random
import aiohttp


class Covid(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def covid(self, ctx, *, country):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                newcountry = country.capitalize()
                async with cs.get(
                        f"https://covid19-api.weedmark.systems/api/v1/stats?country={newcountry}"
                ) as r:
                    data = await r.json(content_type=None)

                    embed = discord.Embed(
                        title=data['data']['covid19Stats'][0]['country'])
                    embed.add_field(
                        name='City',
                        value=data['data']['covid19Stats'][0]['city'],
                        inline=False)
                    embed.add_field(
                        name='Province',
                        value=data['data']['covid19Stats'][0]['province'],
                        inline=False)
                    embed.add_field(
                        name='Confirmed',
                        value=data['data']['covid19Stats'][0]['confirmed'],
                        inline=True)
                    embed.add_field(
                        name='Deaths',
                        value=data['data']['covid19Stats'][0]['deaths'],
                        inline=True)
                    embed.add_field(
                        name='Recovered',
                        value=data['data']['covid19Stats'][0]['recovered'],
                        inline=True)
                    embed.add_field(name='Message',
                                    value=data['message'],
                                    inline=False)
                    embed.set_thumbnail(
                        url=
                        'https://ec.europa.eu/programmes/creative-europe/sites/default/files/covid19-cdc-unsplash.jpg'
                    )
                    await ctx.send(embed=embed)
                    await ctx.message.add_reaction('🧼')


def setup(bot):
    bot.add_cog(Covid(bot))
