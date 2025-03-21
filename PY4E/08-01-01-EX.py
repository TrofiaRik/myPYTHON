friends=['joseph','yeoshua','rachel']
for friend in friends:
    print(f"Hello my dear {friend}!")
print("Well done!")
print(friends[1])
print("LISTS ARE MUTABLE!")
fruit="Banana"
try:
    fruit[0]="b"
except:
    print("We were hit by a traceback! Not possible to do fruit[0]=\"b\"")
print("Let's try with a list:")
fruits=["Banana","mela","Pera"]
print(fruits)
fruits[1]="Mela"
fruits[1]=fruits[1].upper()
print(fruits)
print("Let's try \"len\"")
print(len(fruits))
for i in range(len(fruits)):
    print(fruits[i])
