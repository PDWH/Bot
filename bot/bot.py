#AUTHOR: duhack
#GITHUB: https://github.com/duhack

import discord
from discord.ext import commands, tasks
from discord.utils import get

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='?', intents=intents) #W MIEJSCU '!' USTAW PREFIX BOTA

extensions = ['commands', 'events']

for extension in extensions:
    bot.load_extension(extension)

bot.run('ODQwNjM4MjEwMzU4NzcxNzIy.YJbHVw.PK3U-TaJD-mf9NZbZElauTHgwhA') #TUTAJ WPISZ TOKEN BOTA