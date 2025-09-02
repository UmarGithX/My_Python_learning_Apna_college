# lsit in python 
# A built-in data type that stores set of values
# It can store elements of different types (integer, float, string, etc.)

marks= [12,85,95,78,42,85,65,45]
print(marks[0])
# print(type(marks))

person = ["Umar" , 25 , "Russia"]
print(person)
person[0] = "Muhammad Umar"
print(person)

# this will add the new value at the end of the list
marks.append(455) 
print(marks)

# sort 
# this will sort in assending order
marks.sort()
print(marks)

# sorting From revurse
# this will sort the value from the revurse
marks.sort(reverse=True)
print(marks)

# revurse 
# the list will be in origial form but it will revurse
marks.reverse()
print(marks)

# insert 
# it works like the append but you have choice where you wants to insert the Data.
marks.insert(0,"Starting:")
print(marks)

# remove 
# it will remove the Data 1st Occure in the List
marks.remove(42)
print(marks)

# pop
# it will remove the Data From the list but its Your Choice this time which you wants to remove
marks.pop(3)
print(marks)