import datetime

year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

date = datetime.datetime(year, month, day)

print("Date:", date)
print("Year:", date.year)
print("Month:", date.month)
print("Week number:", date.strftime("%U"))
print("Weekday:", date.weekday())
print("Day of the year:", date.strftime("%j"))
print("Day of the month:", date.day)
print("Day of the week:", date.strftime("%A"))

