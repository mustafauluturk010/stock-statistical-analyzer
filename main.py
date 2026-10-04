import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import shapiro


# ============================================================
# STOCK STATISTICAL ANALYZER - V1
# ============================================================

# ============================================================
# 1. VERİYİ YÜKLE
# ============================================================

veri = pd.read_csv("data/stock_data.csv")

baslangic_sermayesi = 1000


# ============================================================
# 2. TEMEL VERİ HAZIRLAMA
# ============================================================

veri["degisim"] = veri["fiyat"].diff()
veri["yuzde_degisim"] = veri["fiyat"].pct_change() * 100

veri["hareketli_ortalama_3"] = (
    veri["fiyat"].rolling(3).mean()
)

veri["hareketli_ortalama_5"] = (
    veri["fiyat"].rolling(5).mean()
)

veri["hareketli_ortalama_7"] = (
    veri["fiyat"].rolling(7).mean()
)


# ============================================================
# 3. HAREKETLİ ORTALAMALAR
# ============================================================

print("\n--- HAREKETLI ORTALAMALAR ---")

print(
    veri[
        [
            "tarih",
            "fiyat",
            "hareketli_ortalama_3",
            "hareketli_ortalama_5",
            "hareketli_ortalama_7"
        ]
    ]
)


# ============================================================
# 4. TEMEL İSTATİSTİKLER
# ============================================================

print("\n--- TEMEL ISTATISTIKLER ---")

print("Ortalama:", veri["fiyat"].mean())
print("Medyan:", veri["fiyat"].median())
print("Standart Sapma:", veri["fiyat"].std())
print("Minimum:", veri["fiyat"].min())
print("Maksimum:", veri["fiyat"].max())
print("Varyans:", veri["fiyat"].var())


# ============================================================
# 5. GETİRİ İSTATİSTİKLERİ
# ============================================================

print("\n--- GETIRI ISTATISTIKLERI ---")

print("Ortalama Getiri:", veri["yuzde_degisim"].mean())
print("Getiri Medyani:", veri["yuzde_degisim"].median())
print("Getiri Standart Sapmasi:", veri["yuzde_degisim"].std())
print("En Yuksek Getiri:", veri["yuzde_degisim"].max())
print("En Dusuk Getiri:", veri["yuzde_degisim"].min())


# ============================================================
# 6. VOLATİLİTE
# ============================================================

volatilite = veri["yuzde_degisim"].std()

print("\n--- VOLATILITE ---")
print("Volatilite:", volatilite)


# ============================================================
# 7. MAXIMUM DRAWDOWN
# ============================================================

zirve = veri["fiyat"].cummax()

drawdown = (
    (veri["fiyat"] - zirve)
    / zirve
    * 100
)

print("\n--- MAXIMUM DRAWDOWN ---")
print("Maximum Drawdown:", drawdown.min(), "%")


# ============================================================
# 8. KORELASYON ANALİZİ
# ============================================================

veri["fiyat_2"] = (
    veri["fiyat"] * 0.98
    + [
        2, -1, 3, -2, 1, 2, -3, 1, -2, 3,
        0, -2, 2, -1, 3, -2, 1, -3, 2, -1,
        3, -2, 1, -3, 2, -1, 3, -2, 1, -3
    ]
)

korelasyon = veri["fiyat"].corr(veri["fiyat_2"])

print("\n--- KORELASYON ---")
print("Korelasyon:", korelasyon)


# ============================================================
# 9. FİYAT VE HAREKETLİ ORTALAMA GRAFİĞİ
# ============================================================

plt.figure(figsize=(10, 5))

plt.plot(
    veri["tarih"],
    veri["fiyat"],
    label="Fiyat"
)

plt.plot(
    veri["tarih"],
    veri["hareketli_ortalama_3"],
    label="3 Gunluk Hareketli Ortalama"
)

plt.xlabel("Tarih")
plt.ylabel("Fiyat")
plt.title("Fiyat ve Hareketli Ortalama")

plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()


