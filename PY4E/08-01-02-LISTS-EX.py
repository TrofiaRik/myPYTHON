print("------")
print("Creating some lists and checking type and dir(methods)")
x=list()
y=[1,2,3,4,5,6,77,8,999]
print("Type of 'x' is:",type(x))
print("Type of 'y' is:",type(y))
print("Dir for 'x' is:",dir(x),"\n")
print("Dir for 'y' is:",dir(y),"\n")
print("----------")
print("Let's create am empty list and append elements to it!")
print("----------\n")
print("Using the 'constructor form' list()")
mystuff=list()
mystuff.append("book")
mystuff.append("pencil")
mystuff.append("pen")
print(mystuff,"\n")
mystuff.sort()
print(mystuff,"\n")
print("----------")
print("Two methods to acomplish the same results, with a 'pure' undetermined while loop, adn with list and methods")
print("One method makes calcs on the fly and does not store all the values, while the other keep the values and use more memory\n")
print("----------\n")
print("----------")
print("The while+variables method")
print("----------")
total=0
count=0
while True:
    inp=input("Insert a number to add: ")
    if inp=='XXX':break
    val=float(inp)
    count=count+1
    total=total+val
print(f"My total is {total} and my avarage is {total/count}\n" )
print("----------")
print("The while+list method")
print("----------\n")
mynumbers=list()
while True:
    inp=input("Insert a number to be added: ")
    if inp=="XXX":break
    val=float(inp)
    mynumbers.append(val)
print(f"The sum is {sum(mynumbers)} while the avarage is {sum(mynumbers)/len(mynumbers)}")
