the_num = None
counter = 0
sum = 0.0
while the_num != "done":
    the_num=input("Enter a number: ")
    try:
        the_num=float(the_num)
    except:
        if the_num != "done":
            print("Bad data")
        continue
    sum = sum + the_num
    counter = counter+1
    print("ok")
print("Well done!")
print("Total inputs (valid!) = ", counter)
print("Sum of the inputs = ", sum)
try:
    print("Avarage = ", sum/counter)
except:
    print("Avarage = None")

num = 0
tot = 0.0
while True :
    sval = input("Enter a number: ")
    if sval == "done" :
        break
    try:
        fval = float(sval)
    except:
        print("Invalid input")
        continue
    num = num +1
    tot = tot + fval
print(tot,num,tot/num)
