# don't code with global. code the OOP way


#finds the sum of all the numbers that are multiples of 5 or 3 in the range 1-1000

class pe1alt(object): # pe1 inherits everything from object class
    #rage
    
    def findNums(): # finds all numbers that are multiples of 5 or 3 and stores it in rage
        print ("Swag")
        #global rage 
        #rage = [5]*0 #resets the value of the list to nothing
                    #you only need to say "global variable" when you are going to change the
                    #global variable in the method, you don't need it for just accessing.
        for i in range(1000): #goes from 0-999
            if i%5==0 or i%3 ==0:
                global rage
                rage.append(i)
    def addNums(): #finds the sum of all numbers in the list and prints that
        print ("swag")
        sum = 0
        for i in rage:
            sum = sum + i
        print (sum)
    rage = [5]*0
    findNums()
    addNums()