# ============================================================
# 10. GÜNLÜK GETİRİ GRAFİĞİ
# ============================================================

plt.figure(figsize=(10, 5))

plt.plot(
    veri["tarih"],
    veri["yuzde_degisim"],
    marker="o"
)

plt.axhline(0)

plt.xlabel("Tarih")
plt.ylabel("Getiri (%)")
plt.title("Gunluk Getiri")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()


# ============================================================
# 11. KORELASYON GRAFİĞİ
# ============================================================

plt.figure(figsize=(8, 5))

plt.scatter(
    veri["fiyat"],
    veri["fiyat_2"]
)

plt.xlabel("Fiyat 1")
plt.ylabel("Fiyat 2")
plt.title("Fiyatlar Arasi Korelasyon")

plt.tight_layout()

plt.show()


# ============================================================
# 12. ANALİZ ÖZETİ
# ============================================================

print("\n--- ANALIZ OZETI ---")

ortalama_getiri = veri["yuzde_degisim"].mean()

if ortalama_getiri > 0:
    print("Ortalama getiri pozitif.")
else:
    print("Ortalama getiri negatif.")


if volatilite < 2:
    print("Volatilite dusuk.")
elif volatilite < 5:
    print("Volatilite orta seviyede.")
else:
    print("Volatilite yuksek.")


if korelasyon > 0.7:
    print("Iki fiyat arasinda guclu pozitif korelasyon var.")
elif korelasyon < -0.7:
    print("Iki fiyat arasinda guclu negatif korelasyon var.")
else:
    print("Iki fiyat arasinda guclu bir korelasyon yok.")


print(
    "Maksimum dusus:",
    round(drawdown.min(), 2),
    "%"
)


# ============================================================
# 13. NORMAL DAĞILIM TESTİ
# ============================================================

istatistik, p_degeri = shapiro(
    veri["fiyat"]
)

print("\n--- NORMAL DAGILIM TESTI ---")

print(
    "Shapiro-Wilk istatistigi:",
    istatistik
)

print(
    "p-degeri:",
    p_degeri
)

if p_degeri > 0.05:
    print(
        "Veriler normal dagilima uyumlu olabilir."
    )
else:
    print(
        "Veriler normal dagilima uymuyor olabilir."
    )


# ============================================================
# 14. FİYAT DAĞILIMI
# ============================================================

plt.figure(figsize=(8, 5))

plt.hist(
    veri["fiyat"],
    bins=5
)

plt.xlabel("Fiyat")
plt.ylabel("Frekans")
plt.title("Fiyat Dagilimi")

plt.tight_layout()

plt.show()


# ============================================================
# 15. Z-SCORE ANALİZİ
# ============================================================

veri["z_score"] = (
    (veri["fiyat"] - veri["fiyat"].mean())
    / veri["fiyat"].std()
)

print("\n--- Z-SCORE ANALIZI ---")

print(
    veri[
        [
            "tarih",
            "fiyat",
            "z_score"
        ]
    ]
)


# ============================================================
# 16. AYKIRI DEĞER ANALİZİ
# ============================================================

Q1 = veri["fiyat"].quantile(0.25)
Q3 = veri["fiyat"].quantile(0.75)

IQR = Q3 - Q1

alt_sinir = Q1 - 1.5 * IQR
ust_sinir = Q3 + 1.5 * IQR

aykiri_degerler = veri[
    (veri["fiyat"] < alt_sinir)
    |
    (veri["fiyat"] > ust_sinir)
]

print("\n--- AYKIRI DEGER ANALIZI ---")

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Alt sinir:", alt_sinir)
print("Ust sinir:", ust_sinir)

if aykiri_degerler.empty:
    print("Aykiri deger bulunamadi.")
else:
    print("Aykiri degerler:")
    print(
        aykiri_degerler[
            [
                "tarih",
                "fiyat"
            ]
        ]
    )


# ============================================================
# 17. GENEL RİSK ANALİZİ
# ============================================================

