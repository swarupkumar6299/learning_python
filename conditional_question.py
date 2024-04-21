#Write a program asking user number if print even and odd.
"""
num= int (input("Enter your number:= "))

if num%2==0:
    print("The number is Even")
else:
    print("The number is Odd") 
"""
# Write a program asking user age and verified is user eligible for vote.
"""
age= int(input("Enter your age:= "))
if (age > 18):
    print("You are eligible for vote")
else:
    print("You are not eligible for vote")
"""
"""
# Write a program the student mark asking and condition applied for result.

chemistry= int(input("Enter your chemisery mark:= "))
physic= int(input("Enter your physic mark:= "))
if (chemistry > 33 and physic > 33):
    print("Pass")
else:
    print("Fail")
"""

#Write a python program that takes an integer input and prints wether it's positive, negative .(consider 0 as possitive)
"""
num =  int(input("Enter your number:= "))
if num>=0:
    print("Your number is Possitive")
else:
    print("Your number is Negative")
"""
# Write a program that takes a character as input and prints whether it's a vowel or a consonant. (Multiple OR will be used)
"""
char= input("Enter a Character:= ")
if char== "a" or char == "e" or char == "i" or char == "o"or  char == "u":
    print("Enter Character is Vowel")
else:
    print("Enter your Character is Consonant")
"""
#Write a program that takes two numbers as input and checks if the first number is divisible by the second.
"""
num1 = int(input("Enter your First no.:= "))
num2 = int(input("Enter your second no.:= "))
if num1%num2 ==0:
    print("Yes it's divisible by 1st no.")
else:
    print("No it's not divisibl by 1st no.")
"""

"""
A student will not be allowed to sit in exam if his/her attendance is less than 75%.
Take following input from user Number of classes held Number of classes attended.
1. Print percentage of class attended
2. Print Is student is allowed to sit in exam or not

Number of classes held
Number of classes attended.
"""
class_held= int(input("Enter the class held := "))
class_Attend= int(input("Enter your class attendence:= "))

class_per = (class_Attend/class_held)*100

print(f"percentage of class held:= {class_per:.2f}%")
if class_Attend >=75:
    print("You are eligible for examination")
else:
    print("You are not eligible for examination") 