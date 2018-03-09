# Check path and file

# Zone (node)
# Sample = Origin: 125 (11013) || Destin: 364 (353)

# Loading Trajectory files
#veh=open("E:\\DynusT_Learning\\VA_Assgn_Testing\\UE_5iter_500min\\output_vehicle.dat","r")
re_v=open("E:\\DynusT_Learning\\VA_Assgn_Testing\\selected_vehicle.dat","w")
pat=open("E:\\DynusT_Learning\\VA_Assgn_Testing\\UE_5iter_500min\\output_path.dat","r")


orin=11013	# Zone number 125
dstn=353	# Znoe number 364

count=0

while 1:
	#vehicle_info=veh.readline().split()
	path_info=pat.readline().split()

	if path_info==[]:
		break

	origin_match=0
	destin_match=0

	for i in path_info:
		if i==str(orin):
			origin_match=1
		if i==str(dstn):
			destin_match=1

	if (origin_match==1) and (destin_match==1):
		count=count+1
		#print path_info
		re_v.write(str(path_info))
		re_v.write('\n')

re_v.close()
pat.close()





















