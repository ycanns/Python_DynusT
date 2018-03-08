#Day4________ for and while controls

# for control
for Target in object:
	expression1
else:
	expression2


# ex
a=['cat', 'cow', 'tiger']
for x in a:
	print len(x), x


# order based for control: range
for x in range(1,10):
	print x


# Use break and continue
for x in range(1,10):
	if x>4:
		break
	print x


for x in range(1,10):
	if x<4:
		continue
	print x

# Print in a single row
for x in range(1,10):
	print x,

# Creaet a multiplication
for i in range(1,10):
	for j in range(1,10):
		print i, '*', j, '=', i*j
	

# While control
while condition:
	expression1
else:
	expression2

# ex
count=1
while count<11:
	print count
	count=count+1


