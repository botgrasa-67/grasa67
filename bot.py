import os
import random
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"¡Bot conectado con éxito como {bot.user}!")
    await bot.change_presence(activity=discord.Game(name="Grasa 67 ⚡ | !ayuda"))

# Comando 1: Medidor de Aura
@bot.command()
async def aura(ctx, usuario: discord.Member = None):
    usuario = usuario or ctx.author
    puntos_aura = random.randint(-1000, 1000)
    
    if puntos_aura > 0:
        msg = f"✨ **{usuario.display_name}** tiene **+{puntos_aura}** de Aura. ¡Totalmente GigaChad!"
    else:
        msg = f"💀 **{usuario.display_name}** tiene **{puntos_aura}** de Aura. Cayó en desgracia."
        
    await ctx.send(msg)

# Comando 2: Juanfer con texto e imagen directa
@bot.command()
async def juanfer(ctx):
    await ctx.send("https://media1.tenor.com/m/b1hLitFQ5jMAAAAd/quintero-river-plate.gif")

# Respuestas automáticas por palabras clave
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.lower() == "ip":
        await message.channel.send("🌐 La IP del server es: `pronto...`")

    await bot.process_commands(message)

bot.run(os.getenv("DISCORD_TOKEN"))
