import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$fix'):
        await message.channel.send('Joining voice channel\nBinding to channel.')
        channel = message.author.voice.channel
        if(not channel):
            await message.channel.send('You are not connected to any voice chat.')
        else:
            await channel.connect(reconnect=True, timeout=666666.0)

client.run('place token here.')