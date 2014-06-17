class Brute():
    def bruteForce(self):
        largestProduct = 0;
        for i in range (100,1000):
            for j in range (100,1000):
                product = str(i*j)
                for index in range(len(product)):
                    if not product[index] == product[len(product)-1-index]:
                        product=0
                        break
                if not product == 0:
                    if largestProduct< int(product):
                        largestProduct = product
        print (largestProduct)
if __name__=="__main__":
    run = Brute()
    run.bruteForce()
