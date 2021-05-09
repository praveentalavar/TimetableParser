def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text

def expand_week(inp):
    l=[]
    dfl=[]
    for i in inp:
        if len(i)>=1:
            for j in i.split(','):
                if "-" in j and j is not None:
                    # Splitting 'x-y' type data to full range
                    k=map(str,[*range(int(j.split("-")[0]),int(j.split("-")[1])+1,1)])
                    l.extend(k)
                else:
                    l.append(j)
            dfl.extend(l)
            dfl.extend("#")
            l.clear()

    str1=""
    ll=[]
    for i in range(0,len(dfl)):
        if dfl[i] != "#":
            str1 = str1+","+dfl[i]
        else:
            ll.append(str1)
            str1= ""
    
    update = [e[1:] for e in ll]
    
    return update