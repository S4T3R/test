a = []
s = 0
count = 0
while len(a) < 7:
    b = int(input("dien 1 so: "))
    a.append(b)
    s += b
x = int(input("1 so nao do: "))
for i in range(7):
    if a[i] == x:
        count += 1



print("tong day so la", s)
print("so lon nhat cua day la", max(a))
print("so nho nhat cua day la", min(a))
print("so lan x xuat hien la", count)