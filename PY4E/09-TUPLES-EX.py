print("Here are some TUPLES")
tup1='a',
tup2='a','b','c'
tup3=('a','b','c')
print(f"tup1='a', --> {type(tup1)}")
print(f"tup2='a','b','c' --> {type(tup2)}")
print(f"tup3=('a','b','c') --> {type(tup3)}")

print('SORTING LISTS OF TUPLES INSIDE DICTIONARIES')
mydict={'a':10, 'z':63, 'b':4}
print(mydict.items())
print(sorted(mydict.items()))
