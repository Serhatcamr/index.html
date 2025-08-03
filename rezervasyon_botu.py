import json
import datetime
import os

class RezervasyhoneBot:
    def __init__(self):
        self.rezervasyonlar = []
        self.rezervasyon_dosyasi = 'rezervasyonlar.json'
        self.menü = {
            'ana_yemekler': {
                'A1': 'Adana Kebap - 85 TL',
                'A2': 'Karışık Izgara - 95 TL', 
                'A3': 'Köfte - 65 TL',
                'A4': 'Tavuk Şiş - 70 TL'
            },
            'başlangıçlar': {
                'B1': 'Çorba - 25 TL',
                'B2': 'Salata - 30 TL',
                'B3': 'Meze Tabağı - 45 TL'
            },
            'içecekler': {
                'C1': 'Ayran - 10 TL',
                'C2': 'Kola - 15 TL',
                'C3': 'Çay - 8 TL',
                'C4': 'Türk Kahvesi - 20 TL'
            }
        }
        
        self.saatler = {
            '1': '18:00-19:00',
            '2': '19:00-20:00', 
            '3': '20:00-21:00',
            '4': '21:00-22:00',
            '5': '22:00-23:00'
        }
        
        self.masalar = {
            '1': 'Pencere Kenarı (2 kişilik)',
            '2': 'Bahçe (4 kişilik)',
            '3': 'VIP Bölüm (6 kişilik)',
            '4': 'Aile Masası (8 kişilik)'
        }
        
        self.rezervasyonlari_yukle()

    def rezervasyonlari_yukle(self):
        """Kayıtlı rezervasyonları yükle"""
        try:
            if os.path.exists(self.rezervasyon_dosyasi):
                with open(self.rezervasyon_dosyasi, 'r', encoding='utf-8') as f:
                    self.rezervasyonlar = json.load(f)
        except:
            self.rezervasyonlar = []

    def rezervasyonlari_kaydet(self):
        """Rezervasyonları dosyaya kaydet"""
        with open(self.rezervasyon_dosyasi, 'w', encoding='utf-8') as f:
            json.dump(self.rezervasyonlar, f, ensure_ascii=False, indent=2)

    def ana_menu_goster(self):
        """Ana menüyü göster"""
        print("\n🍽️  AIDA RESTORAN REZERVASYON BOTU")
        print("=" * 50)
        print("Merhaba! Size nasıl yardımcı olabilirim?")
        print("\n📋 MENÜ:")
        print("1️⃣  Yeni Rezervasyon Yap")
        print("2️⃣  Mevcut Rezervasyonları Görüntüle")
        print("3️⃣  Yemek Menüsünü İncele")
        print("4️⃣  Restoran Bilgileri")
        print("5️⃣  Rezervasyon İptal Et")
        print("0️⃣  Çıkış")
        
        return input("\n👆 Seçiminizi yapın (0-5): ")

    def rezervasyon_yap(self):
        """Yeni rezervasyon oluştur"""
        print("\n🎯 YENİ REZERVASYON")
        print("=" * 30)
        
        # İsim al
        isim = input("👤 İsminiz: ").strip()
        if not isim:
            print("❌ İsim boş olamaz!")
            return
        
        # Telefon al
        telefon = input("📱 Telefon numaranız: ").strip()
        if not telefon:
            print("❌ Telefon numarası gerekli!")
            return
        
        # Kişi sayısı
        print("\n👥 KAÇ KİŞİLİK REZERVASYON?")
        print("1️⃣  1-2 kişi")
        print("2️⃣  3-4 kişi")
        print("3️⃣  5-6 kişi")
        print("4️⃣  7+ kişi")
        
        kisi_secim = input("Seçim: ")
        kisi_sayilari = {'1': '1-2', '2': '3-4', '3': '5-6', '4': '7+'}
        
        if kisi_secim not in kisi_sayilari:
            print("❌ Geçersiz seçim!")
            return
        
        kisi_sayisi = kisi_sayilari[kisi_secim]
        
        # Tarih al
        print(f"\n📅 HANGİ TARİH? (Bugün: {datetime.date.today()})")
        tarih = input("Tarih (GG.AA.YYYY): ").strip()
        
        # Saat seç
        print("\n🕐 SAAT SEÇİNİZ:")
        for kod, saat in self.saatler.items():
            print(f"{kod}️⃣  {saat}")
        
        saat_secim = input("Seçim: ")
        if saat_secim not in self.saatler:
            print("❌ Geçersiz saat seçimi!")
            return
        
        saat = self.saatler[saat_secim]
        
        # Masa seç
        print("\n🪑 MASA TERCİHİ:")
        for kod, masa in self.masalar.items():
            print(f"{kod}️⃣  {masa}")
        
        masa_secim = input("Seçim: ")
        if masa_secim not in self.masalar:
            print("❌ Geçersiz masa seçimi!")
            return
        
        masa = self.masalar[masa_secim]
        
        # Özel istek
        ozel_istek = input("\n💭 Özel isteğiniz (opsiyonel): ").strip()
        
        # Rezervasyon oluştur
        rezervasyon = {
            'id': len(self.rezervasyonlar) + 1,
            'isim': isim,
            'telefon': telefon,
            'kisi_sayisi': kisi_sayisi,
            'tarih': tarih,
            'saat': saat,
            'masa': masa,
            'ozel_istek': ozel_istek,
            'durum': 'Aktif',
            'olusturma_tarihi': datetime.datetime.now().isoformat()
        }
        
        self.rezervasyonlar.append(rezervasyon)
        self.rezervasyonlari_kaydet()
        
        # Onay göster
        print("\n✅ REZERVASYON BAŞARILI!")
        print("=" * 30)
        print(f"🆔 Rezervasyon No: {rezervasyon['id']}")
        print(f"👤 İsim: {isim}")
        print(f"📅 Tarih: {tarih}")
        print(f"🕐 Saat: {saat}")
        print(f"👥 Kişi: {kisi_sayisi}")
        print(f"🪑 Masa: {masa}")
        if ozel_istek:
            print(f"💭 Özel İstek: {ozel_istek}")
        
        print("\n📱 Rezervasyon numaranızı not alın!")
        input("\nDevam etmek için Enter'a basın...")

    def rezervasyonlari_listele(self):
        """Mevcut rezervasyonları göster"""
        if not self.rezervasyonlar:
            print("\n📝 Henüz rezervasyon bulunmuyor!")
            input("Devam etmek için Enter'a basın...")
            return
        
        print("\n📋 MEVCUT REZERVASYONLAR")
        print("=" * 50)
        
        for rez in self.rezervasyonlar:
            if rez['durum'] == 'Aktif':
                print(f"\n🆔 #{rez['id']} - {rez['isim']}")
                print(f"   📅 {rez['tarih']} | 🕐 {rez['saat']}")
                print(f"   👥 {rez['kisi_sayisi']} kişi | 🪑 {rez['masa']}")
                if rez['ozel_istek']:
                    print(f"   💭 {rez['ozel_istek']}")
        
        input("\nDevam etmek için Enter'a basın...")

    def menu_goster(self):
        """Yemek menüsünü göster"""
        print("\n🍽️  YEMEK MENÜMÜZ")
        print("=" * 40)
        
        for kategori, yemekler in self.menü.items():
            print(f"\n📋 {kategori.upper()}:")
            for kod, yemek in yemekler.items():
                print(f"   {kod} - {yemek}")
        
        print("\n💡 Rezervasyon sırasında sipariş verebilirsiniz!")
        input("Devam etmek için Enter'a basın...")

    def restoran_bilgileri(self):
        """Restoran hakkında bilgi"""
        print("\n🏪 AIDA RESTORAN")
        print("=" * 30)
        print("📍 Adres: Atatürk Cad. No:123 Nilüfer/BURSA")
        print("📱 Telefon: 0224 123 45 67")
        print("🕐 Çalışma Saatleri: 18:00 - 24:00")
        print("🅿️  Ücretsiz Vale Hizmeti")
        print("🎵 Canlı Müzik (Cuma-Cumartesi)")
        print("💳 Tüm Kartlar Geçerli")
        
        input("\nDevam etmek için Enter'a basın...")

    def rezervasyon_iptal(self):
        """Rezervasyon iptal et"""
        if not self.rezervasyonlar:
            print("\n❌ İptal edilecek rezervasyon yok!")
            input("Devam etmek için Enter'a basın...")
            return
        
        print("\n🗑️  REZERVASYON İPTAL")
        print("=" * 30)
        
        # Aktif rezervasyonları göster
        aktif_rezervasyonlar = [r for r in self.rezervasyonlar if r['durum'] == 'Aktif']
        
        if not aktif_rezervasyonlar:
            print("❌ İptal edilecek aktif rezervasyon yok!")
            input("Devam etmek için Enter'a basın...")
            return
        
        for rez in aktif_rezervasyonlar:
            print(f"🆔 {rez['id']} - {rez['isim']} ({rez['tarih']} {rez['saat']})")
        
        try:
            iptal_id = int(input("\nİptal edilecek rezervasyon ID: "))
            
            for rez in self.rezervasyonlar:
                if rez['id'] == iptal_id and rez['durum'] == 'Aktif':
                    rez['durum'] = 'İptal'
                    rez['iptal_tarihi'] = datetime.datetime.now().isoformat()
                    self.rezervasyonlari_kaydet()
                    print(f"✅ #{iptal_id} numaralı rezervasyon iptal edildi!")
                    input("Devam etmek için Enter'a basın...")
                    return
            
            print("❌ Geçersiz rezervasyon ID!")
        except ValueError:
            print("❌ Geçerli bir numara girin!")
        
        input("Devam etmek için Enter'a basın...")

    def botu_calistir(self):
        """Ana bot döngüsü"""
        while True:
            secim = self.ana_menu_goster()
            
            if secim == '1':
                self.rezervasyon_yap()
            elif secim == '2':
                self.rezervasyonlari_listele()
            elif secim == '3':
                self.menu_goster()
            elif secim == '4':
                self.restoran_bilgileri()
            elif secim == '5':
                self.rezervasyon_iptal()
            elif secim == '0':
                print("\n👋 Teşekkürler! AIDA Restoran'ı tercih ettiğiniz için...")
                print("🍽️  Lezzetli yemekler için bekleriz!")
                break
            else:
                print("\n❌ Geçersiz seçim! Lütfen 0-5 arası bir numara girin.")
                input("Devam etmek için Enter'a basın...")

# Botu çalıştır
if __name__ == "__main__":
    bot = RezervasyhoneBot()
    bot.botu_calistir()