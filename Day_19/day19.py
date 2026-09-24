#Project Helix MULTI-DNA BATCH ANALYZER
#Author: J Pearlson Job
print("==============================================")
print("   PROJECT HELIX MULTI-DNA BATCH ANALYZER")
print("==============================================")
def analyze_dna(sequence):
    length=len(sequence)
    a_count=sequence.count("A")
    t_count=sequence.count("T")
    g_count=sequence.count("G")
    c_count=sequence.count("C")
    gc_count=g_count+c_count
    gc_percentage=((gc_count/length)*100)
    return length, a_count, t_count, g_count, c_count,gc_count, gc_percentage
dna_samples=["ATGCGCTA","ATATATAT","GGCGCGGC","ATGC","GCGCGC"]
count=1;total_bases=0;high_quality=[];low_quality=[];lowcount=0;highcount=0
highest_gc_percentage=0;lowest_gc_percentage=100;average_dna_length=0
for dna in dna_samples:
    length, a_count, t_count, g_count, c_count, gc_count, gc_percentage=analyze_dna(dna)
    print("==============================================")
    print("DNA Sample", count)
    print("DNA Sequence:", dna)
    print("Length of DNA sequence:", length)
    print("Count of A:", a_count)
    print("Count of T:", t_count)
    print("Count of G:", g_count)
    print("Count of C:", c_count)
    print("Total GC count:", gc_count)
    print("GC percentage:", gc_percentage, "%")
    count+=1
    if gc_percentage>highest_gc_percentage:
        highest_gc_percentage=gc_percentage
        high=dna
    if gc_percentage<lowest_gc_percentage:
        lowest_gc_percentage=gc_percentage
        low=dna
    if gc_percentage>=50:
        high_quality.append(dna)
        highcount+=1
    else :
        low_quality.append(dna)
        lowcount+=1
    average_dna_length+=length
    total_bases+=length
average_dna_length/=len(dna_samples)
print("==============================================")
print("               ANALYSIS SUMMARY")
print("==============================================")
print("Highest GC percentage:", highest_gc_percentage, "%")
print("Lowest GC percentage:", lowest_gc_percentage, "%")
print("Average DNA length:", average_dna_length)
print("Total bases analyzed:", total_bases)
print("DNA Sample with Highest GC percentage:", high)
print("DNA Sample with Lowest GC percentage:", low)
print("Total High Quality DNA Samples (GC% >= 50):", highcount)
print("High Quality DNA Samples (GC% >= 50):", high_quality)
print("Total Low Quality DNA Samples (GC% < 50):", lowcount)
print("Low Quality DNA Samples (GC% < 50):", low_quality)
print("==============================================")
