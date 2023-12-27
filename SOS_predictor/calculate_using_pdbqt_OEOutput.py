from pathlib import Path
import math
import os
# from biopandas.mol2 import PandasMol2
# pmol = PandasMol2()
# pmol.read_mol2(str(file_path))

input_folder_path = os.getcwd()

Fe_coordinates = []

Fe_coordinates = [132.948, -61.511, -0.283]

pose = 1
print ("\n""********************************************** SELECT YOUR CHOICE OF ATOM *********************************************")
print ("\n" "\t" "\t" " Choice 1 : Oxygen atoms only" "\n" "\t" "\t" "\n")
# comb = input(" Based on the above menu kindly enter your Choice of atom/atoms of which you want to find the distance from O4P : ")
comb = 1
print ("\n" " If you want the atoms with no criteria of a distance please enter 100" "\n")
# limit = input(" Kindly enter the distance upto which you want to measure : ")
limit = 100

def Fetching_each_file(input_folder_path,Fe_coordinates):
	input_folder_path = Path(input_folder_path)
	
	
	files_list = [item for item in input_folder_path.glob("*.pdbqt") if item.is_file()]
	files_list.sort()
	out_path = input_folder_path/"Final_Output.txt"

	with open(out_path,"w") as fw:
		header = ["Ligand","\t","Atom","\t","AtomNo","\t","Dist_from_Fe","\n"]
		fw.writelines(header)

	for input_path in files_list:
		print("\n" " Input file successfully read from:  ", input_path)
		ligand = input_path.parts[-1].split("_")[0]
		# print(ligand)
		out_path = Main(input_path, out_path, Fe_coordinates, ligand, comb, limit)
	print("\n" " Output file successfully generated at:  ", out_path)
		
		#print(ligand)
	return out_path


def Main(input_path, out_path, Fe_coordinates, ligand, comb, limit):
	final_list = []
	
	with open(input_path, "r") as fr:
		for line in fr:
			line_list = Remove_unwanted_spaces(line)
			# print(line_list)
			#print(len(line_list))
			if line_list[0] == "MODEL":
				model = Checking_model_number(line_list,pose)
				if model == "Null":
					break
				
			#print(model)

			if "RESULT:" in line_list:
				docking_score = Extract_docking_score(line_list)
				# print(docking_score)
				
			if int(comb) == 1:
				if line_list[0] == "ATOM" or line_list[0] == "HETATM":
					# print(line_list)
					if line_list[12] == "O" or line_list[12] == "OA":
						print("LINE LIST", line_list)
						coordinates_list = Extracting_axis_coordinates(line_list)
						print("Coordinates list", coordinates_list)
						print("Fe coordinates", Fe_coordinates)
						dist = Finding_distance(coordinates_list,Fe_coordinates)
						print(dist, limit)
						if dist < float(limit):
							# print(line_list)
							coordinates_list.insert(0,ligand)
							# coordinates_list.insert(1,model)
							# coordinates_list.insert(2,docking_score)
							coordinates_list.insert(4,dist)
							#print(coordinates_list)
							final_list.append(coordinates_list)
								
					#print(final_list)																									
			print(final_list)
		#### for writing data to the model
		print("Final List", final_list)
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
	x = float(line_list[6])
	coordinates_list.append(x)	
	y = float(line_list[7])
	coordinates_list.append(y)	
	z = float(line_list[8])
	coordinates_list.append(z)
		
	return coordinates_list

def Extract_docking_score(line_list):
	docking_score = line_list[3]
	return docking_score
	
def Finding_distance(coordinates_list,Fe_coordinates):
	print("Coordinates list", coordinates_list, "Fe coordinates", Fe_coordinates)
	print(coordinates_list, Fe_coordinates)
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
			print(line)
			# fw.writelines(line[0:2])
			# fw.writelines(line[2:-3])
			fw.writelines(line[0:3] + line[4:5])
			fw.write("\n")
		#fw.write("\n")
		
if __name__ == "__main__":
	Fetching_each_file(input_folder_path,Fe_coordinates)
