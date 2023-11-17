awal = 1
akhir = 5
total = 0

while awal <= akhir:
    total += awal
    print (awal,end="")
    if awal < akhir:
        print (" + ",end="")
    awal += 1
print (f" = {total}")