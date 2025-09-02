# Figure out a way to store 9 & 9.0 as separate values in the set.
# (You can take help of built-in data types)
# method 1
values = {"9" , 9.0}
print(values)

# method 2
val = {
    ("int" , 9),
    ("float" , 9.0)
} 
print(type(val))
print(val)