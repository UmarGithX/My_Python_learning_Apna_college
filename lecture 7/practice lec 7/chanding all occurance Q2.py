# change all the occurance
# Replace python with Java

with open('sampler.txt','r') as a:
    data = a.read()
    
or_data = data.replace('Java' , 'Python')
print(or_data)

with open('sampler.txt','w') as a:
    a.write(or_data) 