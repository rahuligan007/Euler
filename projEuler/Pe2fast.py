
class Pe2fast():
    def fib(max): # this is a generator
        f1, f2 = 0, 1
        while f1 < max:
            yield f1 #returns f1
            f1, f2 = f2, f1 + f2

print(sum(filter(lambda n: n % 2 == 0, fib(4000000))))
#fib(4,000,000) returns a list of all fibonnacci #'s
#then we filter the list, keeping all values n where n%2==0
#take sum of all that
