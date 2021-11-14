import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import json
import sys, traceback

#configs
load_dotenv("./config/.env")
TOKEN = os.getenv("token")
PREFIX = os.getenv("prefix")


bot = commands.Bot(command_prefix=f'{PREFIX}')
bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(
        status=discord.Status.idle, 
        activity=discord.Activity(type=discord.ActivityType.watching, name=f"{PREFIX}help")
    )
    print("Bot online!")


with open ('extension/module.json', 'r') as data:
    cog_data = json.load(data)
    extension = cog_data['imports']

if __name__ == "__main__":
    for modules in extension:
        try:
            bot.load_extension(modules)
            print(f"[/] loaded | {modules}")
        except:
            print(f'Error loading {modules}', file=sys.stderr)
            traceback.print_exc()
            

bot.run(f"{TOKEN}")
   