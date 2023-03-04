# 6-  Liste elemanlarını ters çevirin.
names = ['Ali','Yağmur','Hakan','Deniz']

newlist = []

for i in range(-1, -len(names)-1, -1):
    newlist.append(names[i])

names = newlist

print(names)