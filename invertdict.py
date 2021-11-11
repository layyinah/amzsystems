def invertdict(d):
    d={value:key for key , value in d.items()}
    return d
print("invert dictionary key and value \n", invertdict({'x': 1, 'y': 2, 'z': 3}))