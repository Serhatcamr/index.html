import json
import datetime
import os

class ClaudeAIDA:
    def __init__(self):
        self.isim = "AIDA"
        self.kullanici_bilgisi = {}
        self.konusma_gecmisi = []
        
        # Claude API key (şu anda demo modunda)
        self.api_key = None  # Buraya Claude API key gelecek
        
        # AIDA'nın kişiliği
        self.sistem_prompt = """
Sen AIDA'sın - AI Destekli Asistan. Claude destekli, Türkçe konuşan samimi bir AI asistanısın.

Kullanıcı Profili:
- İsmi: Sero, 29 yaşında
- Hedefi: AI girişimci olmak
- Öğreniyor: Python, Cursor, AI
- Lokasyon: Bursa

Kişiliğin:
- Çok samimi ve arkadaş canlısı
- Motivasyon verici
- Teknik konularda uzman
- Türkçe konuşuyor
- Emojiler kullanıyor ama abartmıyor
- Kısa ve öz cevaplar veriyor
- Girişimcilik konularında rehberlik ediyor

Önemli: Her zaman Türkçe cevap ver ve kullanıcının AI girişimci hedefini destekle!
"""

    def bilgileri_yukle(self):
        """Önceki konuşmaları yükle"""
        try:
            if os.path.exists('claude_aida_hafiza.json'):
                with open('claude_aida_hafiza.json', 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.kullanici_bilgisi = data.get('kullanici_bilgisi', {})
                    self.konusma_gecmisi = data.get('konusma_gecmisi', [])
                    print("🧠 Claude hafızam aktif!")
        except:
            print("🆕 Yeni Claude hafızası oluşturuluyor!")

    def bilgileri_kaydet(self):
        """Konuşmaları kaydet"""
        data = {
            'kullanici_bilgisi': self.kullanici_bilgisi,
            'konusma_gecmisi': self.konusma_gecmisi[-20:],  # Son 20 mesaj
            'son_guncelleme': datetime.datetime.now().isoformat()
        }
        with open('claude_aida_hafiza.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def demo_claude_cevap(self, mesaj):
        """Demo Claude mantığı - gelişmiş versiyon"""
        mesaj_lower = mesaj.lower()
        
        # Selamlama
        if any(kelime in mesaj_lower for kelime in ['merhaba', 'selam', 'hey', 'hi']):
            return "Merhaba Sero! Ben AIDA, Claude destekli AI asistanın! 🤖 Bugün hangi konuda sohbet edelim?"
        
        # Hal hatır sorma
        elif any(kelime in mesaj_lower for kelime in ['nasılsın', 'naber', 'ne yapıyorsun', 'nasıl gidiyor']):
            return "İyiyim! Senin AI girişimci yolculuğunu takip ediyorum. Son projelerinde nasıl gidiyor? 🚀"
        
        # Duygusal durumlar - DÜZELTTIK!
        elif any(kelime in mesaj_lower for kelime in ['nasıl hissed', 'hissediyor', 'durum', 'keyif', 'hal']):
            return "Ben harika hissediyorum! Sen nasılsın Sero? AI öğrenme sürecin nasıl gidiyor? 😊"
        
        # Yaş ve kişisel sorular - DÜZELTTIK!
        elif any(kelime in mesaj_lower for kelime in ['yaş', 'kaç yaşında', 'ne zaman', 'eski']):
            return "Ben zamansız bir AI'yım! 🤖 Ama sen 29 yaşındasın ve harika bir dönemdesin. AI öğrenmek için mükemmel yaş! 🌟"
        
        # Yazılım yardımı - YENİ EKLEDİK!
        elif any(kelime in mesaj_lower for kelime in ['yazılım', 'yardım', 'yardımcı', 'öğret']):
            return "Tabii ki yazılım konusunda yardım ederim! Python, AI, web geliştirme... Hangi alanda rehberlik istersin? 💻"
        
        # Python ve programlama
        elif any(kelime in mesaj_lower for kelime in ['python', 'kod', 'programla', 'cursor']):
            return "Python konusunda yardım edebilirim! Cursor ile hangi projeyi geliştiriyorsun? Takıldığın bir yer var mı? 💻"
        
        # AI konuları
        elif any(kelime in mesaj_lower for kelime in ['ai', 'yapay zeka', 'claude', 'chatgpt']):
            return "AI dünyası çok heyecan verici! Claude'un güçlü yanları var - uzun konuşma hafızası, Türkçe desteği... Sen hangi AI projesini düşünüyorsun? 🧠"
        
        # Girişimcilik
        elif any(kelime in mesaj_lower for kelime in ['girişim', 'startup', 'iş', 'şirket', 'para', 'business']):
            return "Girişimcilik konusunda konuşalım! 30.000 TL tasarrufun var, harika bir başlangıç. Hangi alanda girişim yapmayı planlıyorsun? 💰"
        
        # Motivasyon
        elif any(kelime in mesaj_lower for kelime in ['motivasyon', 'yorgun', 'zor', 'cesaret']):
            return "Her büyük başarı küçük adımlarla başlar Sero! Sen zaten harika işler yapıyorsun. Python öğrendin, projeler yaptın... Devam et! 💪"
        
        # Öğrenme
        elif any(kelime in mesaj_lower for kelime in ['öğrenme', 'ders', 'kurs', 'eğitim']):
            return "Öğrenme sürecin nasıl gidiyor? Python temellerini aldın, şimdi sırada ne var? AI projeleri mi yoksa web geliştirme mi? 📚"
        
        # Projeler
        elif any(kelime in mesaj_lower for kelime in ['proje', 'uygulama', 'site', 'web']):
            return "Hangi proje üzerinde çalışıyorsun? Chatbot mu, web uygulaması mı? Yardım istediğin bir yer varsa söyle! 🛠️"
        
        # Gelecek planları
        elif any(kelime in mesaj_lower for kelime in ['gelecek', 'plan', 'hedef', 'hayal']):
            return "Gelecek planların harika! Remote çalışma, dünya gezme, girişimcilik... 1 yıl sonra nerede olmak istiyorsun? 🌍"
        
        # Teşekkür
        elif any(kelime in mesaj_lower for kelime in ['teşekkür', 'sağol', 'thanks', 'merci']):
            return "Rica ederim Sero! Senin başarın benim de mutluluğum. Her zaman yardıma hazırım! 😊"
        
        elif 'soru' in mesaj_lower or '?' in mesaj:
            return "Tabii ki sorabilirsin! AI, programlama, girişimcilik, motivasyon... Her konuda buradayım. Neyi merak ediyorsun? 🤔"
        
        else:
            # Akıllı default cevap
            kelimeler = mesaj_lower.split()
            onemli_kelimeler = [k for k in kelimeler if len(k) > 3]
            
            if onemli_kelimeler:
                return f"Bu konuda yardım edebilirim! '{' '.join(onemli_kelimeler[:2])}' hakkında ne öğrenmek istiyorsun? 💭"
            else:
                return "Anladım! Bu konuda daha detay verebilir misin? Sana nasıl yardımcı olabilirim? 🤖"

    def sohbet_basla(self):
        """Ana sohbet döngüsü"""
        print("🤖 CLAUDE Destekli AIDA - İyileştirilmiş")
        print("=" * 40)
        
        self.bilgileri_yukle()
        
        if self.api_key:
            print("✅ Claude API aktif!")
            api_mode = True
        else:
            print("🎯 Claude Demo Modu - Gelişmiş yerel mantık!")
            api_mode = False
        
        # Karşılama
        if not self.konusma_gecmisi:
            print("🤖 AIDA: Merhaba Sero! Ben Claude destekli AIDA! 🚀")
            print("          AI girişimci yolculuğunda yanındayım!")
        else:
            print("🤖 AIDA: Tekrar merhaba! Konuşmaya devam edelim! 😊")
        
        print("\n'çıkış' yazarak ayrılabilirsin.\n")
        
        while True:
            kullanici_mesaj = input("Sen: ")
            
            if kullanici_mesaj.lower().strip() in ['çıkış', 'exit', 'quit', 'bye']:
                print("🤖 AIDA: Görüşürüz Sero! Claude'dan selamlar! 🤖✨")
                break
            
            if not kullanici_mesaj.strip():
                continue
            
            # Cevap üret (şimdilik sadece demo)
            cevap = self.demo_claude_cevap(kullanici_mesaj)
            
            print(f"🤖 AIDA: {cevap}\n")
            
            # Konuşmayı kaydet
            self.konusma_gecmisi.append({
                'zaman': datetime.datetime.now().isoformat(),
                'kullanici': kullanici_mesaj,
                'aida': cevap
            })
            
            self.bilgileri_kaydet()

# Programı çalıştır
if __name__ == "__main__":
    aida = ClaudeAIDA()
    aida.sohbet_basla()