import operator
dic={'x': 1, 'y': 2, 'a': 3}
print('dictionary :\n' ,dic)

def valuesort(v):
    sortv=sorted(dic.items(),key=operator.itemgetter(1),reverse=True)
    sortedvalue=dict(sortv)
    return sortedvalue
print("sorted dictionary by there value \n",valuesort({'x': 1, 'y': 2, 'a': 3}))

