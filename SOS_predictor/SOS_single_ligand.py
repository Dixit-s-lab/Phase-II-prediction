import os
import subprocess
import os
import time
import datetime
from tqdm import tqdm
import shutil
#import os, datetime;
#datestring = datetime.datetime.now().strftime("result-%d-%m-%Y-%H-%M-%S");
#print (datestring);
#os.mkdir(datestring);


print ("\t" "\t" "*********************************************************************************************************************************************")
print ("\t" "\t" "*                                                                    Welcome                                                                 *")
print ("\t" "\t" "*                                                     SITE OF SULPHONATION (SOS) PREDICTOR                                                   *")
print ("\t" "\t" "*                                          This is a script to Predict site of sulphonation in ligand                                        *")
print ("\t" "\t" "*                                                 --- written by Shivam Kumar Vyas Avik Das ---                                              *")
print ("\t" "\t" "*                                 PhD Research Scholar,Department of Medicinal Chemistry NIPER Guwahati                                      *")
print ("\t" "\t" "*                                   Guided by Dr Vaibhav A Dixit Assistant professor NIPER Guwahati                                          *")
print ("\t" "\t" "*********************************************************************************************************************************************" "\n") 

# Get the current working directory
current_directory = os.getcwd()

# Print the current working directory
print("Current Working Directory:", current_directory)

# List of directories to replace
directories_to_replace = ['docking', 'Results', '__pycache__']

# Function to replace directories
def replace_directories(directory_name):
    if os.path.exists(directory_name):
        shutil.rmtree(directory_name)
    #os.makedirs(directory_name)

# Replace specified directories
for directory_name in directories_to_replace:
    replace_directories(directory_name)

# Print a message indicating successful replacement
print("Directories replaced successfully.")

# Set the current working directory to a variable
address = current_directory

# Now, address contains the path of the current working directory
print("Address variable:", address)


#address = "/home/caddsys3/Documents/software/SOS_predictor/OpenEye_SOS_predictor"
address1 = address
print("Address 1 is = ", address1)

#os.mkdir(address + "/Results")
# address = "/home/avik/Documents/ResearchProject/SULT/Final-script-work/sult-scripts/Files"
print("Changing current address to the desired address")
print("The current address directory is")
os.chdir(address)
subprocess.run(["pwd"])
print("Looking for sdf input files")
#print("convert molecule into pdb formate from SDF")

from sdf_smi_sdrdkit import *

from File_header_for_tanimoto import *

"""
# convert molecule into pdb formate from SDF
for files in os.listdir("."):	
    if files.endswith(".sdf"):		
        subprocess.run(["obabel", "-isdf", files, "-opdb", "-O" + files.rstrip('.sdf') + ".pdb"])

# convert pdb into sdf file
for files in os.listdir("."):	
    if files.endswith(".pdb"):		
        subprocess.run(["obabel", "-ipdb", files, "-osdf", "-O" + files.rstrip('.pdb') + ".sdf"])
"""
# move sdf files in doking folder

os.mkdir(address1 + "/docking")

address2 = (address1 + "/docking")


for files in os.listdir("."):
    if files.endswith(".sdf"):
        subprocess.run(["mv", files, address2])


subprocess.run(["cp", "oe_dock_indep.py", "rec_2d06.oedu", address2])

subprocess.run(["cp", "mol2_pdbqt_avik.py", "convert_oedu_mol2.py", address2])

subprocess.run(["cp", "calculate_using_pdbqt_OEOutput.py", address2])

os.chdir(address2)

# convert sdf molecule in oeb

from openeye import oechem

def convert_sdf_to_oeb(input_sdf_filename, output_oeb_filename):
    ifs = oechem.oemolistream(input_sdf_filename)
    ofs = oechem.oemolostream(output_oeb_filename)

    for mol in ifs.GetOEGraphMols():
        oechem.OEWriteMolecule(ofs, mol)

    ifs.close()
    ofs.close()

