"""5-masala 3x3 matrisa matrisa har bir elementini alohida qatorga chiqaring"""
a = [[1,2,3],[4,5,6],[7,8,9]] #matrisani tuzamiz
#1-usul
for element in a:  #a ni ichidan qavs to'plamlarini oladi [1,2,3]
    for i in element: #olingan qavs to'plam ichidagi elementni oladi masalan [1,2,3] dan 1
        print(i)

#2-usul
for i in range(3):
    for j in range(3):
        print(a[i][j])