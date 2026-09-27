#Project Helix REGEX MOTIF DETECTOR v1.0
#Author: J Pearlson Job
import re

dna = "CCCATGCGTATGAAATGCCC"

motif = "ATG"

match = re.search(motif, dna)

print("First occurrence:", match.group())
print("Starting position:", match.start())
print("Ending position:", match.end())

print("All occurrences:", re.findall(motif, dna))

for match in re.finditer(motif, dna):
    print("Match:", match.group(), "| Start:", match.start(), "| End:", match.end())

test_sequence = "ATGXCGZTA"

print("Valid bases:", re.findall("[ATGC]", test_sequence))
print("Invalid bases:", re.findall("[^ATGC]", test_sequence))
