#Project Helix REGEX PATTERN ANALYZER v3.0
#Author: J Pearlson Job
import re
sequences = ["ATGCGTATGACGTAA","CCCATATGGCGT","GTGAAACCATGC","ATGCATGGTAG","GGATGGATGATGTGCCCTGA"]
start_codon_pattern = re.compile(r"^(ATG|GTG)")
stop_codon_pattern = re.compile(r"(TAA|TAG|TGA)$")
start_motifs_pattern = re.compile(r"(ATG|GTG)")
invalid_bases_pattern = re.compile(r"[^ATGC]")
print("===================================================================")
print("              PROJECT HELIX REGEX PATTERN ANALYZER v3.0")
print("===================================================================")
for seq in sequences:
    start_codon = start_codon_pattern.findall(seq)
    stop_codon = stop_codon_pattern.findall(seq)
    all_occurences = start_motifs_pattern.findall(seq)
    invalid_bases = invalid_bases_pattern.findall(seq)
    occurence=start_motifs_pattern.finditer(seq)
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
        for occur in occurence: 
                print(f"Start codon found at position: {occur.span()}")
    else:
        print("No start codons found in the sequence.")
    print(f"Invalid bases found: {invalid_bases}") 
    print("---------------------------------------------------------------")
