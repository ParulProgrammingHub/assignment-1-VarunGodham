#enter marks of 5 subjects and find the mean of 5 subjects, calculate percentage. If percentage is less than 35 print fail else print pass.
maths=input("Marks Obtained in maths")
mi=input("Marks Obtained in mi")
py=input("Marks Obtained in Python")
dbms=input("Marks Obtained in dbms")
co=input("Marks Obtained in co")
total = maths + mi + py + dbms + co
avg= total/5.0
print "The mean is %s" % (avg)
per=(total*100)/250
if per<=35 :
    print "YOU HAVE FAILED THE EXAM AND YOU HAVE SCORED %s PERCENTAGE" % (per)

else :
    print "CONGRATULATIONS !!!!! YOU HAVE PASSED THE EXAM AND YOU HAVE SCORED %s PERCENTAGE" % (per)
