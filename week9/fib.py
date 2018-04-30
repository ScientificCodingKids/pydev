# compute i-th Fibonacci number in the series
# https://en.wikipedia.org/wiki/Fibonacci_number

def fibonacci(i):
    if i == 1:
        return 1
    if i == 2:
        return 1
    else:
        return fibonacci(i-1) + fibonacci(i-2)


if __name__ == "__main__":
    print(fibonacci(10))
    #print(fibonacci(10000)) this will blow up the stack
    #note that we do expect computer can help us to compute Fibonacci numbers with very large i
    #we will learn a better way to compute down the road