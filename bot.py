import discord
from discord.ext import commands
import random

# Configuración de permisos (Intents)
intents = discord.Intents.default()
intents.message_content = True  # Para que el bot lea los mensajes

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"¡Bot conectado con éxito como {bot.user}!")
    # Cambia la actividad del bot en Discord
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

# Comando 2: Respuesta con la imagen de Juanfer
@bot.command()
async def juanfer(ctx):
    await ctx.send("https://media.giphy.com/media/l0HlBO7eyXzSZkJri/giphy.gif")

# Respuestas automáticas por palabras clave
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Si alguien pone "ip", responde automático
    if message.content.lower() == "ip":
        await message.channel.send("🌐 La IP del server es: `pronto...`")

    await bot.process_commands(message)

# Pegá tu Token entre las comillas
bot.run("MTUzODI5ODMyMDgxMDkzODQwMQ.GROUWc.j8xL-4J6X9WGaeHZAvzATex4KWdyiOs4J69Z1c")