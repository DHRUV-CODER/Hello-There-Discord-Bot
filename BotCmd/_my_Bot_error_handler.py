import discord
import datetime
from discord.ext import commands


class FkError(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title=':x: Command Error', colour=0x992d22)
            embed.add_field(name='Error', value=error)
            embed.add_field(name='Guild', value=ctx.guild,inline=False)
            embed.add_field(name='Channel', value=ctx.channel)
            embed.add_field(name='User', value=ctx.author)
            embed.add_field(name='Message', value=ctx.message.clean_content)
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed,delete_after=25)
        elif isinstance(error, commands.CommandNotFound):
            embed = discord.Embed(title=':x: Command Error', colour=0x992d22)
            embed.add_field(name='Error', value=error)
            embed.add_field(name='Guild', value=ctx.guild,inline=False)
            embed.add_field(name='Channel', value=ctx.channel)
            embed.add_field(name='User', value=ctx.author)
            embed.add_field(name='Message', value=ctx.message.clean_content)
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed,delete_after=25)
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(title=':x: Command Error', colour=0x992d22)
            embed.add_field(name='Error', value=error)
            embed.add_field(name='Guild', value=ctx.guild,inline=False)
            embed.add_field(name='Channel', value=ctx.channel)
            embed.add_field(name='User', value=ctx.author)
            embed.add_field(name='Message', value=ctx.message.clean_content)
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed,delete_after=25)
        # elif isinstance(error, commands.CommandInvokeError):
        #     embed = discord.Embed(title=':x: Command Error', colour=0x992d22)
        #     embed.add_field(name='Error', value=error)
        #     embed.add_field(name='Guild', value=ctx.guild,inline=False)
        #     embed.add_field(name='Channel', value=ctx.channel)
        #     embed.add_field(name='User', value=ctx.author)
        #     embed.add_field(name='Message', value=ctx.message.clean_content)
        #     embed.timestamp = datetime.datetime.utcnow()
        #     await ctx.send(embed=embed,delete_after=25)
        else:
            raise error



def setup(bot):
    bot.add_cog(FkError(bot))
