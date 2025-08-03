import datetime
import json

def tarih_al():
    """Bugünün tarihini güzel formatta döndür"""
    bugun = datetime.datetime.now()
    return bugun.strftime("%d/%m/%Y")

def gorevleri_yukle():
    """Kayıtlı görevleri dosyadan yükle"""
    try:
        with open('gorevler.json', 'r', encoding='utf-8') as file:
            content = file.read().strip()
            if not content:  # Dosya boşsa
                return []
            return json.loads(content)
    except (FileNotFoundError, json.JSONDecodeError):
        print("🔄 Yeni görev listesi oluşturuluyor...")
        return []

def gorevleri_kaydet(gorevler):
    """Görevleri dosyaya kaydet"""
    with open('gorevler.json', 'w', encoding='utf-8') as file:
        json.dump(gorevler, file, ensure_ascii=False, indent=2)

def gorev_ekle(gorevler):
    """Yeni görev ekle"""
    print("\n➕ YENİ GÖREV EKLE")
    baslik = input("Görev başlığı: ")
    aciklama = input("Açıklama (opsiyonel): ")
    
    gorev = {
        'id': len(gorevler) + 1,
        'baslik': baslik,
        'aciklama': aciklama,
        'tarih': tarih_al(),
        'tamamlandi': False
    }
    
    gorevler.append(gorev)
    print(f"✅ '{baslik}' görevi eklendi!")

def gorevleri_listele(gorevler):
    """Tüm görevleri listele"""
    if not gorevler:
        print("\n📝 Henüz görev yok!")
        return
    
    print(f"\n📋 GÖREV LİSTESİ ({tarih_al()})")
    print("=" * 50)
    
    for gorev in gorevler:
        durum = "✅" if gorev['tamamlandi'] else "⏳"
        print(f"{durum} {gorev['id']}. {gorev['baslik']}")
        if gorev['aciklama']:
            print(f"   💭 {gorev['aciklama']}")
        print(f"   📅 {gorev['tarih']}")
        print()

def gorev_tamamla(gorevler):
    """Görevi tamamlanmış olarak işaretle"""
    gorevleri_listele(gorevler)
    
    try:
        gorev_id = int(input("\nTamamlanan görev ID'si: "))
        
        for gorev in gorevler:
            if gorev['id'] == gorev_id:
                gorev['tamamlandi'] = True
                print(f"🎉 '{gorev['baslik']}' tamamlandı!")
                return
        
        print("❌ Görev bulunamadı!")
    except ValueError:
        print("❌ Geçerli bir ID girin!")

# Ana program
def main():
    print("🎯 GÖREV YÖNETİCİSİ")
    print("=" * 30)
    
    gorevler = gorevleri_yukle()
    
    while True:
        print(f"\n📅 Bugün: {tarih_al()}")
        print("\nNe yapmak istiyorsun?")
        print("1. Görevleri listele")
        print("2. Yeni görev ekle") 
        print("3. Görev tamamla")
        print("4. Çıkış")
        
        secim = input("\nSeçiminiz (1-4): ")
        
        if secim == '1':
            gorevleri_listele(gorevler)
        elif secim == '2':
            gorev_ekle(gorevler)
            gorevleri_kaydet(gorevler)
        elif secim == '3':
            gorev_tamamla(gorevler)
            gorevleri_kaydet(gorevler)
        elif secim == '4':
            print("👋 Görüşürüz!")
            break
        else:
            print("❌ Geçersiz seçim!")

if __name__ == "__main__":
    main()