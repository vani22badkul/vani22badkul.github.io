
def most_frequent (s):
    d=dict()
    for i in s:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    return d
print(most_frequent('Mississippi'))
    
