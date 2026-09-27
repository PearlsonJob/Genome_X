#Project Helix DNA CLASSIFICATION ENGINE v1.0
#Author: J Pearlson Job
print("===================================================")
print("   PROJECT HELIX DNA CLASSIFICATION ENGINE v1.0")
print("===================================================")
samples = [
    {"ID": 101, "Species": "Human", "DNA": "ATGCGCGCTA"},
    {"ID": 102, "Species": "Mouse", "DNA": "ATATGCGCAA"},
    {"ID": 103, "Species": "Yeast", "DNA": "GGCCGCGG"},
    {"ID": 104, "Species": "Human", "DNA": "ATATATAT"}]
def validate_dna(sequence):
    if len(sequence) == 0:
        return False
    if not set(sequence).issubset("ATGC"):
        return False
    else:
        return True
def analyze_dna(sequence):
    length = len(sequence)
    a_count = sequence.count("A")
    t_count = sequence.count("T")
    g_count = sequence.count("G")
    c_count = sequence.count("C")
    gc_count = g_count + c_count
    gc_percentage = (gc_count / length) * 100
    return length, a_count, t_count, g_count, c_count, gc_count, gc_percentage
def classify_gc(gc_percentage):
    if gc_percentage>=60:
        return "High GC Content"
    elif gc_percentage >= 40 :
        return "Medium GC Content"
    else:
        return "Low GC Content"
def generate_report(samples):
    sample_count = len(samples)
    valid_samples = 0;invalid_samples = 0;highest_gc = 0;lowest_gc = 100;avg_length = 0
    for sample in samples:
        if validate_dna(sample["DNA"]):
            length, a_count, t_count, g_count, c_count, gc_count, gc_percentage = analyze_dna(sample["DNA"])
            content=classify_gc(gc_percentage)
            print(f"Sample {sample['ID']} | {sample['Species']} | Length: {length} bp | GC: {gc_percentage:.2f}% | {content}")
            valid_samples += 1
            if gc_percentage > highest_gc:
                highest_gc = gc_percentage
            if gc_percentage < lowest_gc:
                lowest_gc = gc_percentage
            avg_length += length
        else:
            invalid_samples += 1
    if valid_samples > 0:
        avg_length /= valid_samples
    print("===================GENOME X SUMMARY=====================")
    print(f"Total Samples: {sample_count}")
    print(f"Valid Samples: {valid_samples}")
    print(f"Invalid Samples: {invalid_samples}")
    print(f"Average Length: {avg_length:.2f} bp")
    print(f"Highest GC : {highest_gc:.2f}%")
    print(f"Lowest GC : {lowest_gc:.2f}%")
generate_report(samples)
