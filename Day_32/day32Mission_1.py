#Project Helix DNA FILE READER v2.0
#Author: J Pearlson Job
print("===================================================")
print("       PROJECT HELIX DNA FILE READER v2.0")
print("===================================================")
with open("dna_samples.txt", "w") as file:
    samples=["ATGCGTACGTAA", "CCCATATGGCGT"]
    for sample in samples:
        file.write(f"{sample}\n")
with open("dna_samples.txt","a") as file:
    file.write("GTGAAACCATGC\n")
with open("dna_samples.txt", "r") as file:
    for line in file:
        print(f"Sequence: {line.strip()}")
    
