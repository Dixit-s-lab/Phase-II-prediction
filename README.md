# Site of Sulphonation (SOS) Predictor

# 1. Introduction
Welcome to SOS Predictor, a tool designed to predict the potential of a query molecule to be a substrate and identify sites of sulphonation (SOS) in potential substrates. Sulphonation is an important Phase II metabolic reaction catalyzed by a set of sulphotransferase isoforms. Approximately 20 % of FDA-approved drugs undergo Phase II metabolism and thus prediction of the potential SULT substrates and SOS is essential for small-molecule drug discovery, toxicology, and chemical biology. The SOS Predictor leverages accessibility and reactivity-based algorithms to accurately predict substrate potential and sulphonation sites.

# Features
* Substrate Prediction: Determine whether a given molecule is likely to be a substrate for SULT.
* Site Identification: Identification of potential sites of sulphonation within the molecule.
* User-Friendly Interface: Easy installation and intuitive usage, making it accessible to both beginners and experts.

# 2. System Requirements
Before you begin, ensure that your system meets the following requirements:
* OS: Linux
* Python 3.6 or later
* Dependencies specified in the requirements.txt file
To ensure the seamless operation of the SOS Predictor, it requires the dependencies (software) specified in the requirements.txt file to be installed correctly and be available in the user-path (.bashrc file). Additionally, it is recommended to set up a Conda environment that accommodates various essential Python libraries. If you don't already have Conda installed, you can obtain it from the official website at https://www.anaconda.com/. Detailed instructions for the Conda installation are available there.

# 3. Installation 
Follow these steps to install SOS Predictor:
1. Download the Phase-II-prediction-main directory or clone the directory using "gh repo clone Dixit-s-lab/Phase-II-prediction" and extract the contents by executing the command "unzip Phase-II-prediction-main.zip"
2. Navigate to the project directory using the command: "cd SOS-Predictor"
3. Install the necessary dependencies by running "pip install -r requirements.txt" command. 
Alternatively, manually install each specified dependency. If opting for manual installation, ensure to update the path in the .bashrc file accordingly.

# 4. Usage
After installing all the software and dependencies along with updating the path in the .bashrc file follow these steps to perform SOS Prediction on test molecule.
1. Keep the single molecule in the sdf format inside the SOS_predictor directory e.g., dopamine.sdf.
2. Open the SOS_single_ligand.py in gedit or vim text editor, and change the SOS-Predictor directory path in line 22 and save this file.
3. Execute the following command to run SOS Predictor:
4. python SOS_single_ligand.py
5. The tool will generate a Results directory inside the SOS-Predictor which contains the SOS prediction results molecule name, atom no, class prediction, and site prediction in csv format.

# 5. License
SOS_predictor is available under the Creative Commons license and is free for academic research groups working in a degree-granting university/institute. Any work/report/thesis/research-article/review-article resulting from the use of SOS_predictor should properly cite the software and publication associated with the same. For commercial usage of SOS Predictor, please contact us at vaibhavadixit@gmail.com or vaibhav@niperguwahati.in

# 6. Developer
This tool is developed by Shivam Kumar Vyas (PhD Research Scholar) under the supervision of Dr. Vaibhav A. Dixit, Asst. Prof., Dept. of Med. Chem., NIPER Guwahati in the Advanced Center of Computer-Aided Drug Design (A-CADD). SOS_predictor, GUI, websites, tools, layouts, and logos are subject to copyright protection and are the exclusive property of the Department of Medicinal Chemistry, NIPER Guwahati. The name and logos of the NIPER Guwahati website must not be associated with publicity or business promotion without NIPER G's prior written approval.

# 7. Troubleshooting
If you encounter any issues or errors during installation or usage, please contact us at vyasshivam16@gmail.com or vaibhavadixit@gmail.com. 
