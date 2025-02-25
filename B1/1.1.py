import math
a, b = map(int, input("nhap a, b cach nhau 1 dau cach: ").split())
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b:.3f}")

'''Nhập vào tọa độ của hai điểm A(x1, y1) và B(x2, y2). Tính và in ra khoảng cách Euclidean giữa A và B:'''

x1, y1 = map(float, input("Toa do diem A = ").split())
x2, y2 = map(float, input("Toa do diem B = ").split())
d = pow((x1 - x2),2) + pow((y1 - y2), 2)
print(f"d = {math.sqrt(d):.3f}")