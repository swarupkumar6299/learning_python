"""
num1= int(input("Enter your 1st no:= "))
num2= int(input("Enter your 2nd no:= "))

if num1>num2:
    print("number 1st is grestest")
elif num2>num1:
    print("Number 2nd is greatest")
else:
    print("both number are equal")
"""

#Asking 5 mark from user Calculate percentage and print it 
#  91 -- 100 ---> A grade
#  81 -- 90 ----> B Grade
#  71 --80 ----->C Grade
#  61 -- 70-----> D Grade
#  1 ---60 -----> fail
# Invalid
math= int(input("Enter mark in your math= "))
Scence= int(input("Enter mark in your Scence= "))
English= int(input("Enter mark in your English= "))
History= int(input("Enter mark in your History= "))
Geography= int(input("Enter mark in your Geography= "))

Total=  math + Scence + English + History + Geography
percentage =  (Total/500)*100
print(f"percentage score = {percentage} ")

if percentage>91 and percentage<100:
    print("A grade")
elif percentage>81 and percentage< 90:
    print("B Grade")
elif percentage>71 and percentage<80:
    print("C grade")
elif percentage> 61 and percentage < 70:
    print("D grade")
elif percentage>1 and percentage < 60:
    print("Fail")
else:
    print("Invalid") 