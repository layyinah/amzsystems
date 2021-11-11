def valuesort(dictionary):
	return [dictionary[i] for i in sorted(dictionary.keys())]
print("sorted dictionary by there value \n",valuesort({'x': 1, 'y': 2, 'a': 3}))