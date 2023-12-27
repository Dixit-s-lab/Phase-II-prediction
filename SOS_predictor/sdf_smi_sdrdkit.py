import os
import sys
from rdkit import Chem
from rdkit.Chem import AllChem

# List of .sdf files
sdf_files = [file for file in os.listdir() if file.endswith(".sdf")]

for file in sdf_files:
    # Read the molecule from the .sdf file
    mol = Chem.MolFromMolFile(file)
    # Generate the canonical smiles representation of the molecule
    canon_smi = Chem.MolToSmiles(mol)
    # Write the canonical smiles to a .smi file with the same name as the .sdf file
    with open(file.rstrip(".sdf") + ".smi", "w") as f:
        f.write(canon_smi)

# Get the list of all .smi files in the current directory
smi_files = [file for file in os.listdir() if file.endswith(".smi")]

for file in smi_files:
    # Read the SMILES string from the file
    with open(file, "r") as f:
        smiles = f.read().strip()

    # Convert the SMILES string to a RDKit molecule object
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        print(f"Unable to parse SMILES string from {file}")
        continue

    # Convert the isomeric SMILES string to a canonical SMILES string
    canon_smiles = Chem.MolToSmiles(mol, isomericSmiles=False)

    # Replace the isomeric SMILES string with the canonical SMILES string in the file
    with open(file, "w") as f:
        f.write(canon_smiles)

    # Convert the RDKit molecule object to a 2D SDF file with the same name as the input file
    Chem.MolToMolFile(mol, file.rstrip(".smi") + ".sdf", includeStereo=False, kekulize=True)

    # Convert the RDKit molecule object to a 3D SDF file with the same name as the input file
    mol = Chem.AddHs(mol)
    AllChem.EmbedMolecule(mol)
    Chem.MolToMolFile(mol, file.rstrip(".smi") + ".sdf", includeStereo=False, kekulize=True)

