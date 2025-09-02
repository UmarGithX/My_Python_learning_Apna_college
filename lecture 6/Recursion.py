def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)

show =5

print()

def num(n):
    if(n==0):
        return 
    print(n)
    num(-1)
    
num(5)