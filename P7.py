#program to calculate third angle using function
angle1=input("Enter the 1st angle")
angle2=input("Enter the 2nd angle")
def thirdangle(angle1,angle2):
    angle=180-(angle1+angle2)
    return  angle
print "The third angle is %s" % thirdangle(angle1,angle2)

