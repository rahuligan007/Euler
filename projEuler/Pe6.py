#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

squarinSum = 0
sumSquare = 0
for i in range (101):
    squarinSum += i
    sumSquare+=(i*i)
squarinSum*=squarinSum
print (squarinSum - sumSquare)
        

    
