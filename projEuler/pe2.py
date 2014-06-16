#finds the sum of all the fibonacci #'s from 1-4,000,000 that are even.

from Pe1 import * # imports everything from the Pe1 file

class Pe2 (Pe1):
    def __init__(self, bottom, top):
        super(Pe2,self).__init__(bottom, top) #calls the super constructor

    def findNums(self):
        f1 = 1
        f2 = 2
        while f2 < self.top: # need colon for while and if's
            if f2%2 ==0:
                self.rage.append(f2)
            temp = f2
            f2 = f1 + f2
            f1 = temp

if __name__=="__main__":
    run = Pe2(0,4000000)
    run.findNums()
    run.addNums() #calls addNums in the Pe1 class
    
    
