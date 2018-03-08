#Day2________ operation and simple grammar

# Check reserved keywords
import keyword
keyword.kwlist

# Continuous lines --> \
# ex)
if (a==1) and \
	(b==j):
# They consider two lines as a single line with \

# Assign
c,d=3,4
x=y=z=0

# Assign differently in the same line ;
e=3.5; f=5.6

# Exchaning two values
e,f=f,e

# Check variable type
a=1
type(a)

a='dynamic'
type(a)

# Object replacement
X=[1,2,3]
Y=[10, X, 20]
Z=['a',X,'b']
X[1]=1000	# Check X, Y, Z then



# Data managing
s='Hello World!'
s[0]
s[1]
s[-1]
s[-2]
s[1:3]
s[0:5]
s[1:]
s[:3]
s[:]
s[::2]	# Two space baed printing (odd)
s[::-1]	# Reversing print

# Length of variable
len(s)