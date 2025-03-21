print("#0. Input and Convert")
name=input("Enter your name: ")
print(name)
#1 Simple Concatenation
print("#1. Simple Concatenation")
str1="ciao "
str2=name
print(str1 + str2)
#2 type conversion with "int" or "float"
print("#2 type conversion with \"int\" or \"float\"")
str3="123"
str3C=float(str3)
print(str3C+1)
#3 Indexes
print("#3 Indexes")
fruit="banana"
str0=fruit[1]
print(str0)
#4 "len()"
print("#4 \"len()\"")
car="lamborghini"
print(len(car))
#5 looping with "while"
print("#5 looping with \"while\"")
i=0
fruit="banana"
while i<len(fruit):
    letter=fruit[i]
    print(i,letter)
    i=i+1
#6. looping with "for", for maximum elegance and conciseness
print("#6 looping with \"for\", for maximum elegance and conciseness")
word="banana"
index=0
for i in word:
    print(index,i)
    index=index+1
print("#7 Looping and counting")
wrd="califragilistichespiralidoso"
count=0
for i in wrd:
    if i=="l":
        count=count+1
print(count)
