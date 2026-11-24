import amstrong

lower = int(input("Enter lower limit: "))
upper = int(input("Enter upper limit: "))

print("Armstrong numbers are:")

for i in range(lower, upper + 1):
    if amstrong.isarmstrong(i):
        print(i)

