from pathlib import Path
current_dir = Path.cwd()
file=input("Chose your file: ")
try:
    fhand = open(file)
except:
    print("File",file,"cannot be found in",current_dir)
    quit()
count=0
for line in fhand:
    count = count + 1
    #print(line)
fhand.seek(0) # Reset file pointer to the beginning
read = fhand.read()
print(read)
print("Total number of lines for file",file,"=",count)
print("Total number of characters is:",len(read))
print(read[:20])
fhand.seek(0)
for line in fhand:
    line = line.rstrip()
    if line.startswith("From:"):
        print(line)
fhand.seek(0)
for line in fhand:
    line = line.rstrip()
    if not "@uct.ac.za" in line:
        continue
    print(line)
fhand.seek(0)
scount=0
for line in fhand:
    if line.startswith("Subject:"):
        scount=scount+1
print("There were",scount,"subject lines in",file)
fhand.close()
