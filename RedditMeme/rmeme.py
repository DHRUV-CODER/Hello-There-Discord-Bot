import discord
from discord.ext import commands
import random
import aiohttp


class Rmeme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.is_nsfw()
    async def rmeme(self, ctx,subreddit="meme"):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get(f"https://meme-api.herokuapp.com/gimme/{subreddit}") as r:
                    data = await r.json()

                    embed = discord.Embed(title=data['title'])
                    embed.set_image(url=data['url'])
          
                    await ctx.send(embed=embed)
    
    @rmeme.error
    async def Rmeme_error(self,ctx, error):
        if isinstance(error, commands.errors.NSFWChannelRequired):
            embed = discord.Embed(color=0xff2d15)
            embed.add_field(name="Some Of Subrredit May Have NSFW Content",
                            value="`Enable NSFW or Make A Spearate Channel`",
                            inline=True)
            embed.add_field(name="Try  Our Meme Command Instead ",
                            value="`?meme`",
                            inline=False)
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Rmeme(bot))
