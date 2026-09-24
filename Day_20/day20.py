#Project Helix DNA CLASSIFICATION ENGINE v1.0
#Author: J Pearlson Job
print("==============================================")
print(" PROJECT HELIX DNA CLASSIFICATION ENGINE v1.0")
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
def classify_gc(sequence):
    length, a_count, t_count, g_count, c_count, gc_count, gc_percentage=analyze_dna(sequence)
    if gc_percentage>=60.00:
        return "High GC content"
    elif gc_percentage>=40.00 and gc_percentage<=59.99:
        return "Medium GC content"
    else:
        return "Low GC content"
def classify_length(sequence):
    length, a_count, t_count, g_count, c_count, gc_count, gc_percentage=analyze_dna(sequence)
    if length>=1000:
        return "Long DNA sequence"
    else:
        return "Short DNA sequence"
dna_samples = ["ATGCGCTA","ATATATAT","GGCGCGGC","ATGC","GCGCGC","AATGCCGGTT"]
count=1;total_bases=0;higher_gc=[];lower_gc=[];medium_gc=[];lowcount=0;highcount=0;mediumcount=0
highest_gc_percentage=0.00;lowest_gc_percentage=100.00;average_dna_length=0.00
long_dna_count=0;short_dna_count=0;long_dna=[];short_dna=[]
longest=0;shortest=1000
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
    gc_classification=classify_gc(dna)
    length_classification=classify_length(dna)
    count+=1
    if gc_percentage>highest_gc_percentage:
        highest_gc_percentage=gc_percentage
        high=dna
    if gc_percentage<lowest_gc_percentage:
        lowest_gc_percentage=gc_percentage
        low=dna
    if gc_classification=="High GC content":
        higher_gc.append(dna)
        highcount+=1
    elif gc_classification=="Medium GC content":
        medium_gc.append(dna)
        mediumcount+=1
    else:
        lower_gc.append(dna)
        lowcount+=1
    if length_classification=="Long DNA sequence":
        long_dna_count+=1
        long_dna.append(dna)
        print("This DNA sample is classified as a Long DNA sequence.")  
    else:
        short_dna_count+=1
        short_dna.append(dna)
        print("This DNA sample is classified as a Short DNA sequence.")
    if length > longest:
        longest = length
    if length < shortest:
        shortest = length
    average_dna_length+=length
    total_bases+=length
average_dna_length/=len(dna_samples)
print("==============================================")
print("               ANALYSIS SUMMARY")
print("==============================================")
print("Highest GC percentage:", highest_gc_percentage, "%")
print("Lowest GC percentage:", lowest_gc_percentage, "%")
print("Average DNA length:", average_dna_length)
print("Longest DNA sequence:", longest)
print("Shortest DNA sequence:", shortest)
print("Total Long DNA sequences (>= 1000 bases):", long_dna_count)
print("Long DNA sequences (>= 1000 bases):", long_dna)
print("Total Short DNA sequences (< 1000 bases):", short_dna_count)
print("Short DNA sequences (< 1000 bases):", short_dna)
print("Total bases analyzed:", total_bases)
print("DNA Sample with Highest GC percentage:", high)
print("DNA Sample with Lowest GC percentage:", low)
print("Total High Quality DNA Samples (GC% >= 60):", highcount)
print("High Quality DNA Samples (GC% >= 60):", higher_gc)
print("Total Medium Quality DNA Samples (GC% >= 40 and < 60):", mediumcount)
print("Medium Quality DNA Samples (GC% >= 40 and < 60):", medium_gc)
print("Total Low Quality DNA Samples (GC% < 40):", lowcount)
print("Low Quality DNA Samples (GC% < 40):", lower_gc)
print("==============================================")
