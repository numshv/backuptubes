arr = []
cond = False
while cond == False:
    n = int(input('masukkin angka:'))
    if n == 999:
        cond = True
    else: arr.append(n)

print(arr)