risk_skoru = (
    volatilite
    + abs(drawdown.min())
    - ortalama_getiri
)

print("\n--- GENEL RISK ANALIZI ---")

print(
    "Risk skoru:",
    round(risk_skoru, 2)
)

if risk_skoru < 3:
    print("Risk seviyesi: Dusuk")
elif risk_skoru < 7:
    print("Risk seviyesi: Orta")
else:
    print("Risk seviyesi: Yuksek")


# ============================================================
# 18. SİNYAL FONKSİYONLARI
# ============================================================

def sinyal_olustur(satir, hareketli_ortalama):
    if pd.isna(satir[hareketli_ortalama]):
        return "BEKLE"

    if satir["fiyat"] > satir[hareketli_ortalama]:
        return "AL"

    return "SAT"


veri["sinyal"] = veri.apply(
    lambda satir: sinyal_olustur(
        satir,
        "hareketli_ortalama_3"
    ),
    axis=1
)

veri["sinyal_ma5"] = veri.apply(
    lambda satir: sinyal_olustur(
        satir,
        "hareketli_ortalama_5"
    ),
    axis=1
)

veri["sinyal_ma7"] = veri.apply(
    lambda satir: sinyal_olustur(
        satir,
        "hareketli_ortalama_7"
    ),
    axis=1
)


# ============================================================
# 19. SİNYALLERİ GÖSTER
# ============================================================

print("\n--- MA3 / MA5 / MA7 SINYALLERI ---")

print(
    veri[
        [
            "tarih",
            "fiyat",
            "sinyal",
            "sinyal_ma5",
            "sinyal_ma7"
        ]
    ]
)

print("\n--- AL / SAT SINYALLERI ---")

print(
    veri[
        [
            "tarih",
            "fiyat",
            "hareketli_ortalama_3",
            "sinyal"
        ]
    ]
)


# ============================================================
# 20. SONRAKİ FİYAT
# ============================================================

veri["sonraki_fiyat"] = veri["fiyat"].shift(-1)


# ============================================================
# 21. SİNYAL BAŞARI ANALİZİ
# ============================================================

def sinyal_basari(satir):

    if satir["sinyal"] == "BEKLE":
        return None

    if pd.isna(satir["sonraki_fiyat"]):
        return None

    if satir["sinyal"] == "AL":

        if satir["sonraki_fiyat"] > satir["fiyat"]:
            return "BAŞARILI"

        return "BAŞARISIZ"

    if satir["sinyal"] == "SAT":

        if satir["sonraki_fiyat"] < satir["fiyat"]:
            return "BAŞARILI"

        return "BAŞARISIZ"

    return None


veri["sinyal_sonucu"] = veri.apply(
    sinyal_basari,
    axis=1
)


print("\n--- SINYAL PERFORMANSI ---")

print(
    veri[
        [
            "tarih",
            "fiyat",
            "sinyal",
            "sonraki_fiyat",
            "sinyal_sonucu"
        ]
    ]
)


# ============================================================
# 22. SİNYAL BAŞARI ORANI
# ============================================================

gecerli_sonuclar = (
    veri["sinyal_sonucu"]
    .dropna()
)

basarili = (
    gecerli_sonuclar == "BAŞARILI"
).sum()

toplam = len(gecerli_sonuclar)

if toplam > 0:
    basari_orani = (
        basarili
        / toplam
        * 100
    )
else:
    basari_orani = 0


print("\n--- SINYAL BASARI ORANI ---")

print(
    "Basarili sinyal:",
    basarili
)

print(
    "Toplam degerlendirilen sinyal:",
    toplam
)

print(
    "Basari orani:",
    round(basari_orani, 2),
    "%"
)


# ============================================================
# 23. STRATEJİ GETİRİ FONKSİYONU
# ============================================================

