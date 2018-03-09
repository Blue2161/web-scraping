import discord
import asyncio
import bot_token
from discord.ext import commands


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # create the background task and run it in the background
        self.bg_task = self.loop.create_task(self.my_background_task())
        
    description = '''Test bot'''
    bot = commands.Bot(command_prefix='!', description=description)

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def my_background_task(self):
        await self.wait_until_ready()
        counter = 0
        channel = self.get_channel(395078356703510541) # channel ID goes here
        while not self.is_closed():
            counter += 1
            await channel.send(counter)
            print(counter)
            await asyncio.sleep(10) # task runs every 10 seconds

    async def testcommand(ctx):
        await ctx.send('test command with background action')


client = MyClient()
client.run(bot_token.TOKEN)
