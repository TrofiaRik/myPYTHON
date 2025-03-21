print("-----------------------------------------------------------------------------")
print("Using Dictionaries in order to count frequency of items, to produce histagrams")
print("-----------------------------------------------------------------------------\n")
print("Using the FOR LOOP + THE IF STATEMENTS \n")
counts=dict()
names=['QUI','QUO','QUA','QUI','QUO','QUI','QUA','QUO']
for name in names:
    if name not in counts:
        counts[name]=1
    else:
        counts[name]+=1
print(counts)

print("-----------------------------------------------------------------------------\n")
print("Now, just check if the name is present with IF BLOCK")
counts2=dict()
names=['QUI','QUO','QUA','QUI','QUO','QUI','QUA','QUO']
counts2['QUI']=1
for name in names:
    if name in counts2:
        x=counts2[name]
        print(x)
    else:
        x=0
        print(x)

print("-----------------------------------------------------------------------------\n")
print("And then, just check if the name is present with the GET METHOD")
counts2=dict()
names=['QUI','QUO','QUA','QUI','QUO','QUI','QUA','QUO']
counts2['QUI']=1
for name in names:
    x=counts2.get(name,0)
    print(x)

print("-----------------------------------------------------------------------------\n")
print("Using the FOR LOOP + get \n")
counts3=dict()
names=['QUI','QUO','QUA','QUI','QUO','QUI','QUA','QUO']
for name in names:
    counts3[name]=counts3.get(name,0)+1
print(counts3)
