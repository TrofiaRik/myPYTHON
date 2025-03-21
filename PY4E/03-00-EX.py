#03-00-EX
rawstr = input("Enter a number: ")
try:
    ival = float(rawstr)
except:
    ival = None

if ival is not None:
    if ival >= 0:
        print("Nice work")
    else:
        print("Nice work, but number is negative")
else:
    print("Not a number")

rawstr = input("Enter a number: ")
try:
    ival = float(rawstr)
    print("Nice work")
except:
    print("Not a number")
