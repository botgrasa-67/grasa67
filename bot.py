import os
import random
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f"¡Bot conectado con éxito como {bot.user}!")
    await bot.change_presence(activity=discord.Game(name="Grasa 67 ⚡ | !ayuda"))

# Comando: Ayuda
@bot.command()
async def ayuda(ctx):
    embed = discord.Embed(
        title="🐻 Comandos de El Oso Pratto",
        description="Listado de todo lo que podés usar en el server:",
        color=discord.Color.red()
    )
    embed.add_field(name="!juanfer", value="Manda el golazo de Juanfer en Madrid.", inline=False)
    embed.add_field(name="!miguel", value="Manda la foto del Chad Miguel.", inline=False)
    embed.add_field(name="!aura [@usuario]", value="Mide el aura de alguien.", inline=False)
    embed.add_field(name="!penal [izquierda/centro/derecha]", value="Pateale un penal al Oso.", inline=False)
    embed.add_field(name="!frase", value="Tira una frase épica.", inline=False)
    await ctx.send(embed=embed)

# Comando: Medidor de Aura
@bot.command()
async def aura(ctx, usuario: discord.Member = None):
    usuario = usuario or ctx.author
    puntos_aura = random.randint(-1000, 1000)
    
    if puntos_aura > 0:
        msg = f"✨ **{usuario.display_name}** tiene **+{puntos_aura}** de Aura. ¡Totalmente GigaChad!"
    else:
        msg = f"💀 **{usuario.display_name}** tiene **{puntos_aura}** de Aura. Cayó en desgracia."
        
    await ctx.send(msg)

# Comando: Juanfer
@bot.command()
async def juanfer(ctx):
    await ctx.send("https://static2.klipy.com/ii/4e7bea9f7a3371424e6c16ebc93252fe/f0/86/zoHTLrgTPB8E.gif")

# Comando: Miguel
@bot.command()
async def miguel(ctx):
    await ctx.send("🗿 **MIGUEL EL CHAD**\nhttps://static2.klipy.com/ii/d6b0ce929193df3c242ac34b5654d2ce/70/e8/UBZsJ60d.gif")

# Comando: Juego de Penal
@bot.command()
async def penal(ctx, direccion: str = None):
    if not direccion or direccion.lower() not in ["izquierda", "centro", "derecha"]:
        await ctx.send("⚽ Decime dónde pateás: `!penal izquierda`, `!penal centro` o `!penal derecha`")
        return

    opciones = ["izquierda", "centro", "derecha"]
    atajada = random.choice(opciones)
    pateo = direccion.lower()

    if pateo == atajada:
        await ctx.send(f"🧤 **¡ATAJÓ EL OSO!** Se tiró a la **{atajada}** y te la sacó al córner.")
    else:
        await ctx.send(f"⚽ **¡GOOOOOOOL!** Pateaste a la **{pateo}** y el Oso se tiró a la **{atajada}**. Modosodefinitivo.")

# Comando: Frases
@bot.command()
async def frase(ctx):
    frases = [
        "🎩 *Que la gente crea, porque tiene con qué creer.*",
        "🐻 *Sacá del medio.*",
        "⚪🔴⚪ *Y va el tercero, y va el tercero...*",
        "💪 *A ganar o morir, acá no se afloja.*"
    ]
    await ctx.send(random.choice(frases))

# Respuestas automáticas por palabras clave
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.lower() == "ip":
        await message.channel.send("🌐 La IP del server es: `pronto...`")

    await bot.process_commands(message)

# Siempre al final
bot.run(os.getenv("DISCORD_TOKEN"))
