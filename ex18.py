#This one is like your scripts with argv
def print_two(*args):
    argv1, argv2 = args
    print "arg1: %r, arg2: %r" % (argv1, argv2)
    
#Using (argv1, argv2) instead of (*args)
def print_two_again(argv1, argv2):
    print "arg1: %r, arg2: %r" % (argv1, argv2)
    
#only one argv
def print_one(argv1):
    print "arg1: %r" % argv1
    
#No argv
def print_none():
    print "I have nothing."
    
print_two("Minh", "Dang")
print_two_again("Same", "Thing")
print_one("Python")
print_none()
