import os
import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(".", intents=intents)

@bot.event
async def on_ready():
    print("Apolo acordou!!")

@bot.command()
async def somar(ctx:commands.Context, num1, num2):
    soma = int(num1) + int(num2)
    nome_user = ctx.author.name
    await ctx.reply(f"{nome_user}, a soma entre {num1} e {num2} é: {soma}.")

@bot.event()
async def on_member_join(membro:discord.member):
    canal = bot.get_channel(1382140780050780352)
    await canal.send(f"{membro.mention} chegou. seja bem vindo ao lugar!")

bot.run(os.getenv("TOKEN"))