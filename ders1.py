﻿


isimler = ['merve acar', 'yaren parlak', 'ali efe akar']
for sahis in isimler:
    isimlistesi = sahis.split(' ')
    print('======= Üst döngü başlıyor =======')
    for isim in isimlistesi:
        print(isim)
    print('======= Üst döngü bitiyor =======')


isimler = ['merve acar', 'yaren parlak', 'efe akar']
nl = []
for sahis in isimler:
    kelimeler = sahis.split()
    nl.append(kelimeler)
    for kelime in kelimeler:
        print(f"{kelime} kelimesinin içinde {len(kelime)} harf var")
print(nl)


isim = 'merve acar'
for kelime in isim.split():
    print(kelime[-3:])
    print(len(kelime))


lls = [2, 3, 4, 2, 3, 6, 5, 8, 9, 11, 10, 20, 12]
for i in lls[-3:]:
    print(i)
