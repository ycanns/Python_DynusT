#Day8________ Read a file

## INITAILIZATION
# Reading Vehicle trajectory file and Exporting for analysis
f=open("E:\\Research\\DynusT_Learning\\VA_Assgn_Testing\\UE_5iter_500min\\VehTrajectory.dat","r")
s=open("E:\\Research\\DynusT_Learning\\VA_Assgn_Testing\\UE_5iter_500min\\YC.csv","a+")

#f=open("E:\\Research\\DynusT_Learning\\VA_Newtork\\VehTrajectory.dat","r")
#s=open("E:\\Research\\DynusT_Learning\\VA_Newtork\\YC.csv","a+")

print ('______________ Vehicle Travel Information Extracting Start ______________')

# Skip first five lines
for i in range(0,5):
	f.readline()

# Creating Each Column name
s.write('Vehicle_ID')	# Vehicle ID
s.write(',')
s.write('Origin') 	# Origin
s.write(',')
s.write('Destination') 	# Destination
s.write(',')
s.write('Departure_Time') 	# Vehicle's departure time in system clock
s.write(',')
s.write('Total_Travel_Time') 	# Total Travel Time
s.write(',')
s.write('#_of_Nodes') 	# Number of nodes in the vehicle's path
s.write('\n')

Counts=0
Total_TT=0

# Code Start
while 1:

	# read line by line
	Tj=f.readline().split()
	
	# Insert a break, when file reading is done
	if Tj==[]:
		break

	# Finding a condition to extract information
	if Tj[0]=='Veh':
		#print('going on..')
		s.write(Tj[2])	# Vehicle ID
		s.write(',')
		s.write(Tj[6]) 	# Origin
		s.write(',')
		s.write(Tj[8]) 	# Destination
		s.write(',')
		s.write(Tj[18]) 	# Vehicle's departure time in system clock
		s.write(',')
		s.write(Tj[22]) 	# Total Travel Time
		s.write(',')
		s.write(Tj[26]) 	# Number of nodes in the vehicle's path
		s.write('\n')
		Counts=Counts+1
		Total_TT=float(Total_TT)+float(Tj[22])

# Closing all opened files	
f.close()
s.close()
print ('______________ All Processing End ______________')
print '1. Total generated vehicles : ', Counts
print '2. Total travel time : ', Total_TT, 'mins'
print '3. Average travel time : ', Total_TT/Counts, 'mins'

