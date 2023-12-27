import gzip
from openeye import oechem

# Input and output file names for the first conversion
input_file1 = "fred_docked.oeb.gz"
output_file1 = "fred_docked.mol2.gz"

# Perform the first conversion: OEB to MOL2
ifs1 = oechem.oemolistream(input_file1)
ofs1 = oechem.oemolostream(output_file1)

for mol in ifs1.GetOEGraphMols():
    oechem.OEWriteMolecule(ofs1, mol)

ofs1.close()
ifs1.close()

# Unzip the final output file
unzipped_output_file = "fred_docked.mol2"
with gzip.open(output_file1, 'rb') as f_in:
    with open(unzipped_output_file, 'wb') as f_out:
        f_out.write(f_in.read())

print("Conversion completed successfully!")

