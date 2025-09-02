# WAF to find the factorial of n. (n is the parameter)

n= 5
def factorial_Finder(n):
    fac = 1
    for i in range(1,n+1):
        fac *=i
    print(fac)
    
factorial_Finder(10)
