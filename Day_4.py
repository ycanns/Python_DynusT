# Day3________ if-elif-else control

# check data type
a=0
L=[1,2,3]
type(a)==type(0)	# integer?
type(L)==type([])	# list?

# Data check 
a=[1,2,3]
b=[1,2,3]
a == b


# if control
if condition1:
	expression1
elif condition2:
	expression2
else:
	expression3

# ex1
n=-2
if n>0:
	print 'Positive'
elif n<0:
	print 'Negative'
else:
	print 'Zero'

# ex2
order='Americano'
if order=='Latte':
	price=6
elif order=='water':
	price=1
elif order=='smoody':
	price=4
elif order=='Americano':
	price=3

# or use dictionary function
menu={'Latte':6, 'water':1, 'smoody':4, 'Americano':3}
price=menu[order]