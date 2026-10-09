import json

DB_FILE = "dna_databases_updated.json"

try:
    with open(DB_FILE, "r") as file:
        datas = json.load(file)
except FileNotFoundError:
    print(f"Error: {DB_FILE} not found. Please check file path.")
    exit()

print("===================================================")
print("🧬 PROJECT HELIX JSON DATABASE MODIFIER v1.1")
print("===================================================\n")

update = input(" Would you like to update a sample dictionary for a particular ID? (Y/N): ").strip().upper()

if update == "Y":
    try:
        id_to_be_changed = int(input("Enter the ID of the sample you want to update: "))
    except ValueError:
        print("Invalid input! ID must be an integer.")
        exit()
        
    target_sample = next((sample for sample in datas if sample["ID"] == id_to_be_changed), None)
    
    if target_sample:
        field_mode = input("Would you like to update the whole sample data or just a field? (WHOLE/FIELD): ").strip().upper()
        
        if field_mode == "FIELD":
            user_choice = input("Enter the field you want to update (Species/DNA/Length): ").strip().lower()
            
            mapping = {"dna": "DNA", "species": "Species", "length": "Length"}
            input_field = mapping.get(user_choice, user_choice)
            
            if input_field in target_sample:
                if input_field == "Length":
                    auto_calc = input("Auto-calculate length from existing DNA? (Y/N): ").strip().upper()
                    if auto_calc == "Y":
                        target_sample["Length"] = len(target_sample["DNA"])
                    else:
                        target_sample["Length"] = int(input("Enter custom length in bp: "))
                elif input_field == "DNA":
                    new_dna = input("🧬 Enter the new DNA sequence: ").strip()
                    target_sample["DNA"] = new_dna
                    target_sample["Length"] = len(new_dna)  # Automatically update paired length
                else:
                    target_sample[input_field] = input(f"Enter the new value for {input_field}: ").strip()
                
                print(f"\n{input_field} updated successfully for sample ID {id_to_be_changed}.")
            else:
                print(f"Field '{input_field}' does not exist in the sample data.")
                exit()

        elif field_mode == "WHOLE":
            target_sample["Species"] = input("Enter the new species name: ").strip()
            new_dna = input("🧬 Enter the new DNA sequence: ").strip()
            target_sample["DNA"] = new_dna
            
            length_available = input("Do you want to auto-calculate the DNA length? (Y/N): ").strip().upper()
            if length_available == "Y":
                target_sample["Length"] = len(new_dna)
            else:
                target_sample["Length"] = int(input("📏 Enter custom length of the DNA sequence: "))
                
            print(f"\nSample ID {id_to_be_changed} completely updated.")
        
        else:
            print("Invalid input. Please enter 'WHOLE' or 'FIELD'.")
            exit()
            
        with open(DB_FILE, "w") as new_file:
            json.dump(datas, new_file, indent=4)
            
        print("\n--- UPDATED SAMPLE SUMMARY ---")
        print(f"Sample ID: {target_sample['ID']}")
        print(f"Species:   {target_sample['Species']}")
        print(f"DNA:       {target_sample['DNA']}")
        print(f"Length:    {target_sample['Length']} bp")
        print("------------------------------")
        
    else:
        print(f"No sample found with ID {id_to_be_changed}.")

elif update == "N":
    print("No updates made to the database. Exiting.")
else:
    print("Invalid input. Please enter 'Y' or 'N'.")