def strateji_getirisi(satir, sinyal_sutunu):

    sinyal = satir[sinyal_sutunu]

    if sinyal == "BEKLE":
        return None

    if pd.isna(satir["sonraki_fiyat"]):
        return None

    if sinyal == "AL":

        return (
            (satir["sonraki_fiyat"] - satir["fiyat"])
            / satir["fiyat"]
            * 100
        )

    if sinyal == "SAT":

        return (
            (satir["fiyat"] - satir["sonraki_fiyat"])
            / satir["fiyat"]
            * 100
        )

    return None


# ============================================================
# 24. STRATEJİ GETİRİLERİ
# ============================================================

veri["strateji_getirisi"] = veri.apply(
    lambda satir: strateji_getirisi(
        satir,
        "sinyal"
    ),
    axis=1
)

veri["strateji_getirisi_ma5"] = veri.apply(
    lambda satir: strateji_getirisi(
        satir,
        "sinyal_ma5"
    ),
    axis=1
)

veri["strateji_getirisi_ma7"] = veri.apply(
    lambda satir: strateji_getirisi(
        satir,
        "sinyal_ma7"
    ),
    axis=1
)


print("\n--- STRATEJI GETIRILERI ---")

print(
    veri[
        [
            "tarih",
            "fiyat",
            "sinyal",
            "sonraki_fiyat",
            "strateji_getirisi"
        ]
    ]
)


# ============================================================
# 25. STRATEJİ TOPLAM GETİRİLERİ
# ============================================================

ma3_getiri = (
    veri["strateji_getirisi"]
    .sum()
)

ma5_getiri = (
    veri["strateji_getirisi_ma5"]
    .sum()
)

ma7_getiri = (
    veri["strateji_getirisi_ma7"]
    .sum()
)


ilk_fiyat = veri["fiyat"].iloc[0]
son_fiyat = veri["fiyat"].iloc[-1]

al_tut_getirisi = (
    (son_fiyat - ilk_fiyat)
    / ilk_fiyat
    * 100
)


print("\n--- STRATEJI GETIRILERI ---")

print(
    "MA3 strateji getirisi:",
    round(ma3_getiri, 2),
    "%"
)

print(
    "MA5 strateji getirisi:",
    round(ma5_getiri, 2),
    "%"
)

print(
    "MA7 strateji getirisi:",
    round(ma7_getiri, 2),
    "%"
)

print(
    "Al-Tut getirisi:",
    round(al_tut_getirisi, 2),
    "%"
)


# ============================================================
# 26. AL-TUT KARŞILAŞTIRMASI
# ============================================================

print("\n--- AL VE TUT KARSILASTIRMASI ---")

print(
    "Al ve tut getirisi:",
    round(al_tut_getirisi, 2),
    "%"
)

print(
    "MA3 strateji getirisi:",
    round(ma3_getiri, 2),
    "%"
)

fark = ma3_getiri - al_tut_getirisi

print(
    "MA3 stratejisinin farki:",
    round(fark, 2),
    "%"
)


# ============================================================
# 27. MA3 PORTFÖYÜ
# ============================================================

veri["portfoy_getirisi"] = (
    veri["strateji_getirisi"]
    .fillna(0)
)

veri["portfoy_degeri"] = (
    baslangic_sermayesi
    * (
        1
        + veri["portfoy_getirisi"] / 100
    ).cumprod()
)


# ============================================================
# 28. MA5 VE MA7 PORTFÖYLERİ
# ============================================================

veri["portfoy_ma5"] = (
    float(baslangic_sermayesi)
)

veri["portfoy_ma7"] = (
    float(baslangic_sermayesi)
)


for i in range(1, len(veri)):

    onceki_ma5 = veri.loc[
        i - 1,
        "portfoy_ma5"
    ]

    onceki_ma7 = veri.loc[
        i - 1,
        "portfoy_ma7"
    ]

    getiri_ma5 = veri.loc[
        i,
        "strateji_getirisi_ma5"
    ]

    getiri_ma7 = veri.loc[
        i,
        "strateji_getirisi_ma7"
    ]

    if pd.notna(getiri_ma5):

        veri.loc[
            i,
            "portfoy_ma5"
        ] = (
            onceki_ma5
            * (1 + getiri_ma5 / 100)
        )

    else:

        veri.loc[
            i,
            "portfoy_ma5"
        ] = onceki_ma5


    if pd.notna(getiri_ma7):

        veri.loc[
            i,
            "portfoy_ma7"
        ] = (
            onceki_ma7
            * (1 + getiri_ma7 / 100)
        )

    else:

        veri.loc[
            i,
            "portfoy_ma7"
        ] = onceki_ma7


