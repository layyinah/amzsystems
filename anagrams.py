list=['eat', 'ate', 'done', 'tea', 'soup', 'node']
anagrams={}
for i in list:
    newlist=str(sorted(i))

    # print("sorted list \n" ,newlist)

    if newlist in anagrams:
        
        anagrams[newlist].append(i)
    else:
        print("no anagrams")
print(dict(anagrams.values()))