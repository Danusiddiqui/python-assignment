#Print numbers from 1 to 5 using a while loop.
n=5
i=1
while i<=n :
    print(i)
    i=i+1

#Calclate the sum of numbers from 1 to 10 using a while loop.  
n=10
i=1
sumofnum=0
while i<=n :
   sumofnum=sumofnum+i
   i=i+1
print("sum of numbers 1 to 10 " ,sumofnum)

#Calclate the factorial of a number using a for loop.
n = int(input("Enter a number: "))
factorial=1
for i in range(1,n + 1):
       factorial = factorial*i
print(factorial)

#Count the number of vowel in a string using a for loop.
s=input("enter word")
c=0
d=0
for char in s:
 if (char=="a" or char=="e"or char=="i" or char=="0" or char=="u" or char== "A" or char=="E" or char== "I" or char=="O" or char=="U"):
      c=c+1
d=c
print("no of vowels are" , d) 

# Print a pattern using nested loop.
n=int(input("enter no"))
i=1
while i<=n:
  j=1
  while j<=i:
         print("*" , end="")
         j=j+1
  print()
  i=i+1

#Generate a multiplication table using nested loop. 
row=int(input("enter no of rows"))
for i in range(1,row+1):
     for j in range(1,11):
      result = i*j
      print(f"{i} x {j} = {result}\n", end="") 
     print ()
      
