# Project Helix DNA FILE ANALYZER v1.0
# Author: J Pearlson Job
print("===================================================")
print("       PROJECT HELIX DNA FILE ANALYZER v1.0")
print("===================================================")
class FileNotFoundError(Exception):
    pass
class InvalidDNASequenceError(Exception):
    pass
def validate_dna(sequence):
    if len(sequence) == 0:
        raise InvalidDNASequenceError("DNA sequence cannot be empty.")
    if not set(sequence).issubset("ATGC"):
        raise InvalidDNASequenceError("Invalid DNA sequence. Only A, T, G, and C are allowed.")
    return True

def analyze_dna(sequence):
    length=len(sequence)
    a_count=sequence.count("A")
    t_count=sequence.count("T")
    g_count=sequence.count("G")
    c_count=sequence.count("C")
    gc_count=g_count+c_count
    if length==0:
        gc_percentage=0.00
    else:
        gc_percentage=((gc_count/length)*100)
    return length, a_count,t_count, g_count,c_count,gc_count,gc_percentage
try:
    with open("dna_samples.txt", "r") as file:
        for line in file:
            sequence = line.strip()
            try:
                if validate_dna(sequence):
                    length, a_count, t_count, g_count, c_count, gc_count, gc_percentage = analyze_dna(sequence)
                    print(f"Sequence: {sequence}")
                    print(f"Length: {length} bp")
                    print(f"A Count: {a_count}")
                    print(f"T Count: {t_count}")
                    print(f"G Count: {g_count}")
                    print(f"C Count: {c_count}")
                    print(f"GC Count: {gc_count}")
                    print(f"GC Percentage: {gc_percentage:.2f}%")
            except InvalidDNASequenceError as e:
                print(f"Error in sequence {sequence}: {e}")
            print("----------------------------------------")
except FileNotFoundError:
    print("Error: 'dna_samples.txt' file not found.")
finally:
    print("===================================================")
    print("       PROCESS HALTED - END OF FILE ANALYSIS")
    print("===================================================")
