# PANDA BOT VERSION 0.4 ©2020 BENNO PRINS

import discord
import random
import os
from discord.ext.commands import bot
from os import system, name 
from time import sleep

def clear(): 
    # for Windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for MacOS and Linux
    else: 
        _ = system('clear') 

TOKEN = '{Token here}'
PREFIX = 'pbot!'

client = discord.Client(command_prefix=PREFIX)

print('Starting bot...')

@client.event
async def on_ready():
    clear()
    print('Logged in as')
    print('bot name: ' + client.user.name)
    print(client.user.id)
    print('------------------')
    print('bot is online now')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="pbot!help"))
    print('Status has been set to "Listening to pbot!help"')
    print('-----------------------------------------------')
    print('Secret commands:')
    print('pbot!test - sends I\'m working')
    print('pbot!chatrevive - Mentions everyone')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

#    if message.content == "banhammer":
#        msg = 'I can\'t ban you but my creator can, {0.author.mention}'.format(message)
#        await message.channel.send(msg)

    if 'pbot!amistupid' in message.content:
        msg = 'Yes, you\'re stupid, because you aren\'t using 8ball for this, {0.author.mention}'.format(message)
        await message.channel.send(msg)
        
    if 'pbot!test' in message.content:
        await message.channel.send("Yes I'm working")
        
    if 'pbot!hi' in message.content:
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)

    if 'pbot!chatrevive' in message.content:
        msg = '@everyone wake up!'.format(message)
        await message.channel.send(msg)

    if 'pbot!invite' in message.content:
        msg = 'Here\'s the invite link: https://discordapp.com/oauth2/authorize?client_id=695967478584573984&scope=bot'.format(message)
        await message.channel.send(msg)
    
    if 'pbot!help' in message.content:
        msg = '```Panda bot Command List:```'
        await message.channel.send(msg)
        msg = '```pbot!amistupid   : Tells you if you\'re stupid```'
        await message.channel.send(msg)
        msg = '```pbot!hi          : Greets you```'
        await message.channel.send(msg)
        msg = '```pbot!ping        : Pong!```'
        await message.channel.send(msg)
        msg = '```pbot!8ball        : Answers your 8ball question```'
        await message.channel.send(msg)
        msg = '```pbot!help        : Shows this message```'
        await message.channel.send(msg)
        msg = '```pbot!invite      : Sends a bot invite```'
        await message.channel.send(msg)

    if 'pbot!ping' in message.content:
        msg = 'Pong!'
        await message.channel.send(msg)

    if 'pbot!8ball' in message.content:
        possible_responses = [
        'It is decidedly so',
        'Without a doubt',
        'Yes - definitely',
        'You may rely on it',
        'As I see it, yes',
        'Most likely',
        'Signs point to yes',
        'Reply hazy, try again',
        'Ask again later',
        'Better not tell you now',
        'Cannot predict now',
        'Concentrate and ask again',
        'Not gonna happen fam',
        'My reply is no',
        'My sources say no',
        'Outlook not so good',
        'Outlook good',
        'Yes',
        'Very doubtful',
        ]
        await message.channel.send(random.choice(possible_responses) + ", " + message.author.mention)

client.run(TOKEN)


