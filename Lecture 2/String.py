str1= "This is a String"
str2 = "This is a way we can shift line in Pythob by adding \nIn the Line and this will not be printable"
str3 = "If we want it add the TAB in a sentence Just add \tand the tab will apply"
print(str2)

# we can Conctinate the Words by adding "+" Between two words
word1 = "Muhammad" 
word2 = "Umar"
con = (word1+word2)
print(con)
# len is a function in python which count the characters.
print(len(word2)) # this will count the lenght of Muhammad and print it.

# indexing 
# 1st way
age = "Fifteen"
ind = age[2]
print(ind)

# 2nd way
name = "Umar khan"

char = name[2]
print(char)

# slicing
slic = "UmarKhan"
print(slic[1:])



name = input("Enter the Name : " )
print(name)
print("The Length of the string is :",len(name))
index = int((input("Enter the number of Index you wnats :")))
print(name[index])

# practice
 
# WAP to Input user's first name & print Its length.
First_name = "Umar"
print(len(First_name))

# WAP to find the occurrence of $ in a String.
track = "ho $ is it Called $ is callled $ dollar"
print(track.count("$"))