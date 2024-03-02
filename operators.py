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
if e>f:
  print(f"{e} is greater than {f}")
elif f>e: 
  print(f"{f} is greater than {e}")
else : 
  print("they are equal")

#4) Check conditions using logical operators.
x=int(input("enter a number x"))
y=int(input("enter a number y"))
z=int(input("enter a number z"))
if x < y and y < z:
    print(f"{x} is less than {y}, and {y} is less than {z}")

if x == 5 or z == 15:
    print(f"{x} is equal to 5, or {z} is equal to 15")

if not x > z:
    print(f"{x} is not greater than {z}")

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

