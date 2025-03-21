#Use modified version of do_twice to call print_twice TWICE, passing 'spam' as an arguments
#Mod version of do_twice
def do_twice(func, arg):
    func(arg)
    func(arg)

#new print_twice func
def print_twice(arg):
    print(arg)
    print(arg)

#use do_twice
do_twice(print_twice, "spam")
