# enter value in centimetre and convert it to meter and kilometre.
cm=input("Enter the value in CENTIMETER")
m= float (cm/100)
km= float (m/1000)
choice = input("""Enter 1 to convert in METER
and  2 to convert in KILOMETER""")
if choice ==1:
    print "The Distance in METER is %s" % (m)
elif choice ==2:
    print "The Distance in KILOMETER is %s" % (km)
else:
    print "Enter the valid Choice"
    
