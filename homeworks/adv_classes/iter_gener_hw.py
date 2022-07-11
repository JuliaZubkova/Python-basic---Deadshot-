# 1. Implement class iterator for Fibonacci numbers https://en.wikipedia.org/wiki/Fibonacci_number
# Iterator get numbers of first Fibonacci numbers

class FibonacciNumbers:
    def __init__(self, counter):
        self.counter = counter
        self.first = 0
        self.second = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == 0:
            raise StopIteration
        self.counter -= 1
        number = self.first
        self.first, self.second = self.second, self.first + self.second
        return number

for i in FibonacciNumbers(10):
    print(i)
# 0 1 1 2 3 5 8 13 21 34

# 2. Implement generator for Fibonacci numbers

def fibonacci_generator(counter):
    first, second = 0, 1
    while counter != 0:
        yield first
        counter -= 1
        first, second = second, first + second

for k in fibonacci_generator(10):
    print(k)
# 0 1 1 2 3 5 8 13 21 34

# 3. Write generator expression that returns square numbers of integers from 0 to 10

def square(length):
    for l in range(length):
        yield l ** 2

for j in square(11):
    print(j)
# 0 1 4 9 16 25 36 49 64 81 100

# 4.Implement coroutine for accumulation arithmetic mean

def accumulation_mean():
    count = 1
    total = yield
    while True:
        average = total / count
        count += 1
        total += yield average

ac_mean = accumulation_mean()
next(ac_mean)
print(ac_mean.send(2))   # 2.0
print(ac_mean.send(8))   # 5.0
print(ac_mean.send(2))   # 4.0
print(ac_mean.send(4))   # 4.0