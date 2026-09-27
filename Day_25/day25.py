#Project Helix DNA EXCEPTION ENGINE v2.0
#Author: J Pearlson Job
class DNAError(Exception):
    pass

class EmptyDNAError(DNAError):
    pass

class InvalidDNAError(DNAError):
    pass
def validate_dna(sequence):
    if not sequence:
        raise EmptyDNAError(f"The DNA sequence {sequence} is empty. Please enter a valid sequence containing only A, T, G, and C.")
    elif not set(sequence).issubset("ATCG"):
        raise InvalidDNAError(f"The DNA sequence {sequence} contains invalid base(s). Please enter a valid sequence containing only A, T, G, and C.")
    else:
        return True
samples = ["ATGCGCTA","ATGXCGTA",""]
for sample in samples:
    try:
        validate_dna(sample)
    except EmptyDNAError as e:
        print(f"Error: {e}")
    except InvalidDNAError as e:
        print(f"Error: {e}")
    else:
        print("Processing the DNA sequence...")
    finally:
        print("Validation complete for sample:", sample)
