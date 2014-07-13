#finds the greatest prime factor of 600851475143
import math
# this way is slow
class Pe3Slow ():
    #find all the factors of number^
    def factor_gen(self, num):
        i = 2
        while i<math.sqrt(num) : #we would have already checked all factors greater than math.sqrt(num)
            if num%i==0:
                check_prime(num/i)
                check_prime(i)
    #check if the factor is prime
    def check_prime(f):
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
class Pe3Fast ():
    def get_answer(self, num):
        newnum=num
        counter = 2;  
        while counter * counter <= newnum:
            if newnum % counter == 0 :
                newnum = newnum / counter
                largest_fact = counter
            else:
                counter+=1
        if newnum > largest_fact: # the remainder is a prime number
            largest_fact = newnum
        print (largest_fact)

if __name__=="__main__":
    run = Pe3Fast()
    run.get_answer(600851475143)
    #run = Slow()
    #run.factor_gen(600851475143)
