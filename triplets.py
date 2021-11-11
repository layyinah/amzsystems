def triplets(n):
    trip=[]
    res=0
    for t in n:
        for f in range(1,t//2+1):
            res=(f,t-f,t)
        return trip.append(res)

print("triplets from the list is \n",triplets([1,2,3,4,5,6,7,8,9,10]))