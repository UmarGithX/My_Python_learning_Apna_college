# this is a nesting program which we deside to who will drive
# if Your age is less then 18 you cannot Drive and if your age is greater then 80 you also not Drive
age = int(input("Enter Your Age : "))
if(age >= 18):
    if(age >=81):
        print("You cannot Drive")
    else:
        print("You can Drive")
else:
    print("You cannot Drive")