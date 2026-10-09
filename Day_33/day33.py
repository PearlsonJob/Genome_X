#Project Helix JSON DATABASE MODIFIER v1.0
#Author: J Pearlson Job
import json
def lengthcalc(seq):
    return len(seq)

with open("dna_databases.json", "r") as file:
    datas = json.load(file)

for sample in datas:
    sample["Length"] = lengthcalc(sample["DNA"])

with open("dna_databases_updated.json", "w") as new_file:
    json.dump(datas, new_file, indent=4)

print("JSON database successfully updated.")

for sample in datas:
    print(f"Sample ID: {sample['ID']}")
    print(f"Species: {sample['Species']}")
    print(f"DNA: {sample['DNA']}")
    print(f"Length: {sample['Length']} bp")
    print("----------------------------------------")
