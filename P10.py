#Calculate Simple Interest Using Function simple_interest(principal,time,rate)
p=int(input('Enter The Principal Amount : '))
t=int(input('Enter Time In Years : '))
r=int(input('Enter The Interest Percentage : '))
def simple_interest(principal,time,rate):
    interest_value=(principal*time*rate)/100
    return interest_value
print'The Simple Interest Value is :%f '%simple_interest(p,t,r)
