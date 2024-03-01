#1) Calculate the sum, difference, product, and quotient of two numbers.
a=int(input("enter a number a")) 
b=int(input("enter a number b"))
print(" sum is" , a+b )
print(" difference is" , a-b )
print(" product is" , a*b )
print(" quotient is" , a/b )

#2) Perform various assignment operations on a variable.
c =int(input("enter a number"))
d=c
print("assignment = " , d)
c+=10
print("addition assignment c+=10" , c) 
c-=10
print("subtraction assignment c-=10",c) 
c*=10
print("multiplication assignment c*=10",c )
c/=10
print("division assignment c/=10", c) 

#3) Compare two numbers and print the results.
e=int(input("enter a number e"))
f=int(input("enter a number f"))
print("e is greater than f" ,e>f)
print("f is greater than e" , f>e)

#4) Check conditions using logical operators.
g=int(input("enter a number g"))
h=int(input("enter a number h"))
f=g>10 and h>15
print("g >10 and h>15",f )
k=g>10 and h>60
print("g >10 or h > 60", k)
print("not g==h",  not g==h)

#5)Check the identity of variables.
i=int(input("enter a number i"))
j=int(input("enter a number j"))
print("i is j" ,i is j)
print("i is j" ,i is not j)

#6)Perform bitwise operations on any two integers.
x=int(input("enter a number x"))
y=int(input("enter a number y"))
print("x & y" , x&y)
print("x | y" , x|y)
print(" ~y" , ~y)

#7) Use unary operators to change the sign of a number.
s=int(input("enter a number s"))
h=-s
print("changed sign " ,h) 

#8) Use the ternary operator to assign values based on conditions.
a=int(input("enter a number a")) 
result = "Greater than 10" if a> 10 else "Less than or equal to 10"
print(result)

