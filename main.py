# ==========================================
# TRAFİK CEZASI DOĞRULAMA VE İTİRAZ ASİSTANI
# Vize Proje İskeleti (Data Mining & LLM Layer)
# ==========================================

class TrafikCezaAnalizSistemi:
    def __init__(self, surucu_id):
        self.surucu_id = surucu_id

    def anomali_skoru_hesapla(self, ceza_yeri, anlik_konum):
        if ceza_yeri != anlik_konum:
            return 88.5 
        else:
            return 12.0

    def llm_itiraz_dilekcesi_uret(self, ceza_maddesi, suphe_skoru):
        if suphe_skoru > 70.0:
            return "[OTOMATİK LLM İTİRAZ DİLEKÇESİ TASLAĞI OLUŞTURULDU]"
        else:
            return "İtiraz gerek görülmedi."

if __name__ == "__main__":
    asistan = TrafikCezaAnalizSistemi(surucu_id="TR-34-KRM-04")
    skor = asistan.anomali_skoru_hesapla("Kadıköy", "Beylikdüzü")
    print(f"Şüphe Skoru: %{skor}")
