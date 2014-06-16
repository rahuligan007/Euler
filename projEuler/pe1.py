#OOP version. this is considered pythonic, code this way

#finds the sum of all the numbers that are multiples of 5 or 3 in the range 1-1000

class Pe1(object): # Pe1 inherits everything from object class
    #rage, bottom and top are all global variables
    def __init__(self, bottom, top): # __init__ is the constructor
                                    # the parameters are always self and then anything else
                                    # self is the same thing as this in java
        self.bottom = bottom
        self.top = top
        self.rage = [5]*0
    def findNums(self): # finds all numbers that are multiples of 5 or 3 and stores it in rage
        print ("Swag")
       
        for i in range(self.top): #goes from 0-999
            if i%5==0 or i%3 ==0:
                self.rage.append(i)
    def addNums(self): #finds the sum of all numbers in the list and prints that
        print ("swag")
        sum = 0
        for i in self.rage:
            sum = sum + i
        print (sum)
    
    if __name__=="__main__": # = public static void main
        run = Pe1(0,1000)#you pass in a value for all parameters of the init except for self
                #you don't do anything for self
        run.findNums()
        run.addNums()