def main():
    input_directory = "."  # Set this to the directory containing the .sdf files
    output_directory = "."  # Set this to the desired output directory

    for filename in os.listdir(input_directory):
        if filename.endswith(".sdf"):
            input_sdf_filename = os.path.join(input_directory, filename)
            output_oeb_filename = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}.oeb.gz")
            convert_sdf_to_oeb(input_sdf_filename, output_oeb_filename)

if __name__ == "__main__":
    main()

# openeye docking

from oe_dock_indep import *


# convert docked output into mol2 and unzip

from convert_oedu_mol2 import *

# mol2 to pdbqt convert

from mol2_pdbqt_avik import *

# rename pdbqt files

import os
import re

# Define a regular expression pattern to match the name in the first line
name_pattern = re.compile(r'REMARK  Name = (.+)$')

# Get a list of all .pdbqt files in the current directory
pdbqt_files = [filename for filename in os.listdir() if filename.endswith('.pdbqt')]

# Iterate through each .pdbqt file
for pdbqt_file in pdbqt_files:
    with open(pdbqt_file, 'r') as file:
        # Read the first line
        first_line = file.readline()
        # Try to match the name pattern in the first line
        match = name_pattern.search(first_line)
        
        if match:
            # Extract the name from the matched group
            name = match.group(1)
            
            # Construct the new filename
            new_filename = f'{name}_docked.pdbqt'
            
            # Rename the file
            os.rename(pdbqt_file, new_filename)
            
            print(f'Renamed {pdbqt_file} to {new_filename}')
        else:
            print(f'Could not find a name in {pdbqt_file}')

# rename done
#adding _docked in pdbqt file
"""
for files in os.listdir("."):
        if files.endswith(".pdbqt"):
	        subprocess.run(["obabel", files, "-o", "pdbqt", "-O", files.rstrip('.pdbqt') + "_docked.pdbqt", "-m", "-h"], check=True)
"""

#from calculate_using_pdbqt_OEOutput import *
# calculate distance from docked file

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


os.mkdir(address2 + "/BDE-calculation")
address3 = address2 + "/BDE-calculation"

for files in os.listdir("."):
    if files.endswith(".pdbqt"):
        subprocess.run(["mv", files, address3])

os.chdir(address)


os.mkdir(address + "/Results")
address4 = address + "/Results"
print(address4)

address6 = r"/home/caddsys3/Documents/software/SOS_predictor/OE_server_files"

subprocess.run(["cp", "mopac_inp_file_creator.py", address3])
#subprocess.run(["cp", "BDE-calculator.py", address3])
subprocess.run(["cp", "get-mopac-Es-2.sh", address3])
subprocess.run(["cp", "new_modelxl.py", address3])
subprocess.run(["cp", "old_name_inpdbqt_oe.py", address3])

os.chdir(address3)

from mopac_inp_file_creator import *

subprocess.call(['bash', 'get-mopac-Es-2.sh'])
os.chdir(address2)
subprocess.run(["cp", "Final_Output.txt", address3])
os.chdir(address3)
from new_modelxl import *
subprocess.run(["cp", "Accesibility_Model_NEW.csv", address4])
subprocess.run(["cp", "Accesibility_Model_NEW.csv", "/home/caddsys3/Documents/software/SOS_predictor/OE_server_files/"])

os.chdir(address)

for files in os.listdir("."):
    if files.endswith(".smi"):
        subprocess.run(["mv", files, address4])


# files transfer in results directory

original = r"/home/caddsys3/Documents/software/SOS_predictor/OpenEye_SOS_predictor/docking"



original1 = r"/home/caddsys3/Documents/software/SOS_predictor/OpenEye_SOS_predictor/__pycache__"


original2 = r"/home/caddsys3/Documents/software/SOS_predictor/OpenEye_SOS_predictor/Results"


#print (os. getcwd())
"""
target = datestring
shutil.move(original, target)
shutil.move(original1, target)
shutil.move(original2, target)


target1 = r"/home/caddsys3/Documents/software/SOS_predictor/OE_sos-predictor-all-results"



shutil.move(target, target1)
"""

