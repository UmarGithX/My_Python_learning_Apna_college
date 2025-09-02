# WAP to find the greatest of 3 numbers entered by the user.
num1 = int(input("Enter 1st Number"))
num2 = int(input("Enter 2nd Number"))
num3 = int(input("Enter 3rd Number"))


if(num1 > num2 and num1 > num3):
    greater = "number 1st is greater>"
elif(num2 > num1 and num2 > num3):
    greater = "number 2nd is greater>"
elif(num3 > num1 and num3 > num2):
    greater = "number 3rd is greater>"
else:
    print("  '   ")

print(greater)