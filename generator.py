#prints the first 3 squares
#EXAMPLE OF A GENERATOR
def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i*i
mygenerator = createGenerator() #function isn't run yet
for i in mygenerator: #accessing values of generator, the function runs now
    print (i)

print (mygenerator)

# when you call the function, the code you have written in the function body
#does not run. The function only returns the generator object.

#Then, your code will be run each time the for uses the generator.

# The first time the for calls the generator object created from your function,
#it will run the code in your function from the beginning until it hits yield,
#then it'll return the first value of the loop. Then, each other call will run
#the loop you have written in the function one more time, and return the next
#value, until there is no value to return.

#The generator is considered empty once the function runs but does not hit
#yield anymore. It can be because the loop had come to an end, or because you
#do not satisfy a "if/else" anymore.
