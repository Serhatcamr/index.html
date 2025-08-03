import random
import datetime
import json
import re
import os

class AkilliAIDA:
    def __init__(self):
        self.isim = "AIDA"
        self.konusma_gecmisi = []
        self.kullanici_bilgisi = {}
        self.ogrenilen_bilgiler = {}
        
        # Bilgileri dosyadan yükle
        self.bilgileri_yukle()
        
        # Cevap şablonları
        self.cevap_sablonlari = {
            'selamla': [
                "Merhaba {isim}! Seni görmek güzel! 😊",
                "Selam {isim}! Bugün nasılsın?",
                "Hey {isim}! Sana nasıl yardım edebilirim?"
            ],
            'ogrenme_onay': [
                "Anladım! Bunu öğrendim ve hatırlayacağım! 📚",
                "Teşekkürler, bu bilgiyi kaydettim! 🧠",
                "Bu bilgiyi not aldım, unutmayacağım! ✍️"
            ]
        }

    def bilgileri_yukle(self):
        """Önceki öğrenilmiş bilgileri yükle"""
        try:
            if os.path.exists('aida_hafiza.json'):
                with open('aida_hafiza.json', 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.kullanici_bilgisi = data.get('kullanici_bilgisi', {})
                    self.ogrenilen_bilgiler = data.get('ogrenilen_bilgiler', {})
                    print("🧠 Önceki bilgilerimi hatırladım!")
        except:
            print("🆕 Yeni bir hafıza oluşturuyorum!")

    def bilgileri_kaydet(self):
        """Öğrenilen bilgileri dosyaya kaydet"""
        data = {
            'kullanici_bilgisi': self.kullanici_bilgisi,
            'ogrenilen_bilgiler': self.ogrenilen_bilgiler,
            'son_guncelleme': datetime.datetime.now().isoformat()
        }
        with open('aida_hafiza.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def bilgi_cikar(self, mesaj):
        """Mesajdan öğrenilebilir bilgi çıkar"""
        mesaj_lower = mesaj.lower()
        
        # İsim öğrenme
        isim_patterns = [
            r'(?:ben|benim adım|ismim)\s+(\w+)',
            r'adım\s+(\w+)',
            r'ben\s+(\w+)(?:\s|$)'
        ]
        
        for pattern in isim_patterns:
            match = re.search(pattern, mesaj_lower)
            if match:
                isim = match.group(1).title()
                self.kullanici_bilgisi['isim'] = isim
                return f"ismini_{isim}"

        # Meslek/hobi bilgisi
        if any(kelime in mesaj_lower for kelime in ['çalışıyorum', 'iş', 'meslek', 'job']):
            if 'meslek' not in self.ogrenilen_bilgiler:
                # Meslek çıkarma
                meslek_patterns = [
                    r'(\w+)\s+olarak\s+çalışıyorum',
                    r'ben\s+(\w+)(?:yım|im)',
                    r'mesleğim\s+(\w+)'
                ]
                for pattern in meslek_patterns:
                    match = re.search(pattern, mesaj_lower)
                    if match:
                        meslek = match.group(1)
                        self.ogrenilen_bilgiler['meslek'] = meslek
                        return f"meslek_{meslek}"

        # Hobi/ilgi alanları
        hobi_kelimeler = ['seviyorum', 'hobi', 'ilgileniyorum', 'yapıyorum', 'oynuyorum']
        if any(kelime in mesaj_lower for kelime in hobi_kelimeler):
            hobi_patterns = [
                r'(\w+)\s+seviyorum',
                r'(\w+)\s+oynuyorum',
                r'hobim\s+(\w+)',
                r'(\w+)\s+ile\s+ilgileniyorum'
            ]
            for pattern in hobi_patterns:
                match = re.search(pattern, mesaj_lower)
                if match:
                    hobi = match.group(1)
                    if 'hobiler' not in self.ogrenilen_bilgiler:
                        self.ogrenilen_bilgiler['hobiler'] = []
                    if hobi not in self.ogrenilen_bilgiler['hobiler']:
                        self.ogrenilen_bilgiler['hobiler'].append(hobi)
                        return f"hobi_{hobi}"

        # Yaş bilgisi
        yas_patterns = [
            r'(\d+)\s+yaşındayım',
            r'yaşım\s+(\d+)',
            r'ben\s+(\d+)\s+yaşında'
        ]
        for pattern in yas_patterns:
            match = re.search(pattern, mesaj_lower)
            if match:
                yas = match.group(1)
                self.kullanici_bilgisi['yas'] = yas
                return f"yas_{yas}"

        # Şehir bilgisi
        sehir_patterns = [
            r'(\w+)(?:da|de)\s+yaşıyorum',
            r'(\w+)(?:da|de)\s+oturuyorum',
            r'şehrim\s+(\w+)'
        ]
        for pattern in sehir_patterns:
            match = re.search(pattern, mesaj_lower)
            if match:
                sehir = match.group(1).title()
                self.kullanici_bilgisi['sehir'] = sehir
                return f"sehir_{sehir}"

        # Genel bilgi saklama
        bilgi_ifadeleri = ['öğreniyorum', 'başladım', 'planlıyorum', 'istiyorum', 'hedefliyorum']
        if any(ifade in mesaj_lower for ifade in bilgi_ifadeleri):
            # Zaman damgası ile genel bilgi kaydet
            tarih = datetime.datetime.now().strftime("%d/%m/%Y")
            if 'genel_bilgiler' not in self.ogrenilen_bilgiler:
                self.ogrenilen_bilgiler['genel_bilgiler'] = []
            
            bilgi_kaydı = {
                'tarih': tarih,
                'bilgi': mesaj,
                'anahtar_kelimeler': self.anahtar_kelimeleri_cikar(mesaj)
            }
            self.ogrenilen_bilgiler['genel_bilgiler'].append(bilgi_kaydı)
            return "genel_bilgi"

        return None

    def anahtar_kelimeleri_cikar(self, mesaj):
        """Mesajdan anahtar kelimeleri çıkar"""
        # Yaygın kelimeler hariç anahtar kelimeleri bul
        yaygın_kelimeler = ['ben', 'sen', 'bir', 'bu', 'şu', 've', 'ile', 'için', 'gibi', 'var', 'yok']
        kelimeler = re.findall(r'\w+', mesaj.lower())
        return [k for k in kelimeler if k not in yaygın_kelimeler and len(k) > 2]

    def bilgi_sorgula(self, soru):
        """Öğrenilen bilgileri sorgula"""
        soru_lower = soru.lower()
        
        # İsim sorgusu
        if any(kelime in soru_lower for kelime in ['ismim', 'adım', 'kim']):
            if 'isim' in self.kullanici_bilgisi:
                return f"Senin adın {self.kullanici_bilgisi['isim']}! 😊"
        
        # Yaş sorgusu
        if 'yaş' in soru_lower:
            if 'yas' in self.kullanici_bilgisi:
                return f"Sen {self.kullanici_bilgisi['yas']} yaşındasın!"
        
        # Meslek sorgusu
        if any(kelime in soru_lower for kelime in ['meslek', 'iş', 'çalış']):
            if 'meslek' in self.ogrenilen_bilgiler:
                return f"Sen {self.ogrenilen_bilgiler['meslek']} olarak çalışıyorsun!"
        
        # Hobi sorgusu
        if any(kelime in soru_lower for kelime in ['hobi', 'sev', 'ilgi']):
            if 'hobiler' in self.ogrenilen_bilgiler:
                hobiler = ', '.join(self.ogrenilen_bilgiler['hobiler'])
                return f"Senin hobilerin: {hobiler}! 🎯"
        
        # Şehir sorgusu
        if any(kelime in soru_lower for kelime in ['şehir', 'nerede', 'yaşa']):
            if 'sehir' in self.kullanici_bilgisi:
                return f"Sen {self.kullanici_bilgisi['sehir']}'da yaşıyorsun!"
        
        # Genel bilgi arama
        if 'genel_bilgiler' in self.ogrenilen_bilgiler:
            for bilgi in self.ogrenilen_bilgiler['genel_bilgiler']:
                if any(kelime in soru_lower for kelime in bilgi['anahtar_kelimeler']):
                    return f"Hatırladığım: {bilgi['bilgi']} ({bilgi['tarih']})"
        
        return None

    def cevap_uret(self, mesaj):
        """Mesaja akıllı cevap üret"""
        # Önce bilgi çıkarmayı dene
        bilgi_turu = self.bilgi_cikar(mesaj)
        
        if bilgi_turu:
            cevap = random.choice(self.cevap_sablonlari['ogrenme_onay'])
            self.bilgileri_kaydet()  # Yeni bilgiyi kaydet
            return cevap
        
        # Sonra bilgi sorgusu kontrol et
        bilgi_cevabi = self.bilgi_sorgula(mesaj)
        if bilgi_cevabi:
            return bilgi_cevabi
        
        # Selamlama
        if any(kelime in mesaj.lower() for kelime in ['merhaba', 'selam', 'hey']):
            isim = self.kullanici_bilgisi.get('isim', 'arkadaşım')
            return f"Merhaba {isim}! Nasılsın? 😊"
        
        # Varsayılan cevap
        return "Anladım! Bu konuda konuşmaya devam edebiliriz. Başka ne söylemek istersin? 💭"

    def sohbet_basla(self):
        """Ana sohbet döngüsü"""
        print("🧠 AKILLI AIDA - Öğrenen AI Asistan")
        print("=" * 45)
        
        if 'isim' in self.kullanici_bilgisi:
            print(f"Tekrar merhaba {self.kullanici_bilgisi['isim']}! 😊")
        else:
            print("Merhaba! Ben AIDA, senden öğrenmeyi seven AI asistanınım!")
        
        print("'çıkış' yazarak ayrılabilirsin.\n")
        
        while True:
            kullanici_mesaj = input("Sen: ")
            
            if kullanici_mesaj.lower() in ['çıkış', 'exit', 'quit']:
                isim = self.kullanici_bilgisi.get('isim', 'arkadaşım')
                print(f"🤖 AIDA: Görüşürüz {isim}! Öğrendiklerimi unutmayacağım! 🧠✨")
                break
            
            cevap = self.cevap_uret(kullanici_mesaj)
            print(f"🤖 AIDA: {cevap}\n")

# Programı çalıştır
if __name__ == "__main__":
    aida = AkilliAIDA()
    aida.sohbet_basla()