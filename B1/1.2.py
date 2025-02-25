import math

n = int(input("Nhap n: "))
if n < 20 or n > 30:
    while(n < 20 or n > 30):
        n = int(input("Nhap n: "))
x = float(input("Nhap x: "))

# Cách 1
p1 = 2022 * pow(x, n)
for i in range(1, n, 1):
    p1 += i / pow(x, i)
print(f"p1 = {p1:.3f}")

# Cách 2
p2 = 2022 * pow(x, n) + sum(i / pow(x, i) for i in range(n))
print(f"p2 = {p2:.3f}")

# Kiểm tra số nguyên tố
def ngto(n: int) -> bool:
    if n < 2:  # Kiểm tra trường hợp n < 2
        return False
    for i in range(2, math.isqrt(n) + 1):  # Kiểm tra từ 2 đến căn bậc hai của n
        if n % i == 0:
            return False
    return True

print(ngto(n))
