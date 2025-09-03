# # Reading data from a text file 
# f = open('test.txt' , 'r')#with r we read the data
# data = f.read()
# print(data)

# # writing data From a text file 
# r = open('donere.txt' , 'w')#with w we write the data
# write = r.write('1 i am write function\n2 this is the secon line \n3 line is the 3rd line.')
# print(write)

# # writing in the data at the laast
# l = open('appending.txt' , 'a')
# a = l.write('\nat last i will move to the 3rd line')

# r+
# in r+ mode we can read and wirte the data at the same time

q= open('donere.txt' , 'r+')
w = q.write("now this will be only ")

print(q.read())

