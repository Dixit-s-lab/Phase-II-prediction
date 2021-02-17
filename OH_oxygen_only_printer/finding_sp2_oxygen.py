from pathlib import Path
from biopandas.mol2 import PandasMol2

# Fetching_each_mol2_file function that is called from the main_program.py file
def Fetching_each_mol2_file(input_folder_path):
    # extracting only the .mol2 files from input folder using glob function
    # glob functions returns the path of the .mol2 files
    # is_file() checks whether a particular item is a file or not
    input_folder_path = Path(input_folder_path)
    files_list = [item for item in input_folder_path.glob("*.mol2") if item.is_file()]

    ligand_sp2_oxygen = {}  # stores the sp2 oxygens with their bonding atoms according to Ligand
    #ligand_quart_carbon = {}
	
    # looping over each mol2 file present in our input folder
    for file_path in files_list:
        ligand = file_path.parts[-1].split("_")[0]  # fetching the ligand name from the file path

        # quart_carbon_ids is a dictionary stores the actual quarternary carbon ids with their bonding atoms as returned by Main_Quart_Carbon function
        sp2_oxygen_ids = Main_SP2_Oxygen(file_path)
        ligand_sp2_oxygen[ligand] = sp2_oxygen_ids

        # adding all the quarternary carbon ids with their respective ligand
        # ligand_quart_carbon is a  dictionary of dictionary which stores
        # ACTUAL QUARTERNARY CARBONS with Bonding atoms, against their respective ligands
        #"""if len(quart_carbon_ids) != 0: # will be true if there are any quarternary carbons for that ligand
        #    ligand_quart_carbon[ligand] = quart_carbon_ids
        #else: # will be true if that ligand has no quarternary carbons
        #    continue"""

    return ligand_sp2_oxygen # return ligand_quart_carbon to the main_program.py file


def Removing_unwanted_spaces(line):
    line = line.strip(" ")
    for i in range(5,0,-1):	
        line = line.replace(" "*i,"#")
    line = line.split("#")
    return line


# Function Check_Quarternary_Carbon is called by Main_Quart_Carbon function
# It checks and returns the ids of quarternary carbons to the Main_Quart_Carbon function
# This function excets two values:
# 1.) bonds_info: it contains entire information present in the tripos bond section of the mol2 file
# 2.) H_atom_id: it refers to the ID of the first H atom for that mol2 file
def Check_SP2_OXYGEN(atoms_info, file_path):
    #final_list = [] # stores the ids of both the origin and the target atoms one after the other
    #count_dict = {} # stores the count of the all the atoms
    #quart_carbon_ids = [] # store the ids of probable quarternary carbon

    # looping over each line in the bonds_info
    for line in atoms_info:
        line = Removing_unwanted_spaces(line)
        # adding only the origin and the target atom one after the other to the final_list
        #"""final_list.extend([line[1],line[2]])
    #print("final_list: ",final_list)"""

    # First we want to check for Probable Quarternary Carbon Atoms and the logic is that, the atoms having 4 bonds can be
    # Probable Quarternary Carbon Atoms, and we would be storing their counts in a dictionary "count_dict" with keys as the
    # atom_ids and values would be the respective counts
    # Initialising the count of each atom as 0 is count_dict
    #for atom_id in final_list:
    #    count_dict[atom_id] = 0

    # Counting the occurence of each atom in the final list and updating it in count_dict
    #for atom_id in final_list:
    #    count_dict[atom_id] += 1

    # Now selecting the atoms with 4 bonds(Probable Quarternary carbon)
    # and storing them in a list "quart_carbon_ids"
    #for key in count_dict:
    #    if count_dict[key] == 4:
    #        quart_carbon_ids.append(key)"""

    # Till now we only know that our Probable Quarternary Carbon Atoms have 4 bonds(bonding), but we also need to know which
    # are those 4 bonding atoms and then check if any one of them is hydrogen.
    # So we now add the information about the atoms to which each Probable Quarternary Carbon Atoms is bonding
    # The final list has the list of all the atom ids, where the odd indexes are the intitial atoms and even indexes are target atoms
    # So in the outer loop we select our Probable Quarternary Carbon Atom id and check at how many places does this Probable Quarternary Carbon Atom
    # occurs in our final list
    # As soon as we find the index at which our Probable Quarternary Carbon Atom matches with the atom id in the final list
    # we check:
    # 1.) If this index is even this means that our Probable Quarternary Carbon Atom is the target atom, which means to fetch its bonding
    # atom we will subtract 1 from the index and fetch that partcular atom from the final list
    # 2.) If the index is odd this means that our Probable Quarternary Carbon Atom is the initial(origin) atom, which means to fetch its bonding
    # atom we will add 1 to the index and fetch that partcular atom from the final list
    # Then we check if is less than the H atom id, if yes, then we append the bonding atoms to a list "bonding_atoms"

    #Quart_carb_bonding_atoms = {} #This store the Actual Quarternary Carbon Atom along with bonding atoms
    SP2_OXYGEN_atoms = {} #This store the SP2 OXYGEN Atom ids
    #"""for i in range (len(quart_carbon_ids)):
    #    bonding_atoms = []
    #    for j in range (len(final_list)):
    #        if quart_carbon_ids[i] == final_list[j] and j % 2 == 0 and int(final_list[j+1]) < H_atom_id:
    #            bonding_atoms.append(final_list[j+1])
    #        elif quart_carbon_ids[i] == final_list[j] and j % 2 != 0 and int(final_list[j-1]) < H_atom_id:
    #            bonding_atoms.append(final_list[j-1])"""

        # Now we store the Probable Quarternary Carbon Atom along with the bonding atoms in a dictionary
        # Earlier each of our Probable Quarternary Carbon Atom had 4 bonding atoms but now after comparing
        # them with H atom id, only those bonding atoms will remain which are not hydrogen, which also means that
        # If any of our Probable Quarternary Carbon had H as any one of their bonding atom, then that Probable Quarternary Carbon
        # will no longer have 4 bonding atoms and cannot be considered as quarternary

        # Now we will only fetch the actual quarternary carbons by simply checking their number of remaining bonding atoms
    #    """if len(bonding_atoms) < 4: # true if our carbon is not quarternary
    #        continue
    #   else: # true if our carbon is quarternary
            # adding the quarternary carbon id as key and the list of its bonding atoms as values to the dictionary Quart_carb_bonding_atoms
    #        Quart_carb_bonding_atoms[quart_carbon_ids[i]] = bonding_atoms"""
    pmol = PandasMol2()
    pmol.read_mol2(str(file_path)) # reading the ATOM section of mol2 file using BIO PANDAS
    #O3_atom_id = pmol.df["atom_id"][pmol.df["atom_type"] == "O.2"] # fetching the id of sp2 O atom of our file
    H_atom_id = pmol.df["atom_id"][pmol.df["atom_type"] == "H"]
    #check = O3_atom_id.astype(int)
    check2 = H_atom_id.astype(int)  
    #check4 = check - 1 
    check3 = check2 - 1
        
    SP2_OXYGEN_atoms = check3
    #SP2_OXYGEN_atoms.update(check4)
    

    return SP2_OXYGEN_atoms # returning the dictionary "Quart_carb_bonding_atoms" to Main_Quart_Carbon function



