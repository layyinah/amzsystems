def cumulativesum(cs):
    i=1
    while(i<len(cs)):
        cs[i]=cs[i]*cs[i-1]
        i+=1
        return cs[i]
print("cumulative sum is", cumulativesum([1,2,3]))