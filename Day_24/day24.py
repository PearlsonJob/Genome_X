#Project Helix DNA EXCEPTION ENGINE v1.0
#Author: J Pearlson Job
class InvalidDNAError(Exception):
    pass
def validate_dna(sequence):
    if not sequence:
        raise InvalidDNAError("The DNA sequence is empty. Please enter a valid sequence containing only A, T, G, and C.")
    elif not set(sequence).issubset("ATCG"):
        raise InvalidDNAError("The DNA sequence contains invalid base pair. Please enter a valid sequence containing only A, T, G, and C.")
    else:
        return True
for sample in ["ATGCGCTA","ATGXCGTA",""]:
    try:
        validate_dna(sample)
        print("The DNA sequence is valid.")
    except InvalidDNAError as e:
        print(f"Error: {e}")
    else:
        print("Processing the DNA sequence...")
    finally:
        print("Validation complete for sample:", sample)
