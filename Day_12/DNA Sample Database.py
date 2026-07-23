#Genome X University
#Project Helix DNA Sample Database
#Author: J Pearlson Job
print("==============================================")
print("      PROJECT HELIX DNA Sample Database ")
print("==============================================")
sample_id=int(input("Enter Your Sample ID:"))
species=input("Enter your Species:")
lab_name=input("Enter the name of your Laboratory:")
have_length=input("Do you have the length and the GC percentage of your sample(Yes?no)").upper()
if have_length=="YES" or have_length=='Y':
    dna_length=int(input("Enter your Sample DNA Length:"))
    gc_availabilty=input("Do you have the GC percentage?:(Yes/No)").upper()
    if gc_availabilty=="YES" or gc_availabilty=='Y':
        gc_percentage=float(input("Enter your GC Percentage:"))
    elif gc_availabilty=="NO" or gc_availabilty=='N':
        gcount=int(input("Enter the count of G in your DNA Sequence:"))
        ccount=int(input("Enter the count of C in your DNA Sequence:"))
        gc_count= gcount + ccount
        if dna_length!=0:
            gc_percentage= (gc_count/dna_length)*100
        else:
             print("Error! The DNA Lenght cannot be zero")
    detail={"Sample ID": sample_id, "Species":species, "DNA LENGTH": dna_length, "GC Percentage": gc_percentage,}
    if gc_percentage>=50:
            detail["Quality"]="High"
    else:
            detail["Quality"]="Low"
    detail["Laboratory name"]=lab_name
    for key,values in detail.items():
        print(key,":",values)
elif have_length=="NO" or have_length=='N':
    dna=input("Enter the DNA Sequence:\n").upper()
    dna_length=len(dna)
    base_count=dna.count("A")+dna.count("T")+dna.count("G")+dna.count("C")
    gc_count=dna.count('G')+dna.count('C')
    if dna_length!=0:
        gc_percentage= (gc_count/dna_length)*100
    else:
        print("Error! The DNA Lenght cannot be zero")
    if dna_length!=0:
        if base_count!=dna_length:
            if " " in dna:
                print("Please do not have any blanks or white spaces between the Sequence")
            else:
                print("Please enter only the bases of A/T/C/G")
        else:
            detail={"Sample ID": sample_id, "Species":species, "DNA LENGTH": dna_length, "GC Percentage": gc_percentage}
            if gc_percentage>=50:
                detail["Quality"]="High"
            else:
                detail["Quality"]="Low"
            detail["Laboratory name"]=lab_name
            for key,value in detail.items():
                    print(key,":",value)
    else:
        print("Enter the nucleotides Value!")
else:
    print("Enter either Yes/No!")


