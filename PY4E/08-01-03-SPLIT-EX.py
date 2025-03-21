print("Let's do some splitting")
fhand=open("mbox-short.txt")
for line in fhand:
    line=line.rstrip()
    if not line.startswith("From "):continue
    words=line.split()
    print(words[2])
print("New splitting:double one, yo extract domain in email address:")
print("\n\n---------------------------------------------------------")
print("\n\n111111111111111111111111111111111111111111111111111111111")
fhand.seek(0)
for line in fhand:
    line=line.rstrip()
    if not line.startswith("From "):continue
    words=line.split()
    email=words[1]
    pices=email.split("@")
    domain=pices[1]
    print(domain)
print("\nAnotherway")
print("\n\n---------------------------------------------------------")
print("\n\n222222222222222222222222222222222222222222222222222222222")
fhand.seek(0)
for line in fhand:
    line=line.rstrip()
    if line.startswith("From "):
        words=line.split()
        email=words[1]
        pieces=email.split("@")
        domain=pieces[1]
        print(domain)
print("\nAnotherway")
print("\n\n---------------------------------------------------------")
print("\n\n333333333333333333333333333333333333333333333333333333333")
fhand.seek(0)
for line in fhand:
    line=line.rstrip()
    words=line.split()
    #guardian in a compoud state -
    if len(words)<3 or words[0] != "From":
        continue
    email=words[1]
    pieces=email.split("@")
    domain=pieces[1]
    print(domain)
