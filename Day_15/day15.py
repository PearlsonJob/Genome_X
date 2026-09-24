#Project Helix SAFE DNA REPORT GENERATOR v2.0
#Author: J Pearlson Job
print("==============================================")
print(" PROJECT HELIX SAFE DNA REPORT GENERATOR v2.0 ")
print("==============================================")
try:
    id=input("Sample ID:")
    species=input("Species:")
    dna_length=int(input("DNA Length:"))
    gc_percentage=float(input("GC Percentage:"))
    if gc_percentage>=50:
        quality="High"
    else:
        quality="Standard"
    with open("dna report file.txt","w") as file:
        file.write(f"Sample ID:{id}\n")
        file.write(f"Species:{species}\n")
        file.write(f"DNA Length:{dna_length}\n")
        file.write(f"GC Percentage:{gc_percentage}\n")
        file.write(f"Quality:{quality}\n")
    with open("dna report file.txt","r") as file:
        content=file.read()
        print(content)
    another=input("Would you like to save another report?\n").upper()
    if another=="YES" or another=="Y":
        print("Feature coming soon...")
        print("File saved Successfully!")
    elif another=="NO" or another=="N":
        print("File saved successfullly!")
    else:
        print("Enter either \"Yes\" or \"No\"")
except ValueError:
    print("Error! Please type in a proper integer or a decimal number")
