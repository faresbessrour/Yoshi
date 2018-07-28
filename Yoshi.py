import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
from bot_commands import commands

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')

@client.event
@asyncio.coroutine
def on_message(message):
    if message.author == client.user: return
    if 'yoshi' in message.content.lower() and 'sorry' in message.content.lower():
        yield from client.send_message(message.channel, 'NP, just don\'t do it again dude')
    elif 'yoshi' in message.content.lower():
        yield from client.send_message(message.channel, 'What do you mean by that?')
    elif message.content.startswith('!'):
        yield from client.send_message(message.channel, commands.commands(message.content))
    elif 'firas' in message.content.lower() and 'great' in message.content.lower():
        yield from client.send_message(message.channel, 'Firas is a great person indeed')
    elif 'firas' in message.content.lower() and 'bad' in message.content.lower():
        yield from client.send_message(message.channel, 'Dude shut up, Firas is great')
    
def main():    
    client.run('NDYyOTcwOTg1NDk5NDU5NTg5.Dj38kw.8mMdLy1vI0-GExgXgRpPQrbHJUw')

if __name__ == '__main__':
    main()
