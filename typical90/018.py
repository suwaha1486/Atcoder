# ★3
import math

t = int(input())
l, x, y = map(int, input().split())
q = int(input())

for i in range(q):
    e = int(input())
    theta = 2 * math.pi * e / t
    y_axis = -(l / 2.0) * math.sin(theta)
    z_axis = (l / 2.0) * (1.0 - math.cos(theta))
    
    print(math.atan2(z_axis, math.sqrt(x**2 + (y - y_axis)**2)) * 180 / math.pi)
