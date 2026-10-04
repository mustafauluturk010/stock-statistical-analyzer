# Stock Statistical Analyzer

Python öğrenirken geliştirdiğim bir finansal veri analiz projesi.

Projeye basit bir fiyat verisiyle başladım. Zamanla hareketli ortalamalar, AL/SAT sinyalleri, portföy hesaplama, risk analizi ve farklı stratejilerin karşılaştırılması gibi özellikler ekledim.

Şu an proje V1 aşamasında.

## Neler Yapabiliyor?

* Ortalama, medyan, varyans ve standart sapma hesaplama
* Günlük yüzde değişim hesaplama
* Volatilite analizi
* Maximum Drawdown hesaplama
* MA3, MA5 ve MA7 hareketli ortalamaları
* AL / SAT / BEKLE sinyalleri
* Sinyal başarı oranı
* Strateji getirilerinin hesaplanması
* 1000 TL üzerinden portföy simülasyonu
* Al-Tut stratejisi ile karşılaştırma
* Risk ve getiri karşılaştırması
* Sharpe Ratio
* Z-Score analizi
* Aykırı değer analizi
* Shapiro-Wilk testi
* Grafikler
* Strateji puanlama sistemi

## Kullanılanlar

* Python
* Pandas
* Matplotlib
* SciPy

## Proje Yapısı

```text
stock-statistical-analyzer/
│
├── data/
│   └── stock_data.csv
│
├── main.py
├── requirements.txt
└── README.md
```

## V1 Sonuçları

Projede 1000 TL başlangıç sermayesi kullanarak dört farklı yaklaşımı karşılaştırdım.

| Strateji | Son Portföy |  Getiri |
| -------- | ----------: | ------: |
| MA3      |   787.07 TL | -21.29% |
| MA5      |  1140.33 TL | +14.03% |
| MA7      |  1333.33 TL | +33.33% |
| Al-Tut   |  1600.00 TL | +60.00% |

Bu veri setinde en yüksek getiriyi Al-Tut stratejisi verdi.

Kendi oluşturduğum puanlama sisteminde ise **MA7** birinci çıktı.

### Risk sonuçları

| Strateji | Standart Sapma | Maximum Drawdown | Sharpe |
| -------- | -------------: | ---------------: | -----: |
| MA3      |          3.62% |          -30.64% | -0.210 |
| MA5      |          3.30% |          -11.10% |  0.153 |
| MA7      |          2.88% |           -3.08% |  0.360 |
| Al-Tut   |          3.44% |           -3.08% |  0.492 |

## Çalıştırmak

Önce gerekli kütüphaneleri yüklemek için:

```bash
pip install -r requirements.txt
```

Daha sonra:

```bash
python main.py
```

Windows'ta `python` çalışmazsa:

```bash
py main.py
```

## Projenin Durumu

**V1 tamamlandı.**

Bu sürümde kullandığım veri seti küçük ve örnek verilerden oluşuyor. Amacım öncelikle Python, Pandas ve temel istatistik konularını kullanarak çalışan bir analiz sistemi oluşturmak.

İleride projeyi gerçek piyasa verileriyle çalışacak şekilde geliştirmek istiyorum.

## Not

Bu proje eğitim amacıyla geliştirilmiştir ve yatırım tavsiyesi değildir.
