# Analysing data from a .pdbqt file
# Note: The input .pdbqt file was coverted to a .txt file for reading purpose, this
# doesn't cause any descrepencies in the final output


from pathlib import Path
import math
import os

print ("\t" "\t" "*********************************************************************************************************************************************")
print ("\t" "\t" "*                                                                                                                                           *")
print ("\t" "\t" "* Welcome, This is a script to measure distance between specified atoms in ligand to one specific atom in the receptor as per user's choice *")
print ("\t" "\t" "*        It will return the distance of the specified atoms which are located at less than 6A from the specified receptor atom               *")
print ("\t" "\t" "*                                                               --- written by Avik Das ---                                                 *")
print ("\t" "\t" "*                                                                   M.Pharm,BITS Pilani                                                     *")
print ("\t" "\t" "*                                                                guided by Vaibhav A Dixit                                                  *")
print ("\t" "\t" "*********************************************************************************************************************************************" "\n") 
input_folder_path = r""
input_folder_path = input("\n" " Please enter the path of your folder containing all output files in pdbqt format: ")
####Enter the path of your all your folder containing .pdbqt file ####
#input_folder_path = r"/home/avik/Documents/ResearchProject/SULT/Test_script"

Fe_coordinates = []
####Enter the Fe coordinates here ####
Fe_coordinates = [float(Fe_coordinates) for Fe_coordinates in input("\n" " Please enter the x,y,z coordinates of the O4P atom separated by a space only: ").split()]
#Fe_coordinates = [132.948, -61.511, -0.283]
####Enter the pose number here
pose = input("\n" " Kindly enter the number of poses you want to analyse: ")
#pose = 3
print ("\n""********************************************** SELECT YOUR CHOICE OF ATOM *********************************************")
print ("\n" "\t" "\t" " Choice 1 : Oxygen atoms only" "\n" "\t" "\t" "\n")
comb = input(" Based on the above menu kindly enter your Choice of atom/atoms of which you want to find the distance from O4P : ")
print ("\n" " If you want the atoms with no criteria of a distance please enter 100" "\n")
limit = input(" Kindly enter the distance upto which you want to measure : ")
#limit = 100

def Fetching_each_file(input_folder_path,Fe_coordinates):
	input_folder_path = Path(input_folder_path)
	
	# extracting only the .pdbqt files from input folder using glob function
	# glob functions returns the path of the .pdbqt files
	# is_file() checks whether a particular item is a file or not
	files_list = [item for item in input_folder_path.glob("*.pdbqt") if item.is_file()]
	files_list.sort()
	out_path = input_folder_path/"Final_Output.txt"

	with open(out_path,"w") as fw:
		header = ["Ligand","\t","Pose_No","\t","Dock_Score","\t","Atom","\t","AtomNo","\t","Dist_from_Fe","\n"]
		fw.writelines(header)

	for input_path in files_list:
		#Output_filename = "Output_" + input_path.parts[-1] + ".txt"
		#out_path = input_folder_path/Output_filename
		#print(out_path)
		#print(input_path.parts[-1])
		ligand = input_path.parts[-1].split("_")[0]
		
		out_path = Main(input_path, out_path, Fe_coordinates, ligand, comb, limit)
	print("\n" " Output file successfully generated at:  ", out_path)
		
		#print(ligand)
	return out_path


def Main(input_path, out_path, Fe_coordinates, ligand, comb, limit):
	final_list = []
	
	with open(input_path, "r") as fr:
		for line in fr:
			line_list = Remove_unwanted_spaces(line)
			#print(line_list)
			#print(len(line_list))
			if line_list[0] == "MODEL":
				model = Checking_model_number(line_list,pose)
				if model == "Null":
					break
				
			#print(model)

			if "RESULT:" in line_list:
				docking_score = Extract_docking_score(line_list)
				#print(docking_score)
				
			if int(comb) == 1:
				if line_list[0] == "ATOM" or line_list[0] == "HETATM":
					if line_list[11] == "O" or line_list[11] == "OA":
						coordinates_list = Extracting_axis_coordinates(line_list)
						dist = Finding_distance(coordinates_list,Fe_coordinates)
						if dist < int(limit):
							#print(line_list)
							coordinates_list.insert(0,ligand)
							coordinates_list.insert(1,model)
							coordinates_list.insert(2,docking_score)
							coordinates_list.insert(5,dist)
							#print(coordinates_list)
							final_list.append(coordinates_list)
								
					#print(final_list)																									
	
		#### for writing data to the model
		Write_data(final_list,out_path)
			
	return out_path
	
def Remove_unwanted_spaces(line):
	line = line.strip(" \n") # making each line of uniform length
	for j in range(7,0,-1):
		line = line.replace(" "*j,"#")	
		line_list = line.split("#")
	#print(line_list)
	#print(len(line_list))
	return line_list

def Checking_model_number(line_list,pose):
		model_number = int(line_list[1])
		if model_number > int(pose):
			return "Null"
		else:
			model = "".join(line_list).strip("\n")
			return model
	
def Extracting_axis_coordinates(line_list):
	coordinates_list = []
	#atom_type = line_list[11].strip("\n")	
	#coordinates_list.append(atom_type)
	#atom_id = line_list[3]	
	#coordinates_list.append(atom_id)
	
	atom_name = line_list[2]
	coordinates_list.append(atom_name)
	atom_no = line_list[1]
	coordinates_list.append(atom_no)
	x = float(line_list[5])
	coordinates_list.append(x)	
	y = float(line_list[6])
	coordinates_list.append(y)	
	z = float(line_list[7])
	coordinates_list.append(z)
		
	return coordinates_list

def Extract_docking_score(line_list):
	docking_score = line_list[3]
	return docking_score
	
def Finding_distance(coordinates_list,Fe_coordinates):
	x_dist = (coordinates_list[2] - Fe_coordinates[0]) ** 2
	y_dist = (coordinates_list[3] - Fe_coordinates[1]) ** 2
	z_dist = (coordinates_list[4] - Fe_coordinates[2]) ** 2
	dist = math.sqrt(x_dist+y_dist+z_dist)
	dist = round(dist,3)
	return dist

def Write_data(final_list,out_path):
	#header = ["Ligand","\t","Model Number","\t","Score","\t","Atom","\t","AtomNo","\t","Distance from Fe","\n"]
	#print(final_list)
	#print(len(final_list))
	#print(out_path)
	with open(out_path,"a") as fw:
		#fw.writelines(header)
		
		for line in final_list:
			line = [str(item)+"\t"+"   " for item in line]
			fw.writelines(line[0:2])
			fw.writelines(line[2:-3])
			
			fw.write("\n")
		#fw.write("\n")
		
#Fetching_each_file(input_folder_path,Fe_coordinates)
