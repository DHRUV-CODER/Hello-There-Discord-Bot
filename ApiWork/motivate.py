import discord
from aiohttp import ClientSession
from discord.ext import commands, tasks


class API(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="motivate",
                      description="hi",
                      aliases=['quote', 'boost'])
    async def motivate(self, ctx):
        async with ctx.channel.typing():
            url = "https://quotes15.p.rapidapi.com/quotes/random/"

            headers = {
                'x-rapidapi-key':
                "0d0c7dce72msh502b2dc1d9800f2p1a78b2jsn3ee85834582a",
                'x-rapidapi-host': "quotes15.p.rapidapi.com"
            }
            async with ClientSession() as session:
                async with session.get(url, headers=headers) as response:
                    r = await response.json()
                    # await ctx.send(f"*{r['content']}*")
                    embed = discord.Embed(title="", color=0x35fd44)
                    embed.add_field(name="Todays Quote",
                                    value=f"`{r['content']}`",
                                    inline=True)
                    await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(API(bot))
