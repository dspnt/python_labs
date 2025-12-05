m = int(input("Минуты:"))
while m > 1440:
    m = m - 1440
n = m // 60
n1 = m - n * 60
if n1 < 10:
    print(f"{n}:0{n1}")
else:
    print(f"{n}:{n1}")
