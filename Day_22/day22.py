#Project Helix MODULAR DNA ANALYSIS v2.0
#Author: J Pearlson Job
def validate_dna(sequence):
    l=len(sequence);count=0
    if l==0:
        return False
    else:
        for base in sequence:
            if base in ['A', 'T', 'G', 'C']:
                 count += 1
    if count==l:
        return True
    else:
        return False
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
def classify_gc(sequence):
    length, a_count, t_count, g_count, c_count, gc_count, gc_percentage=analyze_dna(sequence)
    if gc_percentage>=60.00:
        return "High GC content"
    elif gc_percentage>=40.00 and gc_percentage<60.00:
        return "Medium GC content"
    else:
        return "Low GC content"
def generate_report(sequence):
    check=validate_dna(sequence)
    if check==False:
        print("Invalid DNA sequence. Please enter a valid sequence containing only A, T, G, and C.")
    else:
        length,a_count,t_count,g_count,c_count,gc_count,gc_percentage=analyze_dna(sequence)
        gc_classification=classify_gc(sequence)
        print("===========================================================================")
        print("                       PROJECT HELIXX DNA REPORT")
        print("===========================================================================")
        print("DNA Sequence Report:")
        print("Length:", length)
        print(f"Base Counts: \n\t A: {a_count},\n\t T: {t_count},\n\t G: {g_count},\n\t C: {c_count}")
        print("GC Count:", gc_count)
        print(f"GC Percentage: {gc_percentage:.2f}%")
        print("GC Classification:", gc_classification)
        print("===========================================================================")
print("===========================================================================")
print("                PROJECT HELIX MODULAR DNA ANALYSIS v2.0")
print("===========================================================================")
dna_sequence=input("Enter a DNA sequence: ").upper()
generate_report(dna_sequence)
