#PROJECT HELIX: DNA Quality Checker
#Author: J Pearlson Job
print("=========================================================================")
print("                 PROJECT HELIX: DNA Quality Checker v1.0")
print("=========================================================================")
dna_length=int(input("Enter the total length of the DNA fragment in base pairs (bp): "))
start_codon=input("Is a start codon present?(yes/no):")
if dna_length <= 0 or dna_length > 1000000 :
    print("Invalid input for the DNA length.")
else:
    if dna_length > 300 and dna_length % 3 == 0 and start_codon.lower() =="yes":
        print("The DNA fragment is of HIGH QUALITY CODING SEQUENCE.")
    elif start_codon.lower()!="yes":
        print("No Start Codon Detected")
    else:
        print("The DNA fragment's Sequence required further analysis.")
        if dna_length <= 300 and dna_length % 3 != 0:
           print("The Sequence is too short and is also not divisible by 3")
        elif dna_length <= 300:
           print("The Sequence is too short.Please enter a value greater than 300")
        elif dna_length % 3 != 0:
            print("The Sequence is not divisible by 3")
