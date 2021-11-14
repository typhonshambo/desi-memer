import discord
from discord.ext import commands

import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'utils')))
from utils.scrapper import *

class randomMeme(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def meme(self, ctx):
        post = ranMeme()
        await ctx.send(embed=post)

    @commands.command()
    async def desimeme(self, ctx):
        post = desiMeme()
        await ctx.send(embed=post)



def setup(client):
    client.add_cog(randomMeme(client))
   