import random
import aiohttp
from discord.ext import commands
import discord


class Fort(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def fort(self, ctx, *, playername):
        try:
            async with ctx.channel.typing():
                async with aiohttp.ClientSession() as cs:
                    async with cs.get(
                            f"https://fortnite-api.com/v1/stats/br/v2?name={playername}"
                    ) as r:
                        data = await r.json(content_type=None)

                        embed = discord.Embed(
                            title=
                            f"Showing Stats For Player : __{playername}__ <a:noob:805793279978504193>",
                            color=0x50e1ed)
                        embed.add_field(
                            name='Level 🔼',
                            value="`{}`".format(
                                data['data']['battlePass']['level']),
                            inline=True)
                        embed.add_field(
                            name='Progress',
                            value="`{}`".format(
                                data['data']['battlePass']['progress']),
                            inline=True)
                        embed.add_field(
                            name='Matches Played',
                            value="`{}`".format(data['data']['stats']['all']
                                                ['overall']['matches']),
                            inline=False)
                        embed.add_field(
                            name='Wins',
                            value="`{}`".format(data['data']['stats']['all']
                                                ['overall']['wins']),
                            inline=False)
                        embed.add_field(
                            name=' ☠',
                            value="`{}`".format(data['data']['stats']['all']
                                                ['overall']['deaths']),
                            inline=True)
                        embed.add_field(
                            name='KDr <a:tenor:805793777197383721>',
                            value="`{}`".format(
                                data['data']['stats']['all']['overall']['kd']),
                            inline=True)
                        embed.add_field(
                            name='Score',
                            value="`{}`".format(data['data']['stats']['all']
                                                ['overall']['score']),
                            inline=False)
                        embed.add_field(
                            name='Score Per Min',
                            value="`{}`".format(data['data']['stats']['all']
                                                ['overall']['scorePerMin']),
                            inline=True)
                        embed.add_field(
                            name='/ Match',
                            value="`{}`".format(data['data']['stats']['all']
                                                ['overall']['scorePerMatch']),
                            inline=True)
                        embed.add_field(
                            name='Top 3️⃣',
                            value="`{}`".format(data['data']['stats']['all']
                                                ['overall']['top3']),
                            inline=False)
                        embed.add_field(
                            name='Top 5️⃣',
                            value="`{}`".format(data['data']['stats']['all']
                                                ['overall']['top5']),
                            inline=True)
                        embed.add_field(
                            name='Top 🔟',
                            value="`{}`".format(data['data']['stats']['all']
                                                ['overall']['top10']),
                            inline=True)
                        embed.set_thumbnail(
                            url=
                            "https://dehayf5mhw1h7.cloudfront.net/wp-content/uploads/sites/1052/2019/08/13071156/fortnite-logo.jpg"
                        )
                        embed.add_field(
                            name='Kills',
                            value="`{}`".format(data['data']['stats']['all']
                                                ['overall']['kills']),
                            inline=False)
                        embed.add_field(
                            name='Kills Per Min',
                            value="`{}`".format(data['data']['stats']['all']
                                                ['overall']['killsPerMin']),
                            inline=True)
                        embed.add_field(
                            name='/ Match',
                            value="`{}`".format(data['data']['stats']['all']
                                                ['overall']['killsPerMatch']),
                            inline=True)
                        embed.add_field(
                            name='Win Rate',
                            value="`{}`".format(data['data']['stats']['all']
                                                ['overall']['winRate']),
                            inline=True)
                        embed.add_field(
                            name='Mins Played',
                            value="`{}`".format(data['data']['stats']['all']
                                                ['overall']['minutesPlayed']),
                            inline=True)
                        embed.add_field(name='Players Out Lived ',
                                        value="`{}`".format(
                                            data['data']['stats']['all']
                                            ['overall']['playersOutlived']),
                                        inline=False)
                        embed.add_field(name='Played Game Last Time:',
                                        value="```css\n{} ```".format(
                                            data['data']['stats']['all']
                                            ['overall']['lastModified']),
                                        inline=True)
                        await ctx.send(embed=embed)
        except:
            embed = discord.Embed(title="Player Not Found",
                                  description="awww",
                                  color=0xfb0000)
            embed.set_thumbnail(
                url=
                "https://media1.tenor.com/images/0d2ab2a829a39772546a1439468ad70b/tenor.gif?itemid=4995479"
            )
            await ctx.send(embed=embed)

    @commands.command()
    async def fortcode(self, ctx, code):
        try:
            async with ctx.channel.typing():
                async with aiohttp.ClientSession() as cs:
                    async with cs.get(
                            f"https://fortnite-api.com/v2/creatorcode?name={code}"
                    ) as r:
                        data = await r.json()

                        embed = discord.Embed(title=data['data']['code'],
                                              color=0xccce84)
                        embed.add_field(name="ID",
                                        value=data['data']['account']['id'])
                        embed.add_field(name="Name",
                                        value=data['data']['account']['name'])
                        embed.add_field(name="Status Of Code",
                                        value=data['data']['status'],
                                        inline=False)
                        embed.add_field(name="Verified",
                                        value=data['data']['verified'])
                        embed.set_thumbnail(
                            url=
                            "https://legiit-service.s3.amazonaws.com/4285d861bc62cba0f06e6a1e95a2f08a/3514eb9be591e93bc3c9dd4bb042e5a3.PNG"
                        )
                        await ctx.send(embed=embed)
                        await ctx.message.add_reaction(
                            '<a:verified:794968371669499924>')
        except:
            embed = discord.Embed(title="Not Found In Data",
                                  description="awww",
                                  color=0xfb0000)
            embed.set_thumbnail(
                url=
                "https://media1.tenor.com/images/0d2ab2a829a39772546a1439468ad70b/tenor.gif?itemid=4995479"
            )
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Fort(bot))
