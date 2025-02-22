import discord
from discord.ext import commands
import random
import requests
import os

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix="*", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
    
@bot.command()
async def joined(ctx, member: discord.Member = None):
    """Says when a member joined."""
    if member is None:
        await ctx.send('Lütfen bir kullancı etiketleyin.')
    else:  
        await ctx.send(f'{member.name} sunucuya şu tarihte katıldı: {discord.utils.format_dt(member.joined_at)}')   
    
@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))  
    
@bot.command()
async def repeat(ctx, times: int, *, content='repeating...'):
    """Repeats a message multiple times."""
    for _ in range(times):
        await ctx.send(content)
         
@bot.command()
async def rastegele_mem(ctx):
    try:
        # 'images' klasöründeki tüm dosyaların listesini alıyoruz.
        files = os.listdir('images')
        if not files:# Eğer klasör boşsa kullanıcıya bilgi veriyoruz.
            await ctx.send("Resim klasörü boş!")
            return
        # Rastgele bir dosya seçiyoruz.
        miim = random.choice(files)
        # Dosyayı açıp kullanıcıya gönderiyoruz.
        with open(f'images/{miim}', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    except FileNotFoundError:
        await ctx.send("Resim klasörü bulunamadı! Lütfen 'images' klasörünün mevcut olduğundan emin olun.")
    except Exception as e:
        await ctx.send(f"Bir hata oluştu: {e}")   

@bot.command()
async def mem(ctx):
    files = os.listdir('images')
    if not files:
        await ctx.send("Resim klasörü boş!")
        return
    miim = random.choice(files)
    await ctx.send(file=discord.File(f'images/{miim}'))
    
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    return res.json().get('url', "Bir hata oluştu, tekrar deneyin!")

@bot.command()
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    await ctx.send(get_duck_image_url())
     
bot.run("TOKEN")
