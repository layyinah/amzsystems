def prog(p):
    freq = {}
    py=['print','numpy','yield']
    c=['printf','scanf','getchar']
    dic={'python':0,'c':0}
    words=open(p).read().split()
    for w in words:
        freq[w]=freq.get(w,0)+1
    result=freq.items()
    for i in result:
        pyprog=i[0] in py
        cprog=i[0] in c
        if(pyprog == True):
            dic['python']=dic.get['python',0]+1;
        elif(cprog == True):
            dic['c']=dic.get['c',0]+1;
    if(dic['python']== 0):
        print("it is python program file")
    else:
        print("it is a c program file")



