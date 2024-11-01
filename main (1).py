'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())
x4,y4=map(int,input().split())


area = 0.5 * abs(x1*y2+x2*y3+x3*y4+x4*y1-(y1*x2+y2*x3+y3*x4+y4*x1)
)


print (area)