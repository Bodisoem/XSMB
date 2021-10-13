import discord
import os
import requests
import json
from discord.ext import commands
import random
from keep_alive import keep_alive

bot = commands.Bot(command_prefix='$')


def get_quote():
	# GET
	response = requests.get("https://zenquotes.io/api/random")
	json_data = json.loads(response.text)
	quote = json_data[0]['q']+ " -"+ json_data[0]['a']
	return quote

def get_random():
	return random.randrange(10)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='hello')
async def hello(ctx):

	await ctx.send('Chao xìn, bậc thầy giải mã những giấc mơ đã tới! Các con vk cần một lời tiên tri thì call ngay nhá.')

@bot.command(name='vebo', help='Cảm thấy chơi đã đủ và cần về bờ, nháy máy $vebo để nhận được những câu quote lấy lại tinh thần khởi nghiệp lại vào ngày mai.')
async def vebo(ctx):
	quote = get_quote()
	await ctx.send(quote)

@bot.command(name='danhlo', help='Cần một con số trước 6 rưỡi chiều hôm nay? Gọi ngay cho con vk với cú pháp $danhlo.')
async def danhlo(ctx):
	try:
		arg1 = get_random()
		arg2 = get_random()
	except ValueError:
		await ctx.send("Hỏng rồi, đéo tìm ra số con vk ạ.")
	else:
		await ctx.send('Con số may mắn của con vk là '+f"||{arg1}||"+f"||{arg2}||"+'. Nháy ngay cho tổng đài trước sáu rưỡi chiều hoặc bốc lấy cái bát to to vào nhá!')

keep_alive()
bot.run(os.environ['TOKEN'])
	