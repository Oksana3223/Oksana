'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
from math import sqrt
x1,y1=int(input()),int(input())
x2,y2=int(input()),int(input())
x3,y3=int(input()),int(input())

a=sqrt((x2-x1)**2+(y2-y1)**2)
b=sqrt((x3-x1)**2+(y3-y1)**2)
c=sqrt((x3-x2)**2+(y3-y2)**2)

P=a+b+c

p=P/2
S=sqrt(p*(p-a)*(p-b)*(p-c))

R=a*b*c/4*S

P=round(P,3)
S=round(S,3)
R=round(R,3)

print('Периметр треугольника:',P)
print('Площадь треугольника:',S)
print('Радиус треугольника:',R)