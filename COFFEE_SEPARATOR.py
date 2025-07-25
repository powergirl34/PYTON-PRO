AI.py
import discord
from discord.ext import commands
import os
from model import get_class
from tensorflow.keras.models import load_model


intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

#GÖRSELLER İÇİN KLASÖR OLUŞTURUYORUZ
IMAGE_DIR= "images"
os.makedirs(IMAGE_DIR, exist_ok=True)

model = load_model(r"C:\Users\hp\Desktop\19keras\keras_model.h5", compile=False)
class_names = open("labels.txt", "r").readlines()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_path = os.path.join(IMAGE_DIR, file_name)

            try:
                await attachment.save(file_path)
                await ctx.send(f"Görsel başarıyla kaydoldu: {file_path}") # Mesajı biraz değiştirdim
                class_name, confidence_score = get_class(image_path=file_path)
                await ctx.send(f"Görselin Sınıfı: {class_name}, tahmin skoru: {confidence_score}")

                if class_name == "Cappuccino":
                    await ctx.send("""Cappuccinolar ilk olarak 1700'lerde Viyana kahvehanelerinde 'Kapuziner' olarak ortaya çıktı. 1805'te 'Kapuziner'in tanımı,
                                     "krema ve şekerli kahve" olarak tanımlandı ve 1850'de içeceğin tanımı, tarife "baharatlar" ekledi. Isıtıcın bir bardak su
                                     kaynatın ve seçtiğiniz çözünebilir kahveden 2 tatlı kaşığı bardağa ekleyin. Kahvenize şeker koyuyorsanız, ekleyin ve
                                     lezzetlendirin. Su kaynadı sonra cappuccino bardağınıza ekleyin, yaklaşık 1/3 'ünü doldurun.""")
                elif class_name == "Espresso": # 'if' yerine 'elif' kullanmak daha doğru.
                    await ctx.send("""Espresso, 20. yüzyılın başlarında İtalya'nın Venedik kentinde icat edildi. Espresso için kaynatılmış sıcak suyun yüksek
                                     basınçla son derece ince öğütülmüş toz kahveden geçmesi gerekir. Filtre yerine süzgeç kullanılır. Böylece kahve yağının
                                     aromatik lezzetinden hiçbir şey kaybolmaz. Sonuç olarak sert ve yoğun bir lezzet içeren kahve elde edilir.""")
                elif class_name == "icelatte": # 'if' yerine 'elif' kullanmak daha doğru.
                    await ctx.send("""Soğuk kahve, geleneksel sıcak kahve demleme yöntemlerinden farklı olarak, kahve çekirdeklerinin soğuk suyla uzun süre
                                     bekletilerek veya soğuk su üzerinden geçirilerek hazırlanan bir içecektir. Bu yöntemlerin kökeni, özellikle 17.yüzyılda
                                     Ortadoğu ve Doğu Akdeniz’de, örneğin Türkiye ve Yunanistan gibi ülkelerde görülmüştür. Ancak soğuk demleme yöntemleri
                                     günümüzde daha yaygın olarak benimsenmiştir. Ice latte nasıl yapılır? Önce espresso hazırlanır, ardından bardağa buz
                                     konulur. Üzerine soğuk süt dökülür ve en son sıcak espresso eklenir. Tatlandırıcı istenirse eklenip karıştırılabilir.""")
                elif class_name == "Salep": # 'if' yerine 'elif' kullanmak daha doğru.
                    await ctx.send("""8. yüzyıl Türkler'in İslamiyet'i kabul ettiği dönemlere denk gelir. O dönemlerde alkollü içeceklerin yasaklanması salebe
                                     olan talebin artmasını sağlamış ve hatta "salep dükkanları" bile açılmış. Tarihi tıp filozofu İbni Sina "Kanun" adlı
                                     eserinde salebe dair detaylı bilgilere yer verir. Salep bitkisinin toprak altındaki yumruları toplanır. Sonra haşlanarak
                                     gölgede kurutulur ve öğütülerek toz haline getirilir. Daha sonra isteğe göre tarçınla harmanlanarak sütle birlikte uzun
                                     süre kaynatılır ve hazır hale getirilmiş olur. Su ve süt eklendiğinde şişmesi özelliği ile dondurma yapımında kullanılmaktadır.""")
                elif class_name == "TURKKAHVESİ": # 'if' yerine 'elif' kullanmak daha doğru.
                    await ctx.send("""Türk kahvesi, 16. yüzyıldan itibaren Osmanlı İmparatorluğu'nda yaygınlaşmaya başlamış ve zamanla tüm dünyaya ün salmıştır.
                                     Kahve, ilk olarak Yemen’den İstanbul’a getirilmiş ve kısa sürede halk arasında popüler hâle gelmiştir. Saraylarda ve halk
                                     kahvehanelerinde içilen bu içecek, sohbetlerin ve dostlukların pekiştirildiği anların vazgeçilmezi olmuştur. Peki nasıl yapılır??
                                     Sade Türk kahvesi, kahvenin saf lezzetini deneyimlemek isteyenler için idealdir. Köpüklü sade Türk kahvesi hazırlarken cezveye
                                     bir fincan soğuk su ve iki çay kaşığı Türk kahvesi eklenir. Şeker eklenmeden kahve iyice karıştırılır. Ardından cezve kısık ateşte
                                     yavaşça pişirilir. Kahve kaynamaya başladığında, oluşan köpük fincana alınır. Kalan kahve tekrar kaynatılıp fincana dökülür. Sade
                                     Türk kahvesi, yoğun aroması ve yumuşak içimi ile kahve severlerin vazgeçilmezidir. Özellikle kahvenin doğal tadını hissetmek isteyenler
                                     için sade tercih edilen bir lezzettir.""")
                else:
                    await ctx.send("""Bilinmeyen bir içecek, yardımcı olamadığımız için özür dileriz :(""")
            except Exception as e:
                await ctx.send(f"Görsel kaydedilemedi: {file_path}. Hata: {e}")
    else:
        await ctx.send("Lütfen bir görsel ekleyin")

                          
bot.run("TOKEN")

model.py 
from tensorflow.keras.models import load_model # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)
def get_class(image_path,model_path="keras_model.h5", lebels_path="labels.txt"):
    
    model = load_model(model_path, compile=False)
    class_names = open(labels_path, "r").readlines()
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = Image.open(image_path).convert("RGB")
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data[0] = normalized_image_array
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    return class_name[2:].strip() , confidence_score
