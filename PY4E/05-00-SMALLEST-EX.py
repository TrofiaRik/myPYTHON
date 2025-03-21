#My version, more concise and more pythonic
smallest_so_far=-1
index=0
print("Before", smallest_so_far)
for the_num in [9,41,12,3,74,15]:
    if smallest_so_far == -1 or smallest_so_far > the_num:
        smallest_so_far=the_num
    index=index+1
    print(index,smallest_so_far, the_num)
print("After", smallest_so_far)

#With None constant, which works great also with bigger_so_far
smallest_so_far=None
index=0
print("Before", smallest_so_far)
for the_num in [9,41,12,3,74,15]:
    if smallest_so_far == None or smallest_so_far > the_num:
        smallest_so_far=the_num
    index=index+1
    print(index,smallest_so_far, the_num)
print("After", smallest_so_far)

#With None constant and if + el if
smallest_so_far=None
index=0
print("Before", smallest_so_far)
for the_num in [9,41,12,3,74,15]:
    if smallest_so_far is None:
        smallest_so_far=the_num
    elif the_num < smallest_so_far:
        smallest_so_far=the_num
    index=index+1
    print(index,smallest_so_far, the_num)
print("After", smallest_so_far)
