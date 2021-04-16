import discord

# сам бот хранится в клиенте
client = discord.Client()

TOKEN = 'ODMyMjkxMjc2OTcxOTY2NDY1.YHhppw.UQsUsjDYr2CgrGdt5KF2B6Vqvlk'

@client.event
async def text_message(message):
    await message.channel.send('hello!')

client.run(TOKEN)
