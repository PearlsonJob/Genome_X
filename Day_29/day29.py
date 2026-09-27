#Project Helix REGEX PATTERN ANALYZER v2.0
#Author: J Pearlson Job
import re
sequences = ["ATGCGTACGTAA","CCCATGCGT","GTGAAACCC","ATGCGTAG","GGGTGCCCTGA"]
print("===================================================================")
print("              PROJECT HELIX REGEX PATTERN ANALYZER v2.0")
print("===================================================================")
for seq in sequences:
    start_codon = re.findall("^(ATG|GTG)", seq)
    stop_codon = re.findall("(TAA|TAG|TGA)$", seq)
    all_occurences = re.findall("(ATG|GTG)+", seq)
    invalid_bases = re.findall("[^ATGC]", seq)
    print(f"Sequence: {seq}")
    if start_codon:
        print("Start codon found: YES")
    else:
        print("Start codon found: NO")
    if stop_codon:
        print("Stop codon found: YES")
    else:
        print("Stop codon found: NO")        
    if all_occurences:
        print(f"All occurrences of start codons: {all_occurences}")
    else:
        print("No start codons found in the sequence.")
    print(f"Invalid bases found: {invalid_bases}") 
    print("---------------------------------------------------------------")
