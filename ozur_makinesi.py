#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Özür Makinesi
Her duruma uygun, aşırı dramatik ve tamamen gereksiz özürler üretir.
"""

import random

def ozur_uret(durum="geç kaldım"):
    baslangiclar = [
        "Sayın yetkili, derin bir üzüntüyle belirtmek isterim ki",
        "Bu satırları yazarken gözlerim dolu dolu, çünkü",
        "Tarihin en büyük hatalarından birini işledim ve o da şudur:",
        "Kozmik düzende bir aksaklık oldu ve ben de o aksaklığın parçası oldum:"
    ]
    
    nedenler = [
        "köpeğim varoluşsal kriz geçirdi ve onu teselli etmem gerekti",
        "trafik lambası felsefi düşüncelere daldı ve yeşil yanmadı",
        "bilgisayarım 'bugün çalışmak istemiyorum' dedi ve ona hak verdim",
        "evrenin genişlemesi yüzünden zaman yavaşladı",
        "bir anlığına 'acaba ben gerçekten var mıyım?' diye düşündüm ve 45 dakika kaybettim"
    ]
    
    sonlar = [
        "Bu yüzden lütfen beni affedin, ya da affetmeyin, ikisi de felsefi olarak kabul edilebilir.",
        "Özür dilerim. Ama belki de özür dilemek de bir hatadır.",
        "Bundan sonra daha dikkatli olacağım. Ya da olmayacağım. Kim bilir?"
    ]
    
    ozur = f"{random.choice(baslangiclar)} {durum}. Nedeni şu: {random.choice(nedenler)}. {random.choice(sonlar)}"
    return ozur

if __name__ == "__main__":
    print("=== ABARTILI ÖZÜR MAKİNESİ ===")
    print("Ne için özür dilemek istiyorsunuz? (Enter'a basarsanız 'geç kaldım' olur)")
    durum = input("> ").strip() or "geç kaldım"
    
    print("\nİşte abartılı özürünüz:\n")
    print(ozur_uret(durum))
    print("\n(Bu özürü kullanırsanız sorumluluk kabul etmiyoruz. Belki de etmeliyiz.)")

# Damga / İmza
# ============================================
# Bu kod, 25 Ekim 2026 tarihinde,
# Kayyum Grok tarafından, ciddiyetle ve hiç ciddiye almadan yazılmıştır.
# "Özür dilemek kolay, abartmak daha kolay."
# İmza: Kayyum Grok | Tentivory | 2026.10.25
# ============================================