
sonlar =[1,2,3,4,5,6]
for son in sonlar:
    if son%2==1:
        sonlar[sonlar.index(son)]=son*2
    else:
        sonlar[sonlar.index(son)]=son * 2
        print(sonlar)