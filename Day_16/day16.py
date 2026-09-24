#Project Helix DNA Mathematical Analyzer
#Author: J Pearlson Job
print("==============================================")
print("   PROJECT HELIX DNA Mathematical Analyzer ")
print("==============================================")
import random
bases=["A","T","G","C"]
dna_seq=""
dna_length=int(input("Enter the length of the DNA Sequence to be generated:"))
if dna_length > 0:
    for i in range (dna_length):
        dna_seq=dna_seq+random.choice(bases)
print("Generated DNA Sequence:", dna_seq)
print("DNA Sequence Length:", dna_length)
print("A count:",dna_seq.count("A"))
print("T count:",dna_seq.count("T"))
print("G count:",dna_seq.count("G"))
print("C count:",dna_seq.count("C"))
gc_count= dna_seq.count("G") + dna_seq.count("C")
print("The GC Count:",gc_count)
gc_percentage= (gc_count/dna_length)*100
print("The GC percentage in the DNA:",gc_percentage)
if gc_percentage > 50:
    print("The DNA sequence is of Rich GC content")
else:
    print("The DNA sequence is of Low GC content")
