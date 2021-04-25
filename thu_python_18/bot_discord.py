import discord
import random

# сам бот хранится в клиенте
client = discord.Client()
TOKEN = 'ODM0ODExMjUwMDkyMjc3Nzgw.YIGUkA.20ejlXs_EdVWMQyMYjKpEWj-Mhc'
# фразы для бота
message_bot_hello = ['Ну хай, ковбой! 🤠', 'Привет', 'Ку. Как дела?']

@client.event
async def on_message(message):
    # проверка на ботов (от спама)
    if message.author.bot == True:
        return
        
    # пишет в консоль сообщения
    print(f'Автор {message.author} написал: {message.content}')
    
    if message.content == 'привет':
        # отправляет сообщения
        await message.channel.send(random.choice(message_bot_hello))

    if message.content == 'как погода':
        # отправляет сообщения
        await message.channel.send('норм')

client.run(TOKEN)
 
