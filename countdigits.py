def countDigit(n):
    i=0
    while n != 0:
        n=n//10
        i= i+1
    return i
num=int(input("enter the number : "))
print("number of digits:", countDigit(num))