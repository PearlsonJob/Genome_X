#Project Helix DNA FILE READER v1.0
#Author: J Pearlson Job
import os
print("Current Working Directory:", os.getcwd())
print("===================================================")
print("       PROJECT HELIX DNA FILE READER v1.0")
print("===================================================")
with open("dna_samples.txt", "w") as file:
    samples = ["ATGCGTACGTAA","CCCATATGGCGT","GTGAAACCATGC","ATGCATGGTAG","GGATGGATGATGTGCCCTGA"]
    for sample in samples:
        file.write(f"{sample}\n")
with open("dna_samples.txt", "r") as file:
    for line in file:
        sequence = line.strip()
        print(f"Sequence: {sequence}")
