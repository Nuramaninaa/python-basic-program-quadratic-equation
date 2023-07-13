#python program to solve quadratic equation

#import complex math module to perform mathematical operations
import cmath

#initialize value a,b,c
a = 8
b = 16
c = 8

#calculate the discriminant d = (b^2 - 4ac)
d = (b**2) - (4*a*c)

#two answer for positive and negative
ans1 = (-b-cmath.sqrt(d))/(2*a)
ans2 = (-b+cmath.sqrt(d))/(2*a)

#print the two answer
print("The answer 1 and answer 2 is ",ans1,ans2)