# ============================================================
# 29. AL-TUT PORTFÖYÜ
# ============================================================

veri["portfoy_al_tut"] = (
    baslangic_sermayesi
    * (
        veri["fiyat"]
        / veri["fiyat"].iloc[0]
    )
)


# ============================================================
# 30. PORTFÖY SONUÇLARI
# ============================================================

print("\n--- TUM STRATEJILER PORTFOY KARSILASTIRMASI ---")

print(
    "MA3 son portfoy:",
    round(
        veri["portfoy_degeri"].iloc[-1],
        2
    ),
    "TL"
)

print(
    "MA5 son portfoy:",
    round(
        veri["portfoy_ma5"].iloc[-1],
        2
    ),
    "TL"
)

print(
    "MA7 son portfoy:",
    round(
        veri["portfoy_ma7"].iloc[-1],
        2
    ),
    "TL"
)

print(
    "Al-Tut son portfoy:",
    round(
        veri["portfoy_al_tut"].iloc[-1],
        2
    ),
    "TL"
)


# ============================================================
# 31. PORTFÖY TABLOSU
# ============================================================

print("\n--- PORTFOY PERFORMANSI ---")

print(
    veri[
        [
            "tarih",
            "fiyat",
            "sinyal",
            "strateji_getirisi",
            "portfoy_degeri"
        ]
    ]
)


# ============================================================
# 32. PORTFÖY KARŞILAŞTIRMA GRAFİĞİ
# ============================================================

plt.figure(figsize=(10, 6))

plt.plot(
    veri["tarih"],
    veri["portfoy_degeri"],
    label="MA3"
)

plt.plot(
    veri["tarih"],
    veri["portfoy_ma5"],
    label="MA5"
)

plt.plot(
    veri["tarih"],
    veri["portfoy_ma7"],
    label="MA7"
)

plt.plot(
    veri["tarih"],
    veri["portfoy_al_tut"],
    label="Al-Tut"
)

plt.axhline(
    y=baslangic_sermayesi,
    linestyle="--",
    label="Baslangic: 1000 TL"
)

plt.title(
    "1000 TL'nin Stratejilere Gore Portfoy Degisimi"
)

plt.xlabel("Tarih")
plt.ylabel("Portfoy Degeri (TL)")

plt.xticks(rotation=45)

plt.legend()
plt.grid()
plt.tight_layout()

plt.show()


# ============================================================
# 33. KÜMÜLATİF GETİRİ GRAFİĞİ
# ============================================================

ma3_kumulatif = (
    veri["strateji_getirisi"]
    .fillna(0)
    .cumsum()
)

ma5_kumulatif = (
    veri["strateji_getirisi_ma5"]
    .fillna(0)
    .cumsum()
)

ma7_kumulatif = (
    veri["strateji_getirisi_ma7"]
    .fillna(0)
    .cumsum()
)

al_tut_kumulatif = (
    veri["fiyat"]
    / veri["fiyat"].iloc[0]
    - 1
) * 100


plt.figure(figsize=(10, 6))

plt.plot(
    veri["tarih"],
    ma3_kumulatif,
    label="MA3"
)

plt.plot(
    veri["tarih"],
    ma5_kumulatif,
    label="MA5"
)

plt.plot(
    veri["tarih"],
    ma7_kumulatif,
    label="MA7"
)

plt.plot(
    veri["tarih"],
    al_tut_kumulatif,
    label="Al-Tut"
)

plt.title(
    "Strateji Getirilerinin Karsilastirilmasi"
)