# Main function extracts the tripos bond section from the mol 2 file and the id of first H atom and sends it to Check_Quarternary_Carbon
def Main_SP2_Oxygen(file_path):
    fr = open(file_path, "r")
    counter = 0 # determines which portion of the Mol2 file we are reading
    atoms_info = [] # store all info available in the tripos bond section of the mol2 file

    ####### Finding the first id for H atom for every file #######
    # We find the first id of H atom for every mol2 file, later on we compare the ids of the bonding atoms of our
    # Probable Carbon Atoms with this H atom id to decide actual Quarternary Carbons
    #"""pmol = PandasMol2()
    #pmol.read_mol2(str(file_path)) # reading the ATOM section of mol2 file using BIO PANDAS
    #H_atom_id = pmol.df["atom_id"][pmol.df["atom_name"] == "H"].iloc[0] # fetching the id of first H atom of our file"""
    ####### Finding the first id for H atom for every file #######

    # reading mol2 file line by line
    for line in fr:
        line = line.strip("\n")

        # Accessing the bond information from @<TRIPOS>BOND section
        # If the value of counter in 0 this means we are not in the @<TRIPOS>BOND section
        # If the value of counter in 1 this means we are inside the @<TRIPOS>BOND section
        if line == "@<TRIPOS>MOLECULE":
            counter = 0
            if len(atoms_info) != 0:
                # here quart_carbon_ids is a dictionary having the Actual Quarternary Carbon Atom with their bonding atoms
                SP2_OXYGEN_atoms = Check_SP2_OXYGEN(atoms_info, file_path)
                #Quart_carb_bonding_atoms = Check_SP2_OXYGEN(atoms_info, file_path)
                #print(quart_carbon_ids)
                break # reading only the first "@<TRIPOS>BOND" section from the file and then breaking the loop

        elif line == "@<TRIPOS>ATOM":
            counter+=1
            continue

        # If counter value is 1, appending the lines to the list bonds_info
        # bonds_info store the bond information for all the atoms of a particular Model
        if counter == 1:
            atoms_info.append(line)

    #print(Models_Quart_Carbon)
    return SP2_OXYGEN_atoms # returning dictionary "Quart_carb_bonding_atoms" to Fetching_each_mol2_file function
#Main_Quart_Carbon()
#input_folder_path = r"D:\PFB_clients\Avik\test_folder"
#Fetching_each_mol2_file(input_folder_path)
