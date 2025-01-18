meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL": "bir şakaya karşılık cevap",
            "SHEESH": "onaylamamak"  
            }

word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
   print [meme_dict(word)]
else:
    print("Kelime sözlükte bulunmamaktadır,yardımcı olamadığımız için üzgünüz.")
