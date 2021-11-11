def square(x):
    return (x*x)

def mapp(m):
    [m for m in map(square,range(5))]

print("square of first five sequence is \n " ,mapp(5))