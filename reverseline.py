file=open('she.txt','r')
rev=file.readlines()
t=reversed(rev)
for i in t:
    print(i[::-1])
    # print(i)
file.close()