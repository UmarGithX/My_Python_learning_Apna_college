# 
# Dictionaries are used to store data values in key:value pairs
# They are unordered, mutable(changeable) & don't allow duplicate keys
dict = {
    "name" : "Umar",
    "age" : "fifteen",
    "learning" : "Coding"
}
print(dict)

key = {
    'old' : 52,
    'height' : 6.02,
    'date' : 22,
    'marks' : [23,45,645,866],
    'names' : ("Umar", "Maaz Khan" , "Hassan")
}
print(key)

print(dict["name"])
print(dict["learning"])

# we can Update the value of the Dictonary in Python 
dict["age"] = "34"
print(dict)
# Also we can add the New Value in Dictonary.
dict["Marks"] = "560"
print(dict)

# nesting in DIctonary
Student_info = {
    "Student name" : "ali",
    "Subjects" : {
        "English" : 78,
        "Arabic" : 58,
        "Computer" : 76,
        "maths" : 96,
    }
}
# this way we can get the info from the Dictonary the Nested Dictonary
print(Student_info["Subjects"]["maths"])
