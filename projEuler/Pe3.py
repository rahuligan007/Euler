#finds the greatest prime factor of 600851475143
import math
# this way is slow
class Slow ():
    #find all the factors of number^
    def factorGen(self, num):
        i = 2
        while i<math.sqrt(num) : #we would have already checked all factors greater than math.sqrt(num)
            if num%i==0:
                checkPrime(num/i)
                checkPrime(i)
    #check if the factor is prime
    def checkPrime(f):
        prime = True
        for j in range(2,int(math.sqrt(i))):
            if i%j==0:
                prime= False
                break #breaks out of the for loop
        if prime:
            print (i)
#this way is hella fast, works kind of like a factor tree
# you divide the number by the smallest prime number that it is divisible by
#, if it's
# divisible, you take the quotient and you divide that by the smallest
# prime # that can divide into the quotient. along the way, you keep
# track of the greatest prime factor.
class Fast ():
    def getAnswer(self, num):
        newnumm=num
        counter = 2;  
        while counter * counter <= newnumm:
            if newnumm % counter == 0 :
                newnumm = newnumm / counter
                largestFact = counter
            else:
                counter+=1
        if newnumm > largestFact: # the remainder is a prime number
            largestFact = newnumm
        print (largestFact)

if __name__=="__main__":
    run = Fast()
    run.getAnswer(600851475143)
    #run = Slow()
    #run.factorGen(600851475143)
