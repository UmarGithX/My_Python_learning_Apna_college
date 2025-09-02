# WAP to check if a list contains a palindrome of elements.
li = [1,2,3,2,1]

lis_1 = li.copy()
lis_1.reverse()

if(li==lis_1):
    print("palindrome")
else:
    print("non Palindrome") 