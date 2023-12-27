import os
import subprocess

print("Renaming files")

#################################_CREATING SEPARATE INPUT FILES FOR TANIMOTO CALCULATION_#################
"""
for files in os.listdir("."):
    if files.endswith(".sdf"):
        newname = files.rstrip('.sdf')
        with open(files) as f:
            line = f.readlines()
        subprocess.run(["rm", "-rf", newname + "_IN" + ".sdf"])
        with open(newname + "_IN" + ".sdf", "w") as f:
            f.writelines(line)
"""
###################################_CHANGING THE NAME OF THE HEADER OF SDF FILE_############################
for files in os.listdir("."):
    if files.endswith(".sdf"):
        name = files.rstrip('.sdf')
        # print(name) PRINTING THE OLD NAME
        with open(files) as f:
            line = f.readlines()
            # print(line[0])
            line[0] = name + "\n"
            # print(line[0], "\n") PRINTING THE NEW NAME
        with open(files, "w") as f:
            f.writelines(line)
