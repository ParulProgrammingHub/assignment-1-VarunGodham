#python program to enter value in days and convert in form of years, months and days.
n=input("Enter the no of days")
year= n/360 
num = n%360
month=num/30
days=num % 30
print "The no of year is %s" % (year)
print "The no of month is %s" % (month)
print "The no of days is %s" % (days)
