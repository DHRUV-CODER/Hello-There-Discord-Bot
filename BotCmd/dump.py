import discord
from discord.ext import commands


class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['convey', 'speak'])
    async def say(self, ctx, *, msg):
        embed = discord.Embed(title="")
        embed = discord.Embed(description=f"**{msg}**")
        await ctx.send(embed=embed)

    @commands.command()
    async def emo(self, ctx):
        await ctx.send(" <:gold:803174264445861888> ")

    @commands.command()
    async def hi(self, ctx):
        await ctx.message.add_reaction('🙋‍♂️')
        await ctx.message.add_reaction('🇭')
        await ctx.message.add_reaction('🇮')

    @commands.command()
    async def u_suck(self, ctx):
        await ctx.message.add_reaction('💢')
        await ctx.message.add_reaction('🇲')
        await ctx.message.add_reaction('🇩')
        await ctx.message.add_reaction('🇫')
        await ctx.message.add_reaction('🇰')
        await ctx.message.add_reaction('🇰')
        await ctx.message.add_reaction('🤏')

    @commands.command()
    async def XavierAnna(self, ctx):
        await ctx.message.add_reaction('<:xavier:799176988387573760>')


def setup(bot):
    bot.add_cog(Stats(bot))
