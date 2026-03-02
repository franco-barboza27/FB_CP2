# Factorial example
def factor(num):
    if num == 1: return 1
    return num * factor(num-1)

print(factor(5))

num = 5
factor = 1

while num > 0:
    factor *= num
    num -=1

print(factor)

# Fibonacci sequence example

number = 10
sequence = [1, 1]

for i in range(1, number):
    sequence.append(sequence[i] + sequence[i-1])

print(sequence)


rec_sequence = []
def fibonacci(n):
    if n == 1:
        return 1  
    elif n == 2:
        return 1
    else:
        # rec_sequence.append(rec_sequence[fibonacci(n)] + rec_sequence[n-1])
        return(fibonacci(n-1) + fibonacci(n-2
                                          ))

print(fibonacci(10))