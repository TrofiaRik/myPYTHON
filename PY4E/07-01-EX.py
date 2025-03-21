from pathlib import Path
cdir=Path.cwd()
file=input("Chose your file: ")
try:
    fhand = open(file)
except:
    print("Cannot find the file",file,"in the current dir",cdir)
    quit()
count = 0 #line count, optional
for line in fhand:#line count, optional
    cline=line.upper().rstrip()
    count = count + 1#line count, optional
    print(cline)#line count, optional
print("Total number of lines for file",file,"=",count)#line count, optional
fhand.close()
