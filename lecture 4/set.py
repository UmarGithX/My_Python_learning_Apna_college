# Set is the collection of the unordered items.
# Each element in the set must be unique & immutable.
# the set is like the dictonary but it dont accept the Dublication and it has not any keys.
collection = {1,3,5,8,7,6}

print(collection)
print(type(collection))
print(len(collection))

# creating Empty Set
colect = set() # this is how we can create an Empty set.

#Some Common properties of Set

# .union it is like the maths one it will collect the unique values from 2 different sets.
col1 = {1,2,3,4,5}
col2 = {4,5,6,7,8,9}
print(col1.union(col2))

# .intersection It will pick the common values only
print(col1.intersection(col2))





