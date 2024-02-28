#1) Convert an integer to a floating-point number.
a=int(input("enter an integer"))
b=float(a)
print(b)

#2) Convert a float to a integer.
c=float(input("enter a floating number"))
d=int(c)
print(d)

#3) Convert a integer to a string.
e=int(input("enter an integer number"))
f=str(e)
print("string is " , f)
print(type(f))

#4) Convert a list to a tuple.
list1 = [1,2,3,"ajay" , 5+7j , True , "a"]
tuple1= tuple(list1)
print(tuple1)
print(type(tuple1))

#5) Convert a tuple to a list.
tuple2 = (1,7,8,3,"vijay" , 5+7j , True , "a", 54)
list2= list(tuple2)
print(list2)
print(type(list2))

#6)Convert a decimal number to binary.
g=int(input("enter an int decimal no"))
h=bin (g)
print(h)

#7)Convert a non-zero number to boolean.
i=int(input(" enter non zero no"))
j=bool(i)
print(j)
print(type(j))