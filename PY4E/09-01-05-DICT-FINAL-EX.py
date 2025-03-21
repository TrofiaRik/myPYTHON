# 1 # SELECTING AND OPENING A FILE
fname=input("Enter the filename: ")
if not fname : fname="clown.txt" #Creating a 'default'
fhand=open(fname)
#print(fhand) #CHKR

# 2 # CREATING THE Dictionary TO BE FILLED
di=dict()

# 3 # LOOPING THROUGH THE FILE lines
for lin in fhand:
    lin=lin.rstrip()
    #print(lin) #CHKR
    wds=lin.split()
    #print(wds) #CHKR

# 4 # THIS FOR LOOP PLUS THE IF IS checking/inserting/adding TO OUR Dictionary
    for w in wds:
        # ***BETTER CHOICE*** IDIOM->CHECK/CREATE/UPDATE Dictionary(COUNTER)
        di[w]=di.get(w,0)+1 #check, assign 0 if w is missing
        #print(f'* {w} {di.get(w,0)-1} +1 --> {di[w]}') #CHKR

        # ***MORE VERBOSE, a standard if else clause
        #if w in di:
        #    di[w]+=1
        #    print(f'"{w}" +1 --> {w}={di[w]}') #CHKR
        #else:
        #    di[w]=1
        #    print(f'"{w}" is **NEW** --> {w}={di[w]}') #CHKR
#print(di) #CHKR

# 5 # LET'S FIND THE MOST COMMON WORD in our Dict
hival=0
hwd=None
for k,v in di.items():
    #print(k,v) #CHKR
    if v > hival:
        hival=v
        hwd=k
print(f'Reading the file "{fname}".\n ***DONE***\n The most common word is "{hwd}", appearing {hival} times')
