myfile = input("Chose your file: ")
fhand = open(myfile)
counts = dict()
for line in fhand :
    l = line
    wrds = l.split()
    for wrd in wrds :
        counts[wrd] = counts.get(wrd, 0) + 1

#### --->>> REVERSE DICTIONARY ITEMS: create a list (my dict becomes a list), invert k,v with a for loop, creating tuples,appending tuples to list
rvrsd_counts = list()
for k,v in counts.items() :
    mytuple = (v,k)
    rvrsd_counts.append(mytuple)

rrc = sorted(rvrsd_counts, reverse=True )

for v,k in rrc[:10] :
    print(k,v)
