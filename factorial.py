def factorial(n):
    if(n == 0):
        return 1
    i= n
    f=1
    while(n/i != n):
        f=f*i
        i-=1
    return f
num=int(input("enter the number : "))
print("factorial of number is", factorial(num))