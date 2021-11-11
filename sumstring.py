def sumstring(str):
    for i in str:
        str.append(i)
    return str
print("sum of estrings \n",sumstring(["hello","world"]))