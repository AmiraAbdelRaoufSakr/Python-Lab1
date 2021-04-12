import math
#Enter two points represented as x1_1,x_2,y_1,y_2

x_1=int(input("Enter x1: "))
y_1=int(input("Enter y1: "))
x_2=int(input("Enter x2: "))
y_2=int(input("Enter y2: "))

d=float(math.sqrt(math.pow(x_1-x_2, 2)+math.pow(y_1-y_2, 2)))

print(f'The distance between 2 points is {d}')
