import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "!", description = "")

@bot.event
async def on_ready():
    print("Bot en marche")

@bot.command()
async def casier(ctx, nom):
    print("coucou")
    if nom == "caca":
        await ctx.send("tg")
    await ctx.send("Voici le casier judiciaire de" ,nom)

bot.run("ODM1MTcyNjA5NzI1MDM4NjUz.YILlGg.CzF_oaE4bR3jYVORrAjYhyJrTwk")