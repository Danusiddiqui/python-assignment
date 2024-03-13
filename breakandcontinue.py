# Write a program to print numbers from 1 to 10, but stop if the number is 5.
for i in range (1,11):
    print(i)
    if i==5:
        break

#Write a program to iterate through a list and stop when encountering a specific element. 
list2=[ 1,2,3,4,5,6,7,8,9,10,11,12]
i=int(input("enter stopping element between 1 to 10"))
for list1 in list2:
    print(list1)
    if list1==i:
        break

#Write a program to skip printing even numbers from  1 to 10.
for i in range(1,11): 
    if i%2==1:
        print(i)
        continue      

#Write a program to print numbers from 0 to 9 using range()
for i in range(1,10):
        print(i)        

""" Write a program to print multiplication tables from 1 to 5, 
but stop after the first table is printed for each number. """
for i in range (1,6):
    for j in range(1,11):    
        result=i*j
        print(f"{i} X {j} = {result}\n" , end="" )
    print("stops")

#Write a program to skip printing even numbers using a while loop.
i=1
n=int(input("enter num"))
while i<n: 
    if i%2 !=0 :
     print(i) 
    i=i+1  