plt.xlabel("Tarih")
plt.ylabel("Kumulatif Getiri (%)")

plt.legend()
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()

plt.show()


# ============================================================
# 34. STRATEJİ SONUÇLARI
# ============================================================

sonuclar = pd.DataFrame({
    "Strateji": [
        "MA3",
        "MA5",
        "MA7",
        "Al-Tut"
    ],

    "Son Portföy (TL)": [
        veri["portfoy_degeri"].iloc[-1],
        veri["portfoy_ma5"].iloc[-1],
        veri["portfoy_ma7"].iloc[-1],
        veri["portfoy_al_tut"].iloc[-1]
    ]
})


sonuclar["Getiri (%)"] = (
    (
        sonuclar["Son Portföy (TL)"]
        - baslangic_sermayesi
    )
    / baslangic_sermayesi
) * 100


print("\n--- STRATEJI SONUCLARI ---")

print(
    sonuclar.round(2)
)


# ============================================================
# 35. EN YÜKSEK GETİRİLİ STRATEJİ
# ============================================================

en_iyi = sonuclar.loc[
    sonuclar["Son Portföy (TL)"].idxmax()
]

print("\n--- EN IYI STRATEJI ---")

print(
    f"{en_iyi['Strateji']} -> "
    f"{en_iyi['Son Portföy (TL)']:.2f} TL "
    f"(%{en_iyi['Getiri (%)']:.2f})"
)


# ============================================================
# 36. MAXIMUM DRAWDOWN FONKSİYONU
# ============================================================

def maksimum_dusus(portfoy):

    zirve = portfoy.cummax()

    dusus = (
        (portfoy - zirve)
        / zirve
    )

    return dusus.min() * 100


# ============================================================
# 37. STRATEJİ RİSKLERİ
# ============================================================

getiriler = {
    "MA3": veri["portfoy_degeri"]
    .pct_change()
    .dropna(),

    "MA5": veri["portfoy_ma5"]
    .pct_change()
    .dropna(),

    "MA7": veri["portfoy_ma7"]
    .pct_change()
    .dropna(),

    "Al-Tut": veri["portfoy_al_tut"]
    .pct_change()
    .dropna()
}


portfoyler = {
    "MA3": veri["portfoy_degeri"],
    "MA5": veri["portfoy_ma5"],
    "MA7": veri["portfoy_ma7"],
    "Al-Tut": veri["portfoy_al_tut"]
}


risk_sonuclari = pd.DataFrame({
    "Strateji": list(getiriler.keys()),

    "Standart Sapma (%)": [
        getiriler["MA3"].std() * 100,
        getiriler["MA5"].std() * 100,
        getiriler["MA7"].std() * 100,
        getiriler["Al-Tut"].std() * 100
    ],

    "Maximum Drawdown (%)": [
        maksimum_dusus(portfoyler["MA3"]),
        maksimum_dusus(portfoyler["MA5"]),
        maksimum_dusus(portfoyler["MA7"]),
        maksimum_dusus(portfoyler["Al-Tut"])
    ]
})


print("\n--- RISK ANALIZI ---")

print(
    risk_sonuclari.round(2)
)


# ============================================================
# 38. SHARPE RATIO
# ============================================================

sharpe_sonuclari = pd.DataFrame({

    "Strateji": list(getiriler.keys()),

    "Ortalama Getiri (%)": [
        getiriler["MA3"].mean() * 100,
        getiriler["MA5"].mean() * 100,
        getiriler["MA7"].mean() * 100,
        getiriler["Al-Tut"].mean() * 100
    ],

    "Standart Sapma (%)": [
        getiriler["MA3"].std() * 100,
        getiriler["MA5"].std() * 100,
        getiriler["MA7"].std() * 100,
        getiriler["Al-Tut"].std() * 100
    ]
})


risksiz_getiri = 0


sharpe_sonuclari["Sharpe Ratio"] = (
    (
        sharpe_sonuclari["Ortalama Getiri (%)"]
        - risksiz_getiri
    )
    /
    sharpe_sonuclari["Standart Sapma (%)"]
)


