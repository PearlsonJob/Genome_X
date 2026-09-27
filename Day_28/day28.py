#Project Helix REGEX PATTERN ANALYZER v1.0
#Author: J Pearlson Job
import re
dna = "ATGAAATTTCCCAAAATGCGT"
match=re.findall("[ATGC]", dna)
print(match)
runs_of_a = re.findall("A+", dna)
print(runs_of_a)
exact_a = re.findall("A{3}", dna)
print(exact_a)
cons_a=re.findall("A{2,4}", dna)
print(cons_a)
wildcard=re.findall("A.G", dna)
print(wildcard)
test_sequence = "ATGXCGZT"
invalid=re.findall("[^ATGC]", test_sequence)
print(invalid)
