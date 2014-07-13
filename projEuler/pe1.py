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
    def find_nums(self): # finds all numbers that are multiples of 5 or 3 and stores it in rage
       for i in range(self.top): #goes from 0-999
            if i%5==0 or i%3 ==0:
                self.rage.append(i)
    def add_nums(self): #finds the sum of all numbers in the list and prints that
        total = 0
        for i in self.rage:
            total = total + i
        print (total)
    
if __name__=="__main__": # = public static void main
    run = Pe1(0,1000)#you pass in a value for all parameters of the init except for self
              #you don't do anything for self
    run.find_nums()
    run.add_nums()

"""
# don't code with global. code the OOP way


#finds the sum of all the numbers that are multiples of 5 or 3 in the range 1-1000

class Pe1Alt(object): # pe1 inherits everything from object class
    
    def find_nums(): # finds all numbers that are multiples of 5 or 3 and stores it in rage 
                    #you only need to say "global variable" when you are going to change the
                    #global variable in the method, you don't need it for just accessing.
        for i in range(1000): #goes from 0-999
            if i%5==0 or i%3 ==0:
                global multiples
                multiples.append(i)
    def add_nums(): #finds the sum of all numbers in the list and prints that
        sum = 0
        for i in multiples:
            sum = sum + i
        print (sum)
    multiples = [5]*0
    find_nums()
    add_nums()
"""
