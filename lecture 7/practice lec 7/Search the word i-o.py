# Search if the word "learning" exists in the file or not.
def Word_finder():
    w="like"
    with open('sampler.txt','r') as a:
        data = a.read()
        # print(data)
    if(data.find(w) != -1):
        print('find')
    else:
        print('not find')
        
        
Word_finder()