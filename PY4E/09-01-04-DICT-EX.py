selected_file=input('Chose your file: ')
fhandle=open(selected_file)

counts=dict()
for line in fhandle:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1

maxcount=None
maxword=None
for key,value in counts.items():
    if maxcount is None or value>maxcount:
        maxcount=value
        maxword=key

print(f"The number of instances of the word \"{maxword}\" are: {maxcount}")

counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
    if counts[key] > 10:
        print(key, counts[key])
