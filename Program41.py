n = int(input("Enter the number of terms: "))

power = lambda x: 2 ** x

for i in range(n):
    print("2^", i, "=", power(i))

