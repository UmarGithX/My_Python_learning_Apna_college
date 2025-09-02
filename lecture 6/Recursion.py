def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)

show =5

print()

# Write a recursive function to calculate the sum of first n natural numbers.
def num(n):
    if(n==0):
        return 0 
    return num(n-1) +n
    
sum = num(5)
print(sum)