#Project Helix DNA MOTIF SCANNER v1.0
#Author: J Pearlson Job
dna = "ATGCGATGTTATGCC"
dna1="ATG-CGA-TTA-GCC"
print("Sequence:", dna)
print("Sequence:", dna1)
print(dna.find("ATG"))
print(dna.count("ATG"))
print(dna1.split("-"))
print("|".join(dna1.split("-")))
