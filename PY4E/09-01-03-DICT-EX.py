print("-----------------------------------------------------------------------------")
print("A simple program for counting frequency of inputted words")
print("-----------------------------------------------------------------------------\n")
print("Using the FOR LOOP + the get method \n")
counts=dict()
print("Insert one or more lines of text below:")
text=input("")
words=text.split()
for word in words:
    counts[word]=counts.get(word, 0)+1
    mymax=max(counts)
print(counts)
print(f'My max is {mymax}\n')
print("-----------------------------------------------------------------------------")
print(" - 1 - Look inside a formed 'counts' Dictionary")
print("-----------------------------------------------------------------------------\n")
counts={'jack':1, 'tom':10, 'glen':12, 'dave':3}
for key in counts:
    print(key,counts[key])
    print('\n')
print("-----------------------------------------------------------------------------")
print(" - 2 - Let's experiment out some methods to extract the data from the Dict.")
print("-----------------------------------------------------------------------------\n\n")
print("- a - Convert to list and print -> getting a list of the keys")
print("-----------------------------------------------------------------------------")
print(list(counts),'\n')
print('- b - Using the \'keys\' method -> extracting keys')
print("-----------------------------------------------------------------------------")
print(counts.keys(),'\n')
print("__________")
print("__________Print using list, print(list(counts.keys()))")
print(list(counts.keys()),'\n')
print("__________")
print("__________Print using the for loop, for item in counts.keys(): print(key)",'\n')
for key in counts.keys():
    print(key)
print('\n')
print("__________")
print("__________Print using the join method")
print(" ".join(counts.keys()))            # 'a b c'
print('\n')
print("__________")
print("__________Print using the join+map+str method")
print(" ".join(map(str, counts.values()))) # '1 2 3'
print('\n')
print('- c Using the \'values\' method -> extracting the values')
print("-----------------------------------------------------------------------------")
print(counts.values(),'\n')
print("__________")
print("__________Print using list, print(list(counts.values()))")
print(list(counts.values()),'\n')
print("__________")
print("__________Print using the for loop, for item in counts.items(): print(item)",'\n')
for val in counts.values():
    print(val)
print('- d - Using the \'items\' method -> extracting the pairs keys+values - N.B. RETURNING OUR FIRST TUPLE')
print("-----------------------------------------------------------------------------")
print(counts.items(),'\n')
print("__________")
print("__________Print using list, print(list(counts.items()))")
print(list(counts.items()),'\n')
print("__________")
print("__________Print using the for loop, for item in counts.items(): print(item)",'\n')
for item in counts.items():
    print(item)
print("__________")
print("__________VERY COOL - ONLY POSSIBLE IN PYTHON - Print using the for loop and the double parameter",'\n')
for key,value in counts.items():
    print(key,value)
