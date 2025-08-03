# Kullanıcıdan bilgi alalım
print("=== KİŞİSEL BİLGİ TOPLAYICI ===")

isim = input("Adınız nedir? ")
yas = input("Kaç yaşındasınız? ")
hedef = input("1 yıl sonra ne olmak istiyorsunuz? ")

print("\n--- ÖZET ---")
print(f"Merhaba {isim}!")
print(f"Sen {yas} yaşındasın")
print(f"Hedefin: {hedef}")
print(f"Harika! {hedef} olmak için çok çalışacaksın!")

# Yaşını sayıya çevir ve hesaplama yap
yas_sayi = int(yas)
gelecek_yas = yas_sayi + 1
print(f"1 yıl sonra {gelecek_yas} yaşında {hedef} olacaksın! 🚀")