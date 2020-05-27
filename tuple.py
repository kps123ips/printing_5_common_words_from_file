file=open('mbox-short.txt')
counts=dict()
for line in file:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1

list=list()
for key,val in counts.items():
    newtuple=(val ,key)
    list.append(newtuple)

list=sorted(list,reverse=True)
for val,key in list[:5]:
    print(key,val)
