#Copy and test the functions
def do_twice(f):
    f()
    f()

def print_spam():
    print("spam")
 
do_twice(print_spam)
