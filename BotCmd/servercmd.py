import discord
from discord.ext import commands


class ServerCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['Server', 'serverinfo', 'infoserver'])
    async def server(self,ctx):
        name = str(ctx.guild.name)
        description = str(ctx.guild.description)

        owner = str(ctx.guild.owner)
        id = str(ctx.guild.id)
        region = str(ctx.guild.region)
        memberCount = str(ctx.guild.member_count)

        icon = str(ctx.guild.icon_url)

        embed = discord.Embed(
            title=name + " || __Server Information__",
            # description=description,
            color=discord.Color.gold())
        embed.set_thumbnail(url=icon)
        embed.add_field(name="Owner", value=owner, inline=True)
        embed.add_field(name="Server ID", value=id, inline=True)
        embed.add_field(name="Region", value=region, inline=True)
        embed.add_field(name="Member Count", value=memberCount, inline=True)

        await ctx.send(embed=embed)


    @commands.command(aliases=['owner'])
    async def serverOwner(self,ctx):
        await ctx.send(f'`So the Boss Here is` ** {ctx.guild.owner}**')


    @commands.command(aliases=['icon'])
    async def serverIcon(self,ctx):
        await ctx.send(ctx.guild.icon_url)


    @commands.command(aliases=['totalmember'])
    async def serverMember(self,ctx):
        # memberCount = str(ctx.guild.member_count)
        await ctx.send(f'`No of members Are`: **{ctx.guild.member_count}**')


    @commands.command(aliases=['serverarea', 'serverregion', 'region'])
    async def serverRegion(self,ctx):
        await ctx.send(f'`Server Region is ` **{ctx.guild.region}**')

def setup(bot):
    bot.add_cog(ServerCmd(bot))
