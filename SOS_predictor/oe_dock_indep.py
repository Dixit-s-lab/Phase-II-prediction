import os
import subprocess
import glob
"""
#SPRUCE getting pdb structure from rcsb
getstructure_command = ["getstructure", "2d06"]
subprocess.run(getstructure_command, check=True)

spruce_command = ["spruce", "-in", "2d06.cif", "-map", "2d06.mtz"]
subprocess.run(spruce_command, check=True)

receptorindu_command = ["receptorindu", "-in", "2D06_A__DU__EST_A-304.oedu", "-out", "rec_2d06.oedu"]
subprocess.run(receptorindu_command, check=True)
"""
#To dock a set of ligands into the receptor
database_file = glob.glob("*.oeb.gz")[0]
fred_command = ["fred", "-mpi_np", "4", "-receptor", "rec_2d06.oedu", "-dbase", database_file]
subprocess.run(fred_command, check=True)

#In addition to analyzing and visualizing the output from a docking run in VIDA, a summary PDF report can be generated using DockingReport.
docking_report_command = ["docking_report", "-docked_poses", "fred_docked.oeb.gz", "-receptor", "rec_2d06.oedu", "-report_file", "fred_docked_report.pdf"]
subprocess.run(docking_report_command, check=True)

