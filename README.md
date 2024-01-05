# Site of Sulphonation (SOS) Predictor

# 1. Introduction
Sulphonation is an important Phase II metabolic reaction catalyzed by a set of sulphotransferase isoforms. Approximately 20 % of FDA-approved drugs undergo Phase II metabolism, and thus, predicting the potential SULT substrates and SOS is essential for small-molecule drug discovery, toxicology, and chemical biology. The SOS Predictor leverages accessibility and reactivity-based algorithms to predict substrate potential and sulphonation sites accurately. The SOS Predictor is a tool designed to classify a query molecule with OH group as a substrate or nonsubstrate along with sites of sulphonation (SOS) in a potential substrate. All the datasets used for model development, like substrate and nonsubstrate along with validation are available in an sdf file format.

# Features
* Substrate Prediction: Determine whether a given molecule will likely be a SULT substrate.
* Site Identification: Identification of potential sites of sulphonation within the molecule.
* User-Friendly Interface: Easy installation and intuitive usage, making it accessible to both beginners and experts.

# 2. System Requirements
Before you begin, ensure that your system meets the following requirements:
* OS: Linux
* Python 3.6 or later
* Dependencies specified in the requirements.txt file
To ensure the seamless operation of the SOS Predictor, the dependencies (software) specified in the requirements.txt file must be installed correctly and available in the user path (.bashrc file). Additionally, it is recommended to set up a Conda environment that accommodates various essential Python libraries. If you haven't already installed Conda, you can obtain it from the official website at https://www.anaconda.com/. Detailed instructions for the Conda installation are available there.

# 3. Installation 
Follow these steps to install SOS Predictor:
1. Download the Phase-II-prediction-main directory or clone the directory using "gh repo clone Dixit-s-lab/Phase-II-prediction" and extract the contents by executing the command "unzip Phase-II-prediction-main.zip."
2. Navigate to the project directory using the command: "cd SOS-Predictor."
3. Install the necessary dependencies by running the "pip install -r requirements.txt" command. 
Alternatively, manually install each specified dependency. If opting for manual installation, ensure to update the path in the .bashrc file accordingly.

# 4. Usage
After installing all the software and dependencies along with updating the path in the .bashrc file, follow these steps to perform SOS Prediction on the test molecule.
1. Place a single molecule in the SDF format inside the SOS_predictor directory, for example, dopamine. sdf. Ensure that this molecule contains at least one OH group; otherwise, the tool will not provide any predictions.
2. Execute the following command to run SOS Predictor:
3. python SOS_single_ligand.py
4. The tool will generate a Results directory inside the SOS-Predictor, which contains the SOS prediction results Ligand, AtomNo, Substrate/Non-substrate, and Site_of_sulphonation in CSV format. The same results will also be displayed on the terminal.

# 5. License
SOS_predictor is available under the Creative Commons license and is free for academic research groups working in a degree-granting university/institute. Any work/report/thesis/research-article/review-article resulting from using SOS_predictor should properly cite the software and associated publication. For commercial usage of SOS Predictor, please contact us at vaibhavadixit@gmail.com or vaibhav@niperguwahati.in

# 6. Developer
This tool is developed by Shivam Kumar Vyas (PhD Research Scholar) under the supervision of Dr. Vaibhav A. Dixit, Asst. Prof., Dept. of Med. Chem., NIPER Guwahati in the Advanced Center of Computer-Aided Drug Design (A-CADD). SOS_predictor, GUI, websites, tools, layouts, and logos are subject to copyright protection and are the exclusive property of the Department of Medicinal Chemistry, NIPER Guwahati. The name and logos of the NIPER Guwahati website must not be associated with publicity or business promotion without NIPER G's prior written approval.

# 7. Troubleshooting
If you encounter any issues or errors during installation or usage, please contact us at vyasshivam16@gmail.com or vaibhavadixit@gmail.com. 
