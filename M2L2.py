import discord 
import random
from discord.ext import commands

# Botun Discord API'ye bağlanması için gerekli izinler
intents = discord.Intents.default()
intents.message_content = True  # Botun mesaj içeriğine erişimine izin veriyoruz.

# Botu başlatıyoruz
bot = commands.Bot(command_prefix='!', intents=intents)
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık!')  # Botun başarılı bir şekilde bağlandığını belirten mesaj


@bot.command()
async def ev_atık(ctx):
    ev_atıkları = ["Cam", "Kağıt", "Plastik", "Metal", "Organik_Atık", "Dönüşemeyecek_Atık"]
    atık = random.choice(ev_atıkları)
    await ctx.send(f"Bu atık {atık} kategorisine aittir.")
    
    
@bot.command()
async def bilgilendirici_videolar(ctx):
    videolar = ["Çevreyi koru: https://www.youtube.com/watch?v=-UfvgBtqy2c",
                "Atıkları ayır: https://www.youtube.com/watch?v=AkwCSW_Ryig",
                "Ağaç dik: https://www.youtube.com/watch?v=GULwQKIc8ig"
        ]
    videolar = random.choice(videolar)
    await ctx.send(f"Bu videoyu izleyebilirsin: {videolar}")
                
    
@bot.command()
async def cevre_gorevi(ctx):
    gorevler = [ "Bir çöp poşeti al ve çöpleri topla.",
                "Bir ağaç dik!",
                "Portakal kabuklarını çöpe atma peteğe koy ve mis gibi kokunun tadını çıkar!",
                "Atıkları işlevlerine göre ayır."
    
   ] 
    gorev = random.choice(gorevler)
    await ctx.send(f"Çevre görevin: {gorev}")


bot.run("TOKEN")
