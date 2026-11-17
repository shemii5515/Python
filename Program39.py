def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

n = int(input("Enter the number of integers: "))

numbers = []

for i in range(n):
    num = int(input("Enter a number: "))
    numbers.append(num)

result = add(*numbers)

print("Sum =", result)

