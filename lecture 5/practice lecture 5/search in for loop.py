# Search for a number x in this tuple using loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

search = int(input("Enter the Search Number ::>>"))
idx = 0
for el in num:
    if el == search:
        print("Founded At index ;", idx)
    idx += 1
else:
    print("<<<>>>")
