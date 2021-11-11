
# def even(x):
#     return x % 2 == 0
#
# result=filter(even,range(10))
# print("result is :" ,list(result))

#

res=filter(lambda x:x % 2 == 0 ,range(10))
for i in res:
    print("result is :", list(i))
