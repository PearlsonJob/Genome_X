#Genome X University
#Project Helix
#Author: J Pearlson Job
print("==============================================")
print("   PROJECT HELIX DNA BATCH STORAGE SYSTEM ")
print("==============================================")
dna_lengths=[1200, 980, 1500, 2100, 750]
print("DNA SAMPLES LOADED SUCCESSFULLY!")
add_dna=input("WOULD YOU LIKE TO ADD ANOTHER DNA SAMPLE'S LENGTH ?\n(YES/NO)")
if add_dna.lower()=="yes":
    new_dna=int(input("PLEASE ENTER THE NEW DNA SAMPLE'S LENGTH:"))
    dna_lengths.append(new_dna)
    print("THE TOTAL DNA SAMPLES PRESENT ARE ",len(dna_lengths))
else:
    print("YOU HAVE OPTED TO NOT ADD ANY NEW DNA SAMPLE'S LENGTH")
    print("THE TOTAL DNA SAMPLES PRESENT ARE ",len(dna_lengths))
sample=0
for length in dna_lengths:
    sample=sample+1
    print("DNA SAMPLE",sample,":",length)
average_length=sum(dna_lengths)/len(dna_lengths)
print("THE LONGEST DNA STRAND :",max(dna_lengths))
print("THE SHORTEST DNA STRAND :",min(dna_lengths))
print("THE AVERAGE LENGTH OF THE DNA SAMPLES PRESENT:", average_length)
if average_length> 1500:
    print("HIGH QUALITY DNA BATCH")
else:
    print("STANDARD DNA BATCH")
