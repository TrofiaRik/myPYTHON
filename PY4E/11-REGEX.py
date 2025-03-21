# SEARCH --> RETURN TRUE/FALSE
#for+if
# fhand = open('mbox.txt')
# for line in fhand :
#     line = line.rstrip()
#     if line.find('From: ') >= 0 :   # FIND
#         print(line)
# fhand.seek(0)
# for line in fhand :
#     line = line.rstrip()
#     if line.startswith('From: ') :  # STARTSWITH
#         print(f'***startswith*** {line}')
# fhand.seek(0)
#with re module
import re
fhand = open('mbox-short.txt')
# for line in fhand :
#    line = line.rstrip()
#    if re.search('From: ', line) :  # RE SEARCH.
#        print(f'*** {line}')
# fhand.seek(0)
for line in fhand :
    line = line.rstrip()

    if re.search('^X.*:', line) : # RE SEARCH. WITH SOME REGEX INSIDE
        print(f'*** ^X.*: *** {line}')

    if re.search('^X-\S+:', line) :
        print(f'*** ^X-\S+: *** {line}')
#findall --> RETURN THE STRING
# GREEDY AND NOT-GREEDY
x = 'From: Using the : character'
greedy = re.findall('^F.+:', x) # ^(start with)F(letter F).(followed by any single character)+(Followed by one or more instances of ANY character):(ending with :)
print(greedy) #greedy, * and + --> chooses always the longest available string is more options are available
not_greedy = re.findall('^F.+?:', x)
print(not_greedy) # the ? tells our regex not to be greedy

y = 'From gionna@ucla.ca.us Sat Jan'

extr = re.findall('\S+@\S+', y)
print(extr)

ex2 = re.findall('^From (\\S+@\\S+)', y) #Parenthesis = start your extraction and end your extraction
print(ex2)

# rememver we can always use also the double split
wrds_sp1 = y.split()
sel = wrds_sp1[1]
wrds_sp2 = sel.split('@')
host = wrds_sp2[1]
print(host)

# and now let's try regex
host_re = re.findall(r'@([^ ]*)', y)
print(host_re)

# or, if I want to select only some lines with From
host_re2 = re.findall(r'^From .*@([^ ]*)', y)
print(host_re2)

# experiment searching for the number in lines like X-DSPAM-Confidence: 0.8475
fhand = open('mbox.txt')
nums_list = list()
for line in fhand :
    mysearch = re.findall(r'X-DSPAM-Confidence: ([0-9.]+)', line)
    #if len(mysearch) != 1 : continue
    if not mysearch : continue # if not means false --> if the mysearch is an empty list=no matches, then it returns false
    val = float(mysearch[0])
    nums_list.append(val)
print(f'Max X-DSPAM-Confidence: {max(nums_list)}')

#EX of escaping special characters
str = 'I have $12.436,26 in my bank account'
match = re.findall(r'\$[0-9,.]+', str)
print(match)
