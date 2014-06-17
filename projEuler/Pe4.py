"""A palindormic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009,
which is 91 times 99 . Find the largest palindrome made from the product of
two 3-digit numbers.
"""
class Brute():
    def bruteForce(self):
        largestProduct = 0;
        for i in range (100,1000):
            for j in range (100,1000):
                product = str(i*j) # converting from int to string
                for index in range(len(product)):
                    if not product[index] == product[len(product)-1-index]:
                        product=0
                        break
                if not product == 0:
                    if largestProduct< int(product): # string to int
                        largestProduct = product
        print (largestProduct)
if __name__=="__main__":
    run = Brute()
    run.bruteForce()
