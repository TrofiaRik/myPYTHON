#1 Basic slicing
print("#1 Basic Slicing")
s="Monty Python"
print(s)
print(s[0:2])
print(s[0:100])
print(s[:])
print(s[:100])
print(s[0:])
print(s[2:7])
#2 Concatenation
print("#2 Concatenation...again - mind the space")
a="ciao"
b=a+" "+"ciao"
print(b)
print(a,a)
print("The result of the print 1 and 2 is the same: in the first concatenation, we added manually the space while in the second print statement we obtained the same result making use of the comma which inside print becomes a space ")
#3 In as a logical operator
print("\"IN\" as a logical operator")
end=0
while end == 0:
    fruit=input("Scegli il tuo frutto: ")
    if "a" in fruit:
        print("Ben fatto!")
        end=1
    else:
        print("Scegli meglio")
#4 String comparisons
print("#4 String comparisons")
word = ""
while word != "banana":
    word = input("Chose a word (but the right one is banana!)")
    if word == "banana":
        print("Ok Banana!")
    elif word < "banana":
        print("Your word",word,"comes BEFORE \"banana\"")
    elif word > "banana":
        print("Your word "+word+" comes AFTER \"banana\"")
#5 String Library
print("#5 String Library")
greet="Hello RICCARDO"
lowergreet=greet.lower()
print(lowergreet)
print(greet)
print("HI THERE!".lower())
print("Let's print the type, first, and then all the methods of the typw trught the \"dir\" function")
print(type(greet))
print(dir(greet))
print("Here it is a list of the most used in this course: ")
print("str.capitalize")
print("str.center")
print("str.endswith(suffix[, start[, end]])")
print("str.find(sub[, start[, end]])")
print("str.lstrip([chars])")
print("str.replace(old, new[, count])")
print("str.lower()")
print("str.rstrip([chars])")
print("str.strip([chars])")
print("str.upper()")
