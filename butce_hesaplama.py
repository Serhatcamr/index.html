def para_formatla(sayi):
    """Sayıyı Türk para formatına çevir: 15000 -> 15.000,00"""
    return f"{sayi:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def para_input(mesaj):
    """Kullanıcıdan para girişi al ve formatla"""
    while True:
        print(f"\n{mesaj}")
        print("💡 Sadece rakam (örnek: 15000)")
        
        giris = input("➤ ")
        
        if giris.isdigit():
            sayi = int(giris)
            formatli = para_formatla(sayi)
            print(f"   📱 {formatli} TL")
            return sayi
        else:
            print("   ❌ Sadece rakam girin!")

print("📱 GİRİŞİMCİ BÜTÇE UYGULAMASI")
print("=" * 35)

isim = input("👤 Adınız: ")

# Temiz girişler
gelir = para_input("💰 Aylık gelir")
kira = para_input("🏠 Aylık kira")
yemek = para_input("🍽️ Aylık yemek")
diger = para_input("🛒 Diğer giderler")

# Hesaplama
toplam_gider = kira + yemek + diger
kalan = gelir - toplam_gider
yuzde = (kalan / gelir) * 100

# Rapor
print(f"\n📊 {isim.upper()} - FİNANSAL DURUM")
print("=" * 35)
print(f"💰 Gelir      : {para_formatla(gelir)} TL")
print(f"📉 Giderler   : {para_formatla(toplam_gider)} TL")
print(f"✨ KALAN      : {para_formatla(kalan)} TL")
print(f"📈 Tasarruf   : %{yuzde:.1f}")

# Girişimcilik tavsiyesi
if kalan > 15000:
    print(f"\n🚀 {para_formatla(kalan)} TL ile AI girişimi için mükemmel!")
elif kalan > 5000:
    print(f"\n🔥 {para_formatla(kalan)} TL ile güçlü başlangıç!")
else:
    print(f"\n💪 {para_formatla(kalan)} TL ile temkinli başlangıç!")