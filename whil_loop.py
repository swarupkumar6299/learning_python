"""
i=1
while i<=10:
    print("Hello World")
    i=i+1
    print("ok Done")
"""
#print 1 to 10 using while loop
"""
i = 1
while i<=50:
    print(i,end=" ")
    i=i+1
    """
# print 1 to 50 even number
"""
i=1
while i<=50:
    if i%2==0:
        print(i,end=" ") 
    i=i+1
    """
#Ask a number from user. print all the number from 1 to that number.
"""
num =  int(input("Enter your number:- "))
i=1
while i<=num:
    print(i,end=" ")
    i=i+1
    """
#Ask a number (N) from user. Print all the numbers from N to 1
"""
num = int(input("Enter your last no- "))
i=num
while i>=1:
    print(i,end=" ")
    i=i-1
    """
#Ask start number and end number from user. Print all the numbers from start to end using while loop.
"""
num1= int(input("Enter your first No:- "))
num2= int(input("Enter your last No:- "))
i=num1
while i<=num2:
    print(i,end=" ")
    i=i+1
    """
#Calculate the sum of all the numbers from 1 to 10
"""
i=1
Total=0
while i<=10:
    Total=Total+i
    i=i+1
print(Total)
"""
#Calculate product of all the numbers from 1 to 10.
"""
i=1
Total=1
while i<=10:
    Total=Total*i
    i=i+1
print(Total)
"""
#Calculate how many numbers are divisible by 7 from 1 to 100.
"""
i=1
count=0
while i<=100:
    if i%7==0:
     count=count+1
    i=i+1
print(count)
"""
#Calculate how many numbers are divisible by both 6 and 7 between 1 to 200.
"""
i=1
count = 0
while i<=200:
    if i%6==0 and i%7==0:
     count=count+1
    i=i+1
print(count)
"""
#Write a program to calculate the sum of all the numbers divisible by 4 from 20 to 50.

i=20
total=0
while i<=50:
    if i%4==0:
        total=total+i
    i=i+1
print(total)

#Ask a number from user. Print the multiplication table of that number.
"""
Table = int(input("Enter number"))
i=1
while i<=10:
    print(f"{Table} * {i} = {Table*i}" )
    i+=1
    """
#Calculate factorial of a number entered by user.
"""
num = int(input("enter your number:- "))
fact=1
i=1
while i<=num:
    fact=fact*i
    i=i+1
print(f"your given number {num} of factorial is:- {fact}")
"""