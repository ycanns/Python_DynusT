# Day 10- CALCULATINON START FOR COUNTING PASSING VEHICLES
# 

def check_flow(from_node):

	print ('==== CALCULATINON START FOR COUNTING PASSING VEHICLES ====')

	UE=open('E:\\Research\\DynusT_Learning\\VA_Assgn_Testing\\UE_5iter_500min\\VehTrajectory.dat','r') # Trajectory data to read
	VA=open('E:\\Research\\DynusT_Learning\\VA_Assgn_Testing\\Veh_assign_oneshot_500min\\VehTrajectory.dat','r') # Trajectory data to read
	VP=open('E:\\Research\\DynusT_Learning\\VA_Assgn_Testing\\Veh_Path_assgin_oneshot_500min\\VehTrajectory.dat','r') # Trajectory data to read

	for i in range(0,5):
		UE.readline()
		VA.readline()
		VP.readline()


	count_UE=0
	count_VA=0
	count_VP=0

	print ('______ Finish to Load all Vehicle Trajectory Files ....')
	# Code Start for UE
	while 1:

		# read line by line
		Tj=UE.readline().split()
		
		# Insert a break, when file reading is done
		if Tj==[]:
			break

		# if Tj is NOT reading vehicle information then,
		if Tj[0]!='Veh':
			for i in Tj:
				if i==str(from_node):
					count_UE=count_UE+1

	print ('______ Finish to for UE Assignment Results ....')
	# Code Start for VA
	while 1:

		# read line by line
		Tj=VA.readline().split()
		
		# Insert a break, when file reading is done
		if Tj==[]:
			break

		if Tj[0]!='Veh':
			for i in Tj:
				if i==str(from_node):
					count_VA=count_VA+1

	print ('______ Finish to for Vehicle Assignment Results ....')
	# Code Start for VP
	while 1:

		# read line by line
		Tj=VP.readline().split()
		
		# Insert a break, when file reading is done
		if Tj==[]:
			break

		if Tj[0]!='Veh':
			for i in Tj:
				if i==str(from_node):
					count_VP=count_VP+1

	print ('______ Finish to for Vehicle + Path Assignment Results ....')


	UE.close()
	VA.close()
	VP.close()

	print ('==== ALL CALCULATINONS END ====')

	print '1. Total counted vehicles in UE assginment: ', count_UE
	print '2. Total counted vehicles in Vehile assginment: ', count_VA
	print '3. Total counted vehicles in Vehicle + Path assginment: ', count_VP




