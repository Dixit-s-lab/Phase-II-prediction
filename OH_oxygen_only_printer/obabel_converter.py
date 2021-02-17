import os
import subprocess


def converter():
    for files in os.listdir("."):
        if files.endswith(".pdbqt"):
            subprocess.run(["obabel", files, "-opdb", "-m"], check=True)
    for files in os.listdir("."):
        if files.endswith(".pdb"):
            #files = files.strip("pdb")
            #subprocess.run(["obabel", files, "-omol2", "-m", "-h"], check=True)
            subprocess.run(["obabel", files, "-o", "mol2", "-O", files.rstrip('pdb') + "mol2", "-h"], check=True)
    for files in os.listdir("."):
        if files.endswith(".pdb"):
            os.remove(files)


converter()

#pat = subprocess.run("pwd")
#k = os.path


def valency_checker():
    for f in os.listdir("."):
        if f. endswith(".mol2"):
            with open(f, "r") as fr:
                for line in fr:
                    line_list = Remove_unwanted_spaces(line)
                    print(line_list)
                    if line_list[0] == '@<TRIPOS>BOND':
                        break


def Remove_unwanted_spaces(line):
    line = line.strip(" \n")  # making each line of uniform length
    for j in range(7, 0, -1):
        line = line.replace(" " * j, "#")
        line_list = line.split("#")
    # print(line_list)
    # print(len(line_list))
    return line_list


valency_checker()
