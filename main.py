import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.all()
bot = commands.Bot(".", intents=intents)
token = os.getenv("TOKEN")

if not token:
    raise RuntimeError("A variável de ambiente TOKEN não está definida.")

@bot.event
async def on_ready():
    print("Apolo acordou!!")

@bot.command()
async def somar(ctx:commands.Context, num1, num2):
    soma = int(num1) + int(num2)
    nome_user = ctx.author.name
    await ctx.reply(f"{nome_user}, a soma entre {num1} e {num2} é: {soma}.")

bot.run(token)