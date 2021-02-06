import discord
from discord.ext import commands



class Common(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # ping command

    @commands.command(aliases=['avatar'])
    async def av(self,ctx,*,member: discord.Member = None):  # set the member object to None
        if not member:  # if member is no mentioned
            member = ctx.message.author  # set member as the author
        userAvatar = member.avatar_url
        await ctx.send(userAvatar)

    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'**Pong!** Latency: {round(self.bot.latency * 1000)}ms')

def setup(bot):
    bot.add_cog(Common(bot))
