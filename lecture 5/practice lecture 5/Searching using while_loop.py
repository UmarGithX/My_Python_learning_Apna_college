# Search for a number x in this tuple using loop:num
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
index = 0
search = int(input("Enter the Search :"))
while index < len(num):
    if(num [index] == search): 
        print("Search find at index :",index)
    else :
        print("FINDING>>>>....")
    index += 1

