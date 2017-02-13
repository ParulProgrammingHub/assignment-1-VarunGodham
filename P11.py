#Calculate Compound Interest Using Function compound_interest(principal,time,rate)
p=int(input('Enter The Principal Amount : '))
t=int(input('Enter Time In Years : '))
r=int(input('Enter The Interest Percentage : '))
def compound_interest(principal,time,rate):
    x=(1+(rate/100))**time
    interest_value=(principal*x-principal)
    return interest_value
print 'The Compound Interest Value is %f : '%compound_interest(p,t,r)