print("\n--- SHARPE RATIO ANALIZI ---")

print(
    sharpe_sonuclari.round(3)
)


# ============================================================
# 39. EN İYİ RİSK / GETİRİ STRATEJİSİ
# ============================================================

en_iyi_sharpe = sharpe_sonuclari.loc[
    sharpe_sonuclari["Sharpe Ratio"].idxmax()
]


print(
    "\n--- EN IYI RISK/GETIRI STRATEJISI ---"
)

print(
    f"{en_iyi_sharpe['Strateji']} -> "
    f"Sharpe Ratio: "
    f"{en_iyi_sharpe['Sharpe Ratio']:.3f}"
)


# ============================================================
# 40. RİSK / GETİRİ GRAFİĞİ
# ============================================================

plt.figure(figsize=(10, 6))

plt.scatter(
    risk_sonuclari["Standart Sapma (%)"],
    sonuclar["Getiri (%)"]
)


for i, strateji in enumerate(
    risk_sonuclari["Strateji"]
):

    plt.annotate(
        strateji,
        (
            risk_sonuclari[
                "Standart Sapma (%)"
            ].iloc[i],

            sonuclar[
                "Getiri (%)"
            ].iloc[i]
        )
    )


plt.axhline(
    y=0,
    linestyle="--"
)

plt.xlabel(
    "Risk - Standart Sapma (%)"
)

plt.ylabel(
    "Getiri (%)"
)

plt.title(
    "Stratejilerin Risk - Getiri Karsilastirmasi"
)

plt.grid()
plt.tight_layout()

plt.show()


# ============================================================
# 41. SHARPE RATIO GRAFİĞİ
# ============================================================

plt.figure(figsize=(10, 6))

plt.bar(
    sharpe_sonuclari["Strateji"],
    sharpe_sonuclari["Sharpe Ratio"]
)

plt.axhline(
    y=0,
    linestyle="--"
)

plt.title(
    "Stratejilerin Sharpe Ratio Karsilastirmasi"
)

plt.xlabel("Strateji")
plt.ylabel("Sharpe Ratio")

plt.grid(axis="y")
plt.tight_layout()

plt.show()


# ============================================================
# 42. GENEL STRATEJİ ANALİZİ
# ============================================================

genel_sonuclar = pd.DataFrame({

    "Strateji":
        sonuclar["Strateji"],

    "Son Portföy (TL)":
        sonuclar["Son Portföy (TL)"],

    "Getiri (%)":
        sonuclar["Getiri (%)"],

    "Standart Sapma (%)":
        risk_sonuclari[
            "Standart Sapma (%)"
        ],

    "Maximum Drawdown (%)":
        risk_sonuclari[
            "Maximum Drawdown (%)"
        ],

    "Sharpe Ratio":
        sharpe_sonuclari[
            "Sharpe Ratio"
        ]
})


print(
    "\n--- GENEL STRATEJI ANALIZI ---"
)

print(
    genel_sonuclar.round(2)
)


# ============================================================
# 43. RİSK / GETİRİ SIRALAMASI
# ============================================================

sirali_sonuclar = (
    genel_sonuclar
    .sort_values(
        by="Sharpe Ratio",
        ascending=False
    )
    .reset_index(drop=True)
)


print(
    "\n--- RISK/GETIRI SIRALAMASI ---"
)

print(
    sirali_sonuclar.round(2)
)


# ============================================================
# 44. STRATEJİ PUANLAMA SİSTEMİ
# ============================================================

puanlama = genel_sonuclar.copy()


puanlama["Getiri Puanı"] = (
    puanlama["Getiri (%)"]
    .rank(
        ascending=False,
        method="min"
    )
)


puanlama["Sharpe Puanı"] = (
    puanlama["Sharpe Ratio"]
    .rank(
        ascending=False,
        method="min"
    )
)


puanlama["Risk Puanı"] = (
    puanlama["Standart Sapma (%)"]
    .rank(
        ascending=True,
        method="min"
    )
)


