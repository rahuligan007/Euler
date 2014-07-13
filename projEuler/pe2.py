#finds the sum of all the fibonacci #'s from 1-4,000,000 that are even.

class Pe2Fast():
    def fib(self, max): # this is a generator
        f1, f2 = 0, 1
        while f1 < max:
            yield f1 #returns f1
            f1, f2 = f2, f1 + f2
if __name__ == "__main__":
    problem = Pe2Fast()
    print(sum(filter(lambda n: n % 2 == 0, problem.fib(4000000))))
#fib(4,000,000) returns a list of all fibonnacci #'s
#then we filter the list, keeping all values n where n%2==0
#take sum of all that

#linear time solution below
"""
from Pe1 import * # imports everything from the Pe1 file

class Pe2 (Pe1):
    def __init__(self, bottom, top):
        super(Pe2,self).__init__(bottom, top) #calls the super constructor

    def find_nums(self):
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
    run.find_nums()
    run.add_nums() #calls addNums in the Pe1 class
    
    
"""
