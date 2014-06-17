#What is the smallest positive number that is evenly divisible (divisible with no remainder) by all of the numbers from 1 to 20?

class Pe5 ():
    def brute (self):
        i=20
        while not (i%2==0 and i%3==0 and i%5==0 and i%7==0 and i%11==0 and i%13==0 and i%17==0 and i%19==0 and i%4==0 and i%9==0 and i%16==0):
            # only check if its divisible by primes and square of primes that are less than 20, then you get all possibilities
            i+=20 # add by 20's to save time
        print (i)


if __name__=="__main__":
    run = Pe5()
    run.brute()
