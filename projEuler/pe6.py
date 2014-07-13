#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

square_sum = 0
sum_square = 0
for i in range (101):
    square_sum += i
    sum_square+=(i*i)
square_sum*=square_sum
print (square_sum - sum_square)
        

    
