import discord
import os
import random 

TOKEN = #Token here

client = discord.Client()
PREFIX = 'bot!'

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('Bot is online now')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="bot!help"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "bot!amistupid":
        await message.channel.send("Yes, you\'re stupid <@{user.id}>")
    if message.content == "bot!test":
        await message.channel.send("Yes I'm working")
    if message.content == "bot!hi":
        await message.channel.send("Hello <@{user.id}>")
    
    if message.content == "bot!help":
        msg = '```Panda Bot Command List:```'
        await message.channel.send(msg)
        msg = '```bot!amistupid   : Tells you if you\'re stupid```'
        await message.channel.send(msg)
        msg = '```bot!hi          : Greets you```'
        await message.channel.send(msg)
#        msg = '```bot!8ball {Question} : Answers your 8 ball question```'
#        await message.channel.send(msg)
        msg = '```bot!ping        : Pong!```'
        await message.channel.send(msg)
        msg = '```bot!help        : Shows this message```'
        await message.channel.send(msg)

    if message.content == "bot!ping":
        await message.channel.send("Pong!")

    if message.content == "bot!8ball":
        async def ball(ctx):
            responses = [
                'It is decidedly so.',
                'Without a doubt.',
                'Yes - definitely.',
                'You may rely on it.',
                'As I see it, yes.',
                'Most likely.',
                'Signs point to yes.',
                'Reply hazy, try again.',
                'Ask again later.',
                'Better not tell you now.',
                'Cannot predict now.',
                'Concentrate and ask again.',
                'Not gonna happen fam.',
                'My reply is no.',
                'My sources say no.',
                'Outlook not so good.',
                'Outlook good.',
                'Yes.',
                'Very doubtful.',]
#            await ctx.('Question: {question}\nAnswer:  [random.choice(responses)]')
            await message.channel.send(ctx.message.channel, "{}".format(random.choice(responses)))

client.run(TOKEN)

