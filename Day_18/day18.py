#Project Helix MODULAR DNA ANALYSIS
#Author: J Pearlson Job
def analyze_dna(sequence):
    length = len(sequence)
    a_count = sequence.count('A')
    t_count = sequence.count('T')  
    g_count = sequence.count('G')
    c_count = sequence.count('C') 
    gc_count = g_count + c_count
    gc_percentage = (gc_count / length) * 100
    return length, a_count, t_count, g_count, c_count, gc_count, gc_percentage
dna=input("Enter a DNA sequence: ").upper()
bases=['A', 'T', 'G', 'C']
validity=True
if len(dna)==0:
    print("DNA SEQUENCE CANNOT BE EMPTY. PLEASE ENTER A VALID DNA SEQUENCE.")
else:
    for base in dna:
        if base not in bases:
            validity=False
            break
if validity==True:
    length, a_count, t_count, g_count, c_count, gc_count, gc_percentage = analyze_dna(dna)
    print("============DNA Sequence Analysis============")
    print("Length of DNA sequence:", length)
    print("Count of A:", a_count)
    print("Count of T:", t_count)
    print("Count of G:", g_count)
    print("Count of C:", c_count)
    print("Total GC count:", gc_count)
    print("GC percentage:", gc_percentage, "%")
else:
    print("Invalid DNA sequence. Please enter a valid sequence containing only A, T, G, and C.")    
