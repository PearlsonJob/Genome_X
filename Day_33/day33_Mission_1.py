#Project Helix JSON DATABASE MODIFIER v1.0
#Author: J Pearlson Job
import json
stock_sample={"ID":104,"Species":"E.coli","DNA":"ATGCGCGTAA"}

def lengthcalc(seq):
    return len(seq)

with open ("dna_databases_updated.json","r") as file:
    datas = json.load(file)
print("===================================================")
print("    PROJECT HELIX JSON DATABASE MODIFIER v1.0")
print("===================================================\n")
answer = (input("Would you like to add a new DNA sample to the database or use a stock sample? (OWN/STOCK)")).upper()
if answer == "OWN":
    new_sample = {}
    new_sample["ID"] = int(input("Enter the sample ID: "))
    new_sample["Species"] = input("Enter the species name: ")
    new_sample["DNA"] = input("Enter the DNA sequence: ")
    length_available =input("Do you want to calculate the length of the DNA sequence? (Y/N)").upper()
    if length_available == "Y":
        new_sample["Length"] = lengthcalc(new_sample["DNA"])
    elif length_available == "N":
        new_sample["Length"] = int(input("Enter the length of the DNA sequence: "))
    datas.append(new_sample)
    with open("dna_databases_updated.json", "w") as new_file:
        json.dump(datas, new_file, indent=4)
    print("New DNA sample added successfully.")
elif answer == "STOCK":
    stock_sample["Length"] = lengthcalc(stock_sample["DNA"])
    datas.append(stock_sample)
    with open("dna_databases_updated.json", "w") as new_file:
        json.dump(datas, new_file, indent=4)
    print("Stock DNA sample added successfully.")
else:
    print("Invalid input. Please enter 'OWN' or 'STOCK'.")
with open("dna_databases_updated.json", "r") as file:
    datas = json.load(file) 
print("\nUpdated JSON database:")
print("---------------------------------------")
for sample in datas:
    print(f"Sample ID: {sample['ID']}")
    print(f"Species: {sample['Species']}")
    print(f"DNA: {sample['DNA']}")
    print(f"Length: {sample['Length']} bp")
    print("----------------------------------------")
