# Avik HAS written this script

import os
import subprocess
from biopandas.mol2 import PandasMol2

#from old_name_inpdbqt_oe import *

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


for files in os.listdir("."):
	if files.endswith(".pdbqt"):
            subprocess.run(["obabel", files, "-o", "pdb", "-m"], check=True)	
for files in os.listdir("."):
        if files.endswith(".pdb"):
	        print("Splitting file :", files)
	        subprocess.run(["obabel", files, "-o", "mol2", "-O", files.rstrip('pdb') + "mol2", "-m", "-h"], check=True)
#	        subprocess.run(["obabel", files, "-o", "mol2", "-O", files.rstrip('.pdb') + "_pose.mol2", "-m"], check=True)


pmol = PandasMol2()
files_list = []
O_list_bond = []
H_list_bond = []
O_list_mol = []
H_list_mol = []
Final_Hydrogen_ID = []

for files in os.listdir("."):
    if files.endswith(".mol2"):
        filename = files.split('.')[0]
        new_file = filename + ".xyz"
        subprocess.run(["obabel", "-imol2", files, "-oxyz", "-O" + filename + ".xyz"])

        print("Assembling file :", files)
        data = pmol.read_mol2(files)
        Hyd_atoms = (pmol.df["atom_id"][pmol.df["atom_type"] == "H"])
        Oxy_atoms = (pmol.df["atom_id"][pmol.df["atom_type"] == "O.3"])
        H_list_mol = Hyd_atoms.tolist()
        O_list_mol = Oxy_atoms.tolist()

        with open(files) as f:
            for lines in f:
                line = lines.strip("\n")
                # line = lines.strip("  ")
                # print(line)
                if line == "@<TRIPOS>BOND":
                    for line in f:
                        line = line.strip(" ")
                        line = line.strip("\n")
                        # print(line)
                        O_list_bond.append(line[6:8].strip())
                        H_list_bond.append(line[11:14].strip())
            # print(O_list_bond)
            # print(H_list_bond)

            occurences = []

            for i in range(len(O_list_mol)):
                for j in range(len(O_list_bond)):
                    if int(O_list_mol[i]) == int(O_list_bond[j]):
                        # print(j)
                        occurences.append(j)

            # print("occurences", occurences)

            Final_Hydrogen_ID = []
            for j in range(len(occurences)):
                for k in range(len(H_list_mol)):
                    if int(H_list_bond[occurences[j]]) != int(H_list_mol[k]):
                        continue

                        # Final_Hydrogen_ID.append(H_list_bond[occurences[j]])
                    else:
                        # continue
                        # print(H_list_bond[occurences[j]])
                        Final_Hydrogen_ID.append(H_list_bond[occurences[j]])
            print("OH Hydrogen atom IDs :", Final_Hydrogen_ID)
            O_list_bond = []
            H_list_bond = []

        for i in range(len(Final_Hydrogen_ID)):
            c = 0
            for xyzfiles in os.listdir("."):
                if xyzfiles.endswith(new_file):
                    with open(xyzfiles) as f, open(filename + "-" + Final_Hydrogen_ID[i] + "-anion.xyz", 'w') as z:
                        for lines in f:
                            c = c + 1
                            line = lines.strip("\n")
                            if c != (int(Final_Hydrogen_ID[i]) + 2):
                                print(line, file=z)
                                print(new_file, "is created")
                                # print(line)
#############################_CHANGING XYZ FILE HEADERS FOR ANION FILES_################
for files in os.listdir():
    if files.endswith("-anion.xyz"):
        with open(files) as f:
            line = f.readlines()
            # print(line[0])
            line_nums = int(line[0]) - 1
            line[0] = str(line_nums) + "\n"
            # print(line[0], "\n") PRINTING THE NEW NAME
        with open(files, "w") as f:
            f.writelines(line)
#############################_STARTING FILE CONVERSION PROCESS_########################

print("\n" "_INITIATING FILE CONVERSION PROCESS_")
#print("Press 1 for generating GAUSSIAN input files")
#print("Press 2 for generating MOPAC input files")
choice = 2

if int(choice) == 1:
    for files in os.listdir():
        if files.endswith(".xyz"):
            filename1 = files.split('.')[0]
            subprocess.run(["obabel", "-ixyz", files, "-ogjf", "-O" + filename1 + ".gjf"])

    proc = "%nprocshared=8"
    mem = "%mem=15GB"
    p = "#p opt=calcfc freq=noraman b3lyp/6-31+g(d,p) scrf=(cpcm,solvent=methanol)"
    print("\n" "The following GAUSSian INPUT files are created ")
    for files in os.listdir():
        if files.endswith(".gjf"):
            with open(files) as f:
                print(files)
                line = f.readlines()
                line[0] = "\n"
                line[1] = "\n"
                line[2] = "\n"
                line[3] = "\n"
                line[4] = "\n"
                # print(line[0:5])
            with open(files, "w") as fw:
                fw.writelines(line)

    for files in os.listdir():
        if files.endswith(".gjf"):
            name = files.split('.')[0]
            # print(name)
            chk = "%chk=" + name + ".chk" + "\n"
            with open(files) as f:
                line = f.readlines()
                line[0] = chk
                line[1] = proc + "\n"
                line[2] = mem + "\n"
                line[3] = p + "\n"
                line[4] = "\n"
                line.insert(5, name + "\n")
                line.insert(6, "\n")
                line.insert(-1, "\n")
                # print(line[0:5])
            with open(files, "w") as fa:
                fa.writelines(line)

    for files in os.listdir():
        if files.endswith("-anion.gjf"):
            with open(files) as f:
                line = f.readlines()
                line[7] = "-1 1" + "\n"
            with open(files, "w") as fs:
                fs.writelines(line)

if int(choice) == 2:
    for files in os.listdir():
        if files.endswith(".xyz"):
            filename1 = files.split('.')[0]
            subprocess.run(["obabel", "-ixyz", files, "-omop", "-O" + filename1 + ".mop"])
    header = "PM7 BONDS CHARGE=0 SINGLET XYZ PRNT=2 PRTXYZ FLEPO PRECISE EPS=32.613 GNORM=0.0"
    header_anion = "PM7 BONDS CHARGE=-1 SINGLET XYZ PRNT=2 PRTXYZ FLEPO PRECISE EPS=32.613 GNORM=0.0"
    print("\n" "The following MOPAC files are created ")
    for files in os.listdir():
        if files.endswith(".mop"):
            name = files.split('.')[0]
            print(files)
            with open(files) as f:
                line = f.readlines()
                line[0] = header + "\n"
                line[1] = name + "\n"
                for i in range(2):
                    line.append("\n")
                # line[-2] = "\n"
            with open(files, "w") as fa:
                fa.writelines(line)

    for files in os.listdir():
        if files.endswith("-anion.mop"):
            with open(files) as f:
                line = f.readlines()
                line[0] = header_anion + "\n"
            with open(files, "w") as fs:
                fs.writelines(line)
   
#    for files in os.listdir():
#        if files.endswith("-anion.mop"):
#            with open(files) as f:

for files in os.listdir("."):
    if not files.endswith("anion.mop") and files.endswith(".mop"):
        # print(files)
        # c=c+1
        subprocess.call(["cp", files, f"{files.split('.')[0]}-neutral.mop"])
    

if int(choice) != 1 and int(choice) != 2:
    print("INVALID INPUT")
