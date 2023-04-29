#calc
a = int(input("a: "))
print("a:", a)
b = int(input("b: "))
print("b:", b)
c = int(input("c: "))
print("c:", c)

s = (a + b + c)/2
print("napivperimeter: ",s)
import math
g = math.sqrt(s * (s - a) * (s - b) * (s - c))
print("Result: ",g)