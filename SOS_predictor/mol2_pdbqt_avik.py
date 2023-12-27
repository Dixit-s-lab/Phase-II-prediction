import os
import time
import subprocess
import datetime
from tqdm import tqdm
import shutil
for files in os.listdir("."):
    if files.endswith(".mol2"):
        # subprocess.run(["obabel", files, "-omol2", "-m"])
        subprocess.run(["obabel", "-imol2", files, "-opdbqt", "-O" + files.rstrip('.mol2') + ".pdbqt"])
