# 5-masala
#raqamni kiriting va shu indeksiyaga fibonochi sonlar ro'yhatini tuzing
#fibonochi sonlar -> 1, 1, 2, 3, 8, 13, 21
 indeks = int(input("=>"))
 a = []

 for i in range(indeks +1)
     if i ==0 or i==1:
         a.append(1)
 else:
     a.append(a[i-1]+a[i-2])
     print(a)
