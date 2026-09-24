#Project Helix BIOLOGICAL SAMPLE DATABASE v1.0
#Author: J Pearlson Job
samples = [
    {"ID": 101, "Species": "Human", "Length": 2000, "GC": 52},
    {"ID": 102, "Species": "Mouse", "Length": 1500, "GC": 41},
    {"ID": 103, "Species": "Human", "Length": 3000, "GC": 67},
    {"ID": 104, "Species": "Yeast", "Length": 800, "GC": 38}]
high_gc_samples = [sample["Species"] for sample in samples if sample["GC"] >= 50]
large_samples = [sample["Length"] for sample in samples if sample["Length"] >= 2000]
count=0;low_gc_count=0;total_length=0;high_gc_count=0
for sample in samples:
    if sample["GC"]<50:
        low_gc_count+=1
        print("ID",sample["ID"],": Low GC")
    else:
        high_gc_count+=1
        print("ID",sample["ID"],": High GC")
    total_length+=sample["Length"]
    count+=1
average_length=total_length/len(samples)
human_lengths=[sample["Length"] for sample in samples if sample["Species"]=="Human"]
print("==============================================")
print("PROJECT HELIX BIOLOGICAL SAMPLE DATABASE v1.0")
print("==============================================")
print("Total Samples:", count)
print("Total DNA Length:",total_length)
print("Average DNA Length:",average_length)
print("\nLow GC Samples:", low_gc_count)
print("High GC Samples:", high_gc_count)
print("Human DNA Lengths:", human_lengths)
print("Large DNA Samples (Length >= 2000):", large_samples)
