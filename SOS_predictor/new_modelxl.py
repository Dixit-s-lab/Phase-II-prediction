import pandas as pd 

H_catanion_energy = 307.3846

def calc_final_energy(row):
    capenergy = (float(row["mopacE_y"]) + H_catanion_energy) - float(row["mopacE_x"])
    TotalEnergy = (0.6111 * capenergy) - 83.288
    return round(TotalEnergy, 4)

def compare_atoms(row):
    if abs(int(row['AtomNo']) - int(row['AtomID'])) == 1:
        return True
    return False

def calculate_BDE_Dist(row):
    return round(float(row["BDE"])/10 + float(row["Dist_from_Fe"]), 3)

def LigandX(row):
    return row["Ligand"] + str(row["AtomNo"])# + "_" + row["Pose_No"][-1]

def LigandXX(row):
    return row["ligandX"] + "_" + row["Pose_No"][-1]

def LigandY(row):
    return row["Ligand"] + str(int(row["AtomID"]) - 1)# + "_" + row["Tag"][-1]

def Dist_from_Fe(row):
    if row["Dist_from_Fe"] <=6.90 or row["BDE"] <= 53.00:
        return "Substrate"
    else:
        return "Non-Substrate"


def isSite_of_sulphonation(row):
    if row["Substrate/Non-substrate"] == "Substrate" and row["BDE_dist"] <= 14.02 or row["BDE"] <= 53.00:
        return "YES"
    else:
        return "NO" 

mopac_energies = pd.read_csv("mopac-energies.txt", sep = " ", header = 0)

mopac_energies["Ligand"] = mopac_energies["molecule"].apply(lambda x: x.split("_")[0])
mopac_energies["Tag"] = mopac_energies["molecule"].apply(lambda x: x.split("_")[1].split("-")[0])
mopac_energies.to_csv("mop_first.csv", index = False)

mopac_anion_energies = pd.read_csv('mopac-anion-energies.txt', sep = " ", header = 0)
mopac_anion_energies["Ligand"] = mopac_anion_energies["molecule"].apply(lambda x: x.split("_")[0])
mopac_anion_energies["AtomID"] = mopac_anion_energies["molecule"].apply(lambda x: x.split("_")[1].split("-")[1])
mopac_anion_energies["Tag"] = mopac_anion_energies["molecule"].apply(lambda x: x.split("_")[1].split("-")[0])
mopac_anion_energies["ligandX"] = mopac_anion_energies.apply(LigandY, axis = 1)
mopac_anion_energies.to_csv("mop_an_first.csv", index = False)


final_energy_df = pd.merge(mopac_energies, mopac_anion_energies, on = ["Ligand", 'Tag'])
final_energy_df = final_energy_df.drop_duplicates(subset = ["molecule_y"])

final_energy_df.to_csv("eneryggy.csv", index = False)

# final_oh = pd.read_csv("Final_Output_OH_OXYGEN_only.txt", sep = "\t", header = 0)
final_oh = pd.read_csv("Final_Output.txt", sep='\t', header = 0, index_col=False)
#print(final_oh)
final_oh["ligandX"] = final_oh.apply(LigandX, axis = 1)
min_distance = final_oh.groupby('ligandX')['Dist_from_Fe'].min()

final_oh = final_oh[final_oh["Dist_from_Fe"].isin(min_distance)]
# final_oh["ligandX"] = final_oh.apply(LigandXX, axis = 1)


final_oh.to_csv("finaOH.csv", index = False)
# exit()

final_merge = pd.merge(final_energy_df, final_oh, on = ["ligandX"])

final_merge.to_csv("finalk.csv", index = False)

final_merge["BDE"] = final_merge.apply(calc_final_energy, axis = 1)
final_merge["BDE_dist"] = final_merge.apply(calculate_BDE_Dist, axis = 1)


final_merge.to_csv("final_output.csv", index = False)
final_merge_X = final_merge.drop(columns = ["molecule_x","molecule_y", "mopacE_x", "mopacE_y", "ligandX", "Ligand_y", "Tag"])
final_merge_X.to_csv("Accesibility_Model_NEW.csv", index = False)
final_merge_X.rename(columns = {'Ligand_x':'Ligand'}, inplace = True)
final_merge_X["Substrate/Non-substrate"] = final_merge_X.apply(Dist_from_Fe, axis = 1)
final_merge_X["Site_of_sulphonation"] = final_merge_X.apply(isSite_of_sulphonation, axis = 1)

final_merge_X.to_csv("Accesibility_Model_NEW.csv", index = False)
#print(final_merge_X)
# changing code here
# Create a new DataFrame with selected columns
selected_columns = ["Ligand", "AtomNo", "Substrate/Non-substrate", "Site_of_sulphonation"]
final_selected_columns = final_merge_X[selected_columns]

# Write the final processed data to "Accesibility_Model_NEW.csv" file with selected columns
final_selected_columns.to_csv("Accesibility_Model_NEW.csv", index=False)

# Print the final DataFrame with selected columns
print(final_selected_columns)