puanlama["Drawdown Puanı"] = (
    puanlama["Maximum Drawdown (%)"]
    .rank(
        ascending=False,
        method="min"
    )
)


puanlama["Toplam Puan"] = (
    puanlama["Getiri Puanı"]
    + puanlama["Sharpe Puanı"]
    + puanlama["Risk Puanı"]
    + puanlama["Drawdown Puanı"]
)


puanlama = (
    puanlama
    .sort_values(
        by="Toplam Puan",
        ascending=True
    )
    .reset_index(drop=True)
)


print(
    "\n--- STRATEJI PUANLAMA ---"
)

print(
    puanlama[
        [
            "Strateji",
            "Getiri Puanı",
            "Sharpe Puanı",
            "Risk Puanı",
            "Drawdown Puanı",
            "Toplam Puan"
        ]
    ].round(2)
)


# ============================================================
# 45. FİNAL STRATEJİ KARARI
# ============================================================

en_iyi_genel = puanlama.iloc[0]


print(
    "\n--- FINAL STRATEJI KARARI ---"
)

print(
    f"En iyi genel strateji: "
    f"{en_iyi_genel['Strateji']}"
)

print(
    f"Toplam puan: "
    f"{en_iyi_genel['Toplam Puan']:.0f}"
)

print(
    f"Getiri: "
    f"%{en_iyi_genel['Getiri (%)']:.2f}"
)

print(
    f"Sharpe Ratio: "
    f"{en_iyi_genel['Sharpe Ratio']:.3f}"
)

print(
    f"Standart Sapma: "
    f"%{en_iyi_genel['Standart Sapma (%)']:.2f}"
)

print(
    f"Maximum Drawdown: "
    f"%{en_iyi_genel['Maximum Drawdown (%)']:.2f}"
)


# ============================================================
# 46. FİNAL RAPOR
# ============================================================

print("\n")
print("=" * 60)
print("              STOCK STATISTICAL ANALYZER")
print("                   FINAL RAPOR")
print("=" * 60)


print("\n[VERI ANALIZI]")

print(
    f"Toplam veri sayisi: {len(veri)}"
)

print(
    f"Baslangic fiyati: "
    f"{veri['fiyat'].iloc[0]:.2f} TL"
)

print(
    f"Son fiyat: "
    f"{veri['fiyat'].iloc[-1]:.2f} TL"
)


print("\n[SINYAL ANALIZI]")

print(
    f"Basarili sinyal: {basarili}"
)

print(
    f"Degerlendirilen sinyal: {toplam}"
)

print(
    f"Sinyal basari orani: %{basari_orani:.2f}"
)


print("\n[STRATEJI SONUCLARI]")


for _, satir in genel_sonuclar.iterrows():

    print(
        f"{satir['Strateji']:<8} | "
        f"Portfoy: "
        f"{satir['Son Portföy (TL)']:>8.2f} TL | "
        f"Getiri: "
        f"%{satir['Getiri (%)']:>7.2f} | "
        f"Sharpe: "
        f"{satir['Sharpe Ratio']:>6.3f}"
    )


print("\n[EN IYI STRATEJI]")

print(
    f"Strateji: "
    f"{en_iyi_genel['Strateji']}"
)

print(
    f"Son Portfoy: "
    f"{en_iyi_genel['Son Portföy (TL)']:.2f} TL"
)

print(
    f"Getiri: "
    f"%{en_iyi_genel['Getiri (%)']:.2f}"
)

print(
    f"Sharpe Ratio: "
    f"{en_iyi_genel['Sharpe Ratio']:.3f}"
)

print(
    f"Standart Sapma: "
    f"%{en_iyi_genel['Standart Sapma (%)']:.2f}"
)

print(
    f"Maximum Drawdown: "
    f"%{en_iyi_genel['Maximum Drawdown (%)']:.2f}"
)


print("\n" + "=" * 60)
print("                 ANALIZ TAMAMLANDI")
print("=" * 60)