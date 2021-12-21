# 디스코드 모듈 import
import discord

bot_token = ""

# bot을 discord.Client()로 선언
bot = discord.Client()  # 구버전 방식

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print('------')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.author.bot:
        return
    await message.channel.send(message.content)


bot.run(bot_token)

