import discord
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, aliases=['Kick'])
    @commands.has_permissions(administrator=True)
    async def kick(self,ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(
            f'{member.mention} **Has Been Kicked** for Reason **{reason}**.')


    @kick.error
    async def kick_error(self,ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title="Missing permission",
                url=
                "https://support.discord.com/hc/en-us/articles/206029707-How-do-I-set-up-Permissions-",
                description="**You Cant Do That :(**  ",
                color=0xfc4747)
            embed.set_author(name="Need To Have A Role with Adminstrator enabled")
            embed.set_thumbnail(
                url=
                'https://225508-687545-raikfcquaxqncofqfm.stackpathdns.com/wp-content/uploads/2019/07/Hindustani-Bhau.jpg'
            )
            await ctx.send(embed=embed)



    @commands.command(pass_context=True, aliases=['Ban'])
    @commands.has_permissions(administrator=True)
    async def ban(self,ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        embed = discord.Embed(title="Banned",
                              description=member.mention,
                              color=0x928783)
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name="Banned By",
                        value=ctx.message.author.mention,
                        inline=True)
        embed.add_field(name="Reason", value=f"{reason}", inline=False)
        channel = await member.create_dm()
        await ctx.send(embed=embed)
        await channel.send(embed=embed)


    @ban.error
    async def ban_error(self,ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title="Missing permission",
                url=
                "https://support.discord.com/hc/en-us/articles/206029707-How-do-I-set-up-Permissions-",
                description="**You Cant Do That :(**  ",
                color=0xff2115)
            embed.set_author(name="Need To Have A Role with Adminstrator enabled")
            await ctx.send(embed=embed)


    @commands.command(pass_context=True, aliases=['alarm'])
    @commands.has_permissions(administrator=True)
    async def warn(self,ctx, member: discord.Member, *, reason=None):
        channel = await member.create_dm()
        await channel.send(
            f'{member.mention} **Has Been GIVEN A NOTICE ** for Reason **{reason}**'
        )
        await ctx.send(
            f'{member.mention} **Has Been GIVEN A NOTICE ** for Reason **{reason}**'
        )


    @warn.error
    async def warn_error(self,ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title="Missing permission",
                url=
                "https://support.discord.com/hc/en-us/articles/206029707-How-do-I-set-up-Permissions-",
                description="**You Cant Do That :(**  ",
                color=0xfc4747)
            embed.set_author(name="Need To Have A Role with Adminstrator enabled")
            await ctx.send(embed=embed)


    @commands.command(pass_context=True,
                    aliases=['clear', 'erase', 'Clean', 'Clear'])
    @commands.has_permissions(administrator=True)
    async def clean(self,ctx, amount=1):
        await ctx.channel.purge(limit=amount)
        await ctx.send('Cleared by {}'.format(ctx.author.mention) +
                      ' Message Will Be Deleted In **45** __Second__',
                      delete_after=45)
        await ctx.message.delete()

    @clean.error
    async def clear_error(self,ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title="Missing permission",
                url=
                "https://support.discord.com/hc/en-us/articles/206029707-How-do-I-set-up-Permissions-",
                description="**You Cant Do That :(**  ",
                color=0xfc4747)
            embed.set_author(name="Need To Have A Role with Adminstrator enabled")
            await ctx.send(embed=embed)



    @commands.command(pass_context=True, aliases=['alarm'])
    @commands.has_permissions(administrator=True)
    async def warn(self,ctx, member: discord.Member, *, reason=None):
        channel = await member.create_dm()
        await channel.send(
            f'{member.mention} **Has Been GIVEN A NOTICE ** for Reason **{reason}**'
        )
        await ctx.send(
            f'{member.mention} **Has Been GIVEN A NOTICE ** for Reason **{reason}**'
        )


    @warn.error
    async def warn_error(self,ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title="Missing permission",
                url=
                "https://support.discord.com/hc/en-us/articles/206029707-How-do-I-set-up-Permissions-",
                description="**You Cant Do That :(**  ",
                color=0xfc4747)
            embed.set_author(name="Need To Have A Role with Adminstrator enabled")
            await ctx.send(embed=embed)




    @commands.command(pass_context=True, aliases=['gr', 'GiveRole', 'rolegive'])
    @commands.has_permissions(administrator=True)
    async def giverole(self,ctx, user: discord.Member, role: discord.Role):
        await user.add_roles(role)
        await ctx.send(
            f"Hey **{ctx.author.name}**, __{user.name}__ has been giving a role called: **{role.name}**"
        )


    @giverole.error
    async def giverole_error(self,ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title="Missing permission",
                url=
                "https://support.discord.com/hc/en-us/articles/206029707-How-do-I-set-up-Permissions-",
                description="**You Cant Do That :(**  ",
                color=0xfc4747)
            embed.set_author(name="Need To Have A Role with Adminstrator enabled")
            await ctx.send(embed=embed)


    @commands.command(pass_context=True, aliases=['Unban', 'UnBan'])
    @commands.has_permissions(administrator=True)
    async def unban(self,ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name,
                                                  member_discriminator):
                await ctx.guild.unban(user)
                # await ctx.send(f'`Unbanned` {user.mention} wc Back!')
                embed = discord.Embed(title="UnBanned",
                                      description=f"{user.mention}",
                                      color=0x73ff15)
                embed.set_thumbnail(url=user.avatar_url)
                embed.add_field(name="UnBanned By",
                                value=ctx.message.author.mention,
                                inline=True)
                await ctx.send(embed=embed)


    @unban.error
    async def unban_error(self,ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title="Missing permission",
                url=
                "https://support.discord.com/hc/en-us/articles/206029707-How-do-I-set-up-Permissions-",
                description="**You Cant Do That :(**  ",
                color=0xfc4747)
            embed.set_author(name="Need To Have A Role with Adminstrator enabled")
            await ctx.send(embed=embed)

    @commands.command(aliases=['memberinfo'])
    @commands.has_permissions(administrator=True)
    async def userinfo(self,ctx, *, user: discord.Member = None):  # b'\xfc'
        if user is None:
            user = ctx.author
        date_format = "%a, %d %b %Y %I:%M %p"
        embed = discord.Embed(color=0x928783, description=user.mention)
        embed.set_author(name=str(user), icon_url=user.avatar_url)
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="Joined", value=user.joined_at.strftime(date_format))
        members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        embed.add_field(name="Join position", value=str(members.index(user) + 1))
        embed.add_field(name="Registered",
                        value=user.created_at.strftime(date_format))
        if len(user.roles) > 1:
            role_string = ' '.join([r.mention for r in user.roles][1:])
            embed.add_field(name="Roles [{}]".format(len(user.roles) - 1),
                            value=role_string,
                            inline=False)
        perm_string = ', '.join([
            str(p[0]).replace("_", " ").title() for p in user.guild_permissions
            if p[1]
        ])
        embed.add_field(name="Guild permissions", value=perm_string, inline=False)
        embed.set_footer(text='ID: ' + str(user.id))
        return await ctx.send(embed=embed)


    @userinfo.error
    async def userinfo_error(self,ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title="Missing permission",
                url=
                "https://support.discord.com/hc/en-us/articles/206029707-How-do-I-set-up-Permissions-",
                description="**You Cant Do That :(**  ",
                color=0xfc4747)
            embed.set_author(name="Need To Have A Role with Adminstrator enabled")
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Moderation(bot))
