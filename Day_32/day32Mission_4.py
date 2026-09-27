# Project Helix DNA FILE ANALYZER v1.0 
# Author: J Pearlson Job
import json
samples = [{"ID": 101,"Species": "Human","DNA": "ATGCGTACGTAA"},
           {"ID": 102,"Species": "Mouse","DNA": "CCCATATGGCGT"},
           {"ID": 103,"Species": "Yeast","DNA": "GTGAAACCATGC"}]
with open("dna_databases.json","w") as file:
    json.dump(samples,file,indent=4)
with open("dna_databases.json","r") as file:
    data=json.load(file)
    for entry in data:
        print(f"Sample ID: {entry['ID']}\n Species: {entry['Species']}\n DNA: {entry['DNA']}")
        print("----------------------------------------")
        
