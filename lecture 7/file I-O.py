# # Python can be used to perform operations on a file. (read & write data)
f = open("demo.txt" , "a+")
data = f.write("\nthis is the best exaple i ever seen in my lisfe")
print(data)
print (type (data))
f. close()

import os
with open("samole.txt","a+") as f:
    f.write("what is the name of pakistan")
