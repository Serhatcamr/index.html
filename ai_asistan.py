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
        sehir_patt