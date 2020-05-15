class Test:
    #The __new__ method is called by the Test.__class__.__call__(Test,*args,**kwargs)
    def __new__(cls,*args,**kwargs):
        print("Creating instance!")
        #__new__ is responsible for creating the instance of the class Test wich will be used in __init__ constructor
        #Starting from python 3.3+ we can't pass any extra arguments to the object if we are overriden the __init__ and __new__ method
        instance = super().__new__(cls)

        return instance

    def __init__(self,num1,num2):
        print("Initializing the attributes!")
        self.sum = num1+num2
 



if __name__ == '__main__':
    test = Test(10,15)
    print("Sum Attribute: %d " %test.sum)

    print('-------------------------------------------')

    test2 = Test.__class__.__call__(Test,10,10)
    print("Sum Attribute: %d " %test2.sum)
    