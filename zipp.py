def zip_fun(n,a):
#     res=zip(n,a)
#     print(list(res))
    [print(n,a) for n,a in zip(n,a)]
zip_fun([1,2,3,4],["a","b","c","d"])