import sys

class Test:
    def __init__(self,number1,number2):
        print("Object created!")
        self.sum=number1+number2

    #__del__ method is a finalizer that will be call when a object is deleted
    #This could happen  in the possible situations:
    # - In the end of the script (garbage collector)
    # - After a "del instance" call
    # - If the instance is a local variable and the function end
    def __del__(self):
        print("Deleting the instance!")
        

if __name__ == '__main__':

    if sys.argv[-1] == "before":
        test = Test(1,2)
        print("Sum Attribute: %d " %test.sum)
        del test
        print("-----------------------------------")
        print("End of the program")
    else:
        test = Test(1,2)
        print("Sum Attribute: %d " %test.sum)
        print("-----------------------------------")
        print("End of the program")



    