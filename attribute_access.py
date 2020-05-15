class Test:
    teste=5
    def __init__(self,number1,number2):
        print("Object created!")

        #To set this attribute, the __setattr__ will be called
        self.sum = number1+number2

        #setattr(self,'sum',number1+number2)

    #__getattribute__ will be called always that you try to access an attribute like (instance.atr)
    # - If the attribute doesn't exist, the method will raise an AttributeError
    def __getattribute__(self,atr):
        print("Get attribute by the __getattribute__ method!")
        #From the docs: In order to avoid infinite recursion in this method, its implementation should always call the base class method with the same name to access any attributes it needs
        return object.__getattribute__(self,atr)

        #Change the above return with the following:
        #return self.atr
        #Look what happen
    
    #__getatr__ will be called if you try to access an attribute that doesn't exist, in other words, always that the __getattribute__ raise an AttributeError
    def __getattr__(self,atr):
        print("The attribute doesn't exist!")

    
    #__setattr__ will be called always that you try to set an attribute like instance.attr=value or using te built in setattr() function
    def __setattr__(self,name,value):
        print("Set attribute by __setattr__ method!")
        #From the docs: If __setattr__() wants to assign to an instance attribute, it should call the base class method with the same name
        object.__setattr__(self,name,value)

        #Change the above return with the following:
        #self.name=value
        #Look what happen

    
    def __delattr__(self,name):
        print("Deleting an attribute")

        #This approach follow the same line of the docs to prevent infinite recursion
        object.__delattr__(self,name)
    
    


   

if __name__ == '__main__':
    print('---------------Existing Attribute---------------------')
    test = Test(10,15)
    print("Sum Attribute: %d " %test.sum)
    print('---------------Non Existing Attribute-----------------')
    #Trying access a non existing attribute
    test.random
    print('---------------Deleting the attribute-----------------')
    del test.sum

   

    