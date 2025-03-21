found = False
print("Before", found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
        #print(found, value) #option of 'early break'
        #break               #option of 'early break'
    else:
        found = False
    print(found, value)
print("After", found)
