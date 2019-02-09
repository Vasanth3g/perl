class vasanth():
    def __init__(self,friend,friend1,friend2):
        self.friend = friend
        self.friend1 = friend1
        self.friend2 = friend2
    def math(self,maths_op,*args):
        print ("%s performed math operations and result is %f: " % (self.friend,maths_op(*args)))

def add (a,b):
    return a + b
vasanth_friends = vasanth("Mahender" , "raja", "satheesh")
#print (vasanth_friends.friend)
vasanth_friends.math(add,35,40)
