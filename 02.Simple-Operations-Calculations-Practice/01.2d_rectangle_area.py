import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

length = math.fabs(x1 - x2)
height = math.fabs(y2 - y1)

area = length * height
perimeter = 2 * (length + height)

print(area)
print(perimeter)
