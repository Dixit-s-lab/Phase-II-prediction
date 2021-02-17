# This program imports the code from calculating_atom_dist_modified.py, finding_quart_carbon.py and from obabel_converter_1 import

from finding_sp2_oxygen import *
from calculating_atom_dist_test import *
import pandas as pd
from obabel_converter import *

####################### CALCULATING ATOM DISTANCE #########################
#Fe_coordinates = [15.435, 0.804, -47.784]
#Fe_coordinates = [132.948, -61.511, -0.283]
#input_folder_path = r"/home/avik/Downloads/OH_oxygen_only_1/OH_oxygen_only"
#input_folder_path = r"D:\PFB_clients\Avik\Avik_project5\OH_oxygen_only"
Final_Output_Path = Fetching_each_file(input_folder_path, Fe_coordinates)
#print("\n" " Output file successfully generated at:  ", Final_Output_Path)
####################### CALCULATING ATOM DISTANCE #########################


####################### CONVERTING .pdbqt to .mol2 using Open Bable#########################
converter()
#valency_checker()
####################### CONVERTING .pdbqt to .mol2 using Open Bable#########################


########### FOR DETECTING QUARTERNARY CARBONS IN ALL MOL2 FILES#############
# We first consider the atoms in the tripos bond section of the mol2 file which have 4 bonds as PROBABLE QUARTERNARY CARBONS
# Because later we will check if any of those 4 bonding atoms are hydrogen or not and
# We will not consider that carbon as quarternary if any of its bonding atoms are hydrogens.

# ligand_quart_carbon is a  dictionary of dictionary which stores
# ACTUAL QUARTERNARY CARBONS with Bonding atoms, against their respective ligands
# which are returned by Fetching_each_mol2_file function located in finding_quart_carbon.py
ligand_sp2_oxygen = Fetching_each_mol2_file(input_folder_path)
print("ligand_sp2_oxygen: ",ligand_sp2_oxygen, "\n")
# printing the output in proper format
print("SP2 hybridised Oxygens for Respective Ligands With their Bonding Atoms are: ")
for key in ligand_sp2_oxygen:
    print(ligand_sp2_oxygen[key])
    #print(key)
########### FOR DETECTING PROBABLE QUARTERNARY CARBONS IN ALL MOL2 FILES#############


################# DELETING ROWS HAVING QUARTERNARY CARBON FROM FINAL OUTPUT FILE#################
Final_Output_No_Quart_Carb_Path = Final_Output_Path.parent/"Final_Output_SP3_OXYGENS_only.txt"
Other_than_SP2_Oxygen_Path = Final_Output_Path.parent/"Final_Output_OH_OXYGEN_only.xlsx"

# reading our final_output.txt file as a dataframe
final_output_df = pd.read_csv(Final_Output_Path, sep="\t", index_col=False)
#print(final_output_df)

final_output_df_new = final_output_df.copy(deep=True) # making a copy of original dataframe
row_indexes_for_removed_ligands = [] # for storing row indexes of atoms which are not SP2 oxygen
# looping over each ligand in ligand_quart_carbon
for ligand in ligand_sp2_oxygen:
    # looping over each quarternary carbon for each ligand
    for Atom_id in ligand_sp2_oxygen[ligand]:
        # geting indexes of the rows to be dropped and saving them in a list
        rows = final_output_df[final_output_df["Ligand"] == ligand][final_output_df["AtomNo"] == int(Atom_id)].index
        row_indexes_for_removed_ligands.append(rows.values)

        # selecting that particular row from the dataframe that has the quarternary carbon and dropping it
        final_output_df.drop(final_output_df[final_output_df["Ligand"] == ligand]
                             [final_output_df["AtomNo"] == int(Atom_id)].index, inplace = True)



# printing the retrieved row indexes for the ligands to be removed
print("row_indexes_for_removed_ligands: ",row_indexes_for_removed_ligands)
# removing the empty lists from the row_indexes_for_removed_ligands
row_indexes_for_removed_ligands = [x for x in row_indexes_for_removed_ligands if len(x)!=0]
print("row_indexes_for_removed_ligands empty list removed", row_indexes_for_removed_ligands)
# bringing all the indexes in a single list so that we can use them in loc function
row_indexes_for_removed_ligands = [index for index_list in row_indexes_for_removed_ligands for index in index_list]
print("row_indexes_for_removed_ligands in a single list: ",row_indexes_for_removed_ligands)

# Extracting the atoms other than SP2 atoms from the original dataframe
only_sp2_df = final_output_df_new.loc[row_indexes_for_removed_ligands,:]
print("DATAFRAME WITH ONLY OH OXYGEN ATOMS")
print(only_sp2_df)

print("DATAFRAME WITH ONLY sp3 OXYGEN ATOMS")
print(final_output_df)

print("ORIGINAL DATAFRAME")
print(final_output_df_new)
#print(final_output_df["Dist_from_Fe"])
# Now "final_output_df" does not have any rows containing quarternary carbon
# rounding off the values in the 'Dist_from_Fe' column in our dataframe upto 3 decimal places
final_output_df["Dist_from_Fe"] = final_output_df["Dist_from_Fe"].round(3)
final_output_df.to_csv(Final_Output_No_Quart_Carb_Path, index=None, sep='\t')
only_sp2_df["Dist_from_Fe"] = only_sp2_df["Dist_from_Fe"].round(3)
only_sp2_df.to_csv(Other_than_SP2_Oxygen_Path, index=None, sep='\t')
print("Output file successfully created at: ", Final_Output_No_Quart_Carb_Path)
print("Output file successfully created at: ",Other_than_SP2_Oxygen_Path)
################# DELETING ROWS HAVING QUARTERNARY CARBON FROM FINAL OUTPUT FILE#################


