# Akıllı karar verici program
print("=== AI GİRİŞİMCİ DANIŞMANI ===")

isim = input("Adın nedir? ")
deneyim = input("Programlama deneyimin var mı? (evet/hayır): ")
calisma_saati = input("Günde kaç saat çalışabilirsin? ")

print(f"\nMerhaba {isim}! Seni analiz ediyorum...")

# Karar verme zamanı
if deneyim.lower() == "evet":
    print("✅ Harika! Deneyimin var, daha hızlı ilerleyebilirsin!")
    oneri = "Direkt AI projelerine başlayabilirsin"
else:
    print("✅ Sorun değil! Herkes sıfırdan başlar")
    oneri = "Python temellerinden başlamalısın"

# Çalışma saatine göre öneri
saat = int(calisma_saati)
if saat >= 3:
    tempo = "Çok hızlı ilerleme yapacaksın! 🚀"
elif saat >= 2:
    tempo = "İyi bir tempoda ilerleyeceksin! 👍"
else:
    tempo = "Yavaş ama emin adımlarla ilerleyeceksin! 🐢"

print(f"\n--- SENİN İÇİN ÖNERİLER ---")
print(f"📋 Başlangıç planı: {oneri}")
print(f"⏰ Tempo tahmini: {tempo}")
print(f"🎯 Sen {saat} saat/gün ile başarılı olacaksın!")

if saat >= 2:
    print("💡 İpucu: Bu tempoda 3 ayda freelance işler alabilirsin!")