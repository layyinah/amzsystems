import collections
from collections import counter
def dups(d):
    dp=counter(d)
    duplicate=list([x for x in d if d[x]>1])
    return duplicate
print("duplicate numbers is " , dups([1, 2, 1, 3, 2, 5]))
