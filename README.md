TRAFIK CEZASI DOGRULAMA VE ITIRAZ ASISTANI - VIZE PROJE RAPORU

1. Analiz Raporu (Giris ve Amac)
Suruculere yazilan trafik cezalarinin gecmis surus verileriyle ve konum bilgileriyle uyumlu olup olmadigini kontrol eden, hatali veya supheli durumlarda ise Buyuk Dil Modeli (LLM) destegiyle otomatik itiraz dilekcesi taslagi olusturan bir karar destek sistemidir.

2. Sistem Gereksinimleri
* Surucu, ceza bilgilerini (tarih, saat, konum, ceza maddesi) sisteme girebilmelidir.
* Istatistiki model (Lojistik Regresyon / Karar Agaclari), cezanin tutarsizlik oranini hesaplayarak "Supha Skoru" uretmelidir.
* Suphe skoru yuksek olan cezalar icin LLM katmani otomatik dilekce taslagi cikarmalidir.

3. Fonksiyonel Gereksinimler
* FR-01: Kullanici ceza detaylarini sisteme kaydeder.
* FR-02: Sistem, konum ve zaman uyumsuzluguna gore ceza icin %0-%100 arasi anomali skoru hesaplar.
* FR-03: Suphe skoru %70'i gecen cezalar icin LLM ilgili kanun maddesine gore itiraz metni uretir.

4. Kullanim Senaryosu (Use Case)
* Aktor: Surucu (Kullanici)
* Senaryo: Surucu hatali oldugunu dusundugu cezayi sisteme girer -> Sistem gecmis verilerle karsilastirip suphe skoru uretir -> Skor yuksekse LLM itiraz dilekcesi hazirlar -> Sonuc ekranda gosterilir.

5. Test Senaryolari (Test Cases)
* TC-01 (Normal Ceza): Dogru kesilen ceza girilir -> Suphe skoru dusuk cikar, LLM calismaz.
* TC-02 (Supheli Ceza): Konumla uyusmayan ceza girilir -> Suphe skoru yuksek cikar, LLM dilekce uretir.
