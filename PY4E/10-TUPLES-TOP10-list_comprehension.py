myfile = input("Chose your file: ")
fhand = open(myfile)
counts = dict()
for line in fhand :
    l = line
    wrds = l.split()
    for wrd in wrds :
        counts[wrd] = counts.get(wrd, 0) + 1

print( sorted( [(v,k) for k,v in counts.items()], reverse=True )[:10] )

print('\n'.join(f"{v} {k}" for v, k in sorted( [(v,k) for k,v in counts.items()], reverse=True)[:10] ) )

print('**'.join(f"{k} {v}" for v, k in sorted( [(v,k) for k,v in counts.items()], reverse=True)[:10] ) )

#for v,k in c_rrc[:10] :
    #print(k,v)
