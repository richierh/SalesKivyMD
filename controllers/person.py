

class Person():

    def __init__(self,parent = None,*args):
        self.parent = parent
        self.argument = list(args)
        print (self.argument)




if __name__=="__main__":

    object1 = Person(None,"bb")
    print (object1)
