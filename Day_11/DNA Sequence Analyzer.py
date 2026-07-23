#Genome X University
#Project Helix DNA Sequence Analyzer
#Author: J Pearlson Job
print("==============================================")
print("      PROJECT HELIX DNA SEQUENCE ANALYZER ")
print("==============================================")
dna=input("Enter the DNA Sequence:\n").upper()
dna_length=len(dna)
base_count=dna.count("A")+dna.count("T")+dna.count("G")+dna.count("C")
if dna_length!=0:
    if base_count!=dna_length:
     if dna.count(" ")>0:
            print("Please do not have any blanks or white spaces between the Sequence")
     else:
        print("Please enter only the bases of A/T/C/G")
    else:
        if dna.startswith("ATG"):
            print("\nSTART CODON DETECTED")
        else:
            print("\nNO START CODON FOUND")
        print("Your DNA sequence was analyzed!\n Here is the DNA sequence you entered for reference:",dna)
        print("The length of the DNA Sequence entered is",dna_length)
        print("The count of Adenosine:",dna.count("A"))
        print("The count of Thymine:",dna.count("T"))
        print("The count of Guanine:",dna.count("G"))
        print("The count of Cytosine:",dna.count("C"))
        gc_count= dna.count("G") + dna.count("C")
        print("The GC Count:",gc_count)
        gc_percentage= (gc_count/dna_length)*100
        print("The GC percentage in the DNA:",gc_percentage)
        if gc_percentage>=50:
            print("HIGH GC COUNT")
        else:
            print("LOW GC COUNT")
else:
    print("The DNA Sequence cannot be Blank!")
