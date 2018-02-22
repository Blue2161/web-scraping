import discord
from discord.ext import commands
import pickle
import random
import re

#include files
import bot_token

client = discord.Client
#TOKEN = 'Mzk1MDg0NTIzNjA1MzI3ODcy.DSNvZw.0uK2cTkTrZknUee7406G6twLrgg'

description = '''Blue's bot in Python'''
bot = commands.Bot(command_prefix='!', description=description)

#terminal run confirmation
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    
#when something happens, do something
@bot.event
    
#on message actions
async def on_message(message):
    if message.author == bot.user:
        return

    #watch for a polite greeting and return it
        
    if re.match('hello bot', message.content.replace(',',''), re.IGNORECASE) or re.match('hi bot', message.content.replace(',',''), re.IGNORECASE):
        await message.channel.send('Hello, {0.author.mention}.'.format(message))

    if re.search(r'(?:^|\W)fuck(?:$|\W)', message.content, re.IGNORECASE): #the string escapes could be better (_)
        await message.delete()
    
    #await message.channel.send("Author: {}\nContent: {}\nChannel: {}\n".format(message.author, message.content, message.channel))
    
    try:
        f = open("channel_data_test", "a")
        f.write(str(message.content))
        f.write('\n')
    finally:
        f.close()
    
    await bot.process_commands(message) #use at the end of an on_message to allow further commands

#bot commands
    #images
@bot.command()
async def image(ctx):
    with open('/home/pi/Pictures/1475510626390.png', 'rb') as f:
        await ctx.send('Test', file = discord.File(f))
        
    #read/write commands
@bot.command()
async def write(ctx, *, msg: str):
    """Writes the message to a text file"""
    try:
        f = open("writetest.txt", "a")
        f.write(msg)
        f.write('\n')
    finally:
        f.close()

@bot.command()
async def read(ctx):
    """Reads a message from a text file"""
    try:
        f = open("writetest.txt", "r")
        await ctx.send(f.readlines(4))
    finally:
        f.close()

@bot.command()
async def addquote(ctx, *, msg: str):
    """Adds a quote to a quote file"""
    try:
        f = open("quotelist.txt", "a")
        f.write(msg)
        f.write('\n')
    finally:
        f.close()

@bot.command()
async def quote(ctx):
    """Reads a random quote from quotelist.txt"""
    try:
        f = open("quotelist.txt", "r")
        line = f.readlines()
        await ctx.send(line[random.randint(0, line_count("quotelist.txt")-1)])
    finally:
        f.close()
        
    #misc commands
@bot.command()
async def pingme(ctx):
    await ctx.author.send("Here's your ping.")            
        
@bot.command()
async def emotes(ctx):
    try:
        f = open("emotes", "a")
        f.write(str(discord.Client.emojis))
        f.write('\n')
        """for item in discord.Client.emojis:
            f.write("%s\n" % item)
        """
    finally:
        f.close()

@bot.command()
async def oh(ctx):
    await ctx.send("<:oh:401120327998111744>")
    #await ctx.send('<:oh:>')

@bot.command()
async def echo(ctx, *, message: str): #message has a "consume rest" behavior, while * takes the first argument/word
    await ctx.send(message)

    #random commands
@bot.command()
async def roll(ctx):
    """Rolls from 0 to 100"""
    await ctx.send(random.randint(0, 100))

    #arithmatic commands
@bot.command()
async def hello(ctx):
    """Says hello"""
    await ctx.send("Hello.")

@bot.command()
async def add(ctx, left : int, right : int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def subtract(ctx, left : int, right : int):
    """Subtracts two numbers."""
    await ctx.send(left - right)

@bot.command()
async def multiply(ctx, left : int, right : int):
    """Multiplies two numbers."""
    await ctx.send(left * right)    

@bot.command()
async def divide(ctx, left : int, right : int):
    """Divides two numbers."""
    if right == 0: #ZeroDivision handling
        await ctx.send("Quit trying to break my bot, shithead.")
    else:
        await ctx.send(left / right)

@bot.command()
async def power(ctx, left : int, right : int):
    """Exponential calculation of two numbers."""
    await ctx.send(left ** right)        

@bot.command()
async def floordivide(ctx, left : int, right : int):
    """Rounded division of two numbers."""
    await ctx.send(left // right)

@bot.command()
async def modulus(ctx, left : int, right : int):
    """Remainder after division of two numbers."""
    await ctx.send(left % right)

#functions
    #counts the number of lines in a file
def line_count(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
       
#runs the bot    
bot.run(bot_token.TOKEN)
