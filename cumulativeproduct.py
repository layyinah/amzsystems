def cumulativeprod(cp):
    i=1
    while(i<len(cp)):
        cp[i]=cp[i]*cp[i-1]
        i+=1
        return cp[i-1]
print("cumulative product is", cumulativeprod([10,20,30]))