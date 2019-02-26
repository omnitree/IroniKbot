import asyncio
import random

import discord
from discord.ext import commands

from Bot_DB.Azure.Load_Azure import test_dict


class FunCog(commands.Cog, name="Fun stuff"):

    def __init__(self, client):
        self.client = client

    async def member_pic(self, ctx, member_name, group_name):
        try:
            max_num = test_dict[group_name][str.lower(member_name)]
            member_name = str.lower(member_name)
            image_url = 'https://ironicbot2.azureedge.net/{}/{}/{}.jpg'.format(group_name, member_name,
                                                                               random.randrange(1, max_num))

            messages = ["Literally best girl", "I love you " + member_name + "!", "But does starry know who that is?",
                        "Lets be honest, you love her too", group_name + " just wouldn't be the same"]

            tmp = discord.Embed()
            tmp.set_image(url=image_url)
            tmp.set_footer(text=random.choice(messages))

            await ctx.send(embed=tmp)
        except Exception as exception:
            print("Oops! Something went wrong... " + str(exception))
            await ctx.send("Oops! Something went wrong... " + str(exception))

        await asyncio.sleep(100)

    @commands.command(pass_context=True)
    async def twice(self, ctx, arg):
        """Give it a name, Get a picture."""

        await self.member_pic(ctx, arg, 'twice')
        await asyncio.sleep(100)

    @commands.command(pass_context=True)
    async def redvelvet(self, ctx, arg):
        """Give it a name, Get a picture."""
        await self.member_pic(ctx, arg, 'redvelvet')

        await asyncio.sleep(100)

    @commands.command(pass_context=True)
    async def nice(self, ctx):

        """Just says nice."""

        await ctx.send("Nice.")

        await asyncio.sleep(100)

    @commands.command(pass_context=True)
    async def dab(self, message: discord.Message):

        """Summon Momo to dab on them haters."""

        author = str(message.author.mention)

        target = message.content[5:]

        if target == '':
            tmp = discord.Embed(description=author + ' DABBED')
        else:
            tmp = discord.Embed(description=author + ' DABBED ON ' + target)

        tmp.set_image(url='https://ironicbot2.azureedge.net/twice/gif/momodab.gif')
        tmp.set_footer(text='Powered by Memes')
        await ctx.send(embed=tmp)

    @commands.command(pass_context=True)
    async def karma(self, message: discord.Message):

        """Karma comes back to bite ya."""

        author = str(message.author.mention)

        target = message.content[7:]

        if target == '':
            tmp = discord.Embed(description="WASTED!")
        else:
            tmp = discord.Embed(description=target + ' is WASTED!')

        tmp.set_image(url='https://ironicbot2.azureedge.net/twice/gif/ezgif-1-073e5fd8fe.gif')
        tmp.set_footer(text='Powered by Memes')
        await ctx.send(embed=tmp)

    @commands.command(pass_context=True)
    async def cutecat(self, ctx):

        """Lookit this cutie"""

        tmp = discord.Embed(description="CUTE CAT DETECTED")

        tmp.set_image(url='https://thumbs.gfycat.com/AgileHardtofindBug-small.gif')
        tmp.set_footer(text='Powered by Memes')
        await ctx.send(embed=tmp)

def setup(bot):
    bot.add_cog(FunCog(bot))

