#Project Helix DNA FILE READER v2.0 Mission 2
#Author: J Pearlson Job
print("===================================================")
print("       PROJECT HELIX DNA FILE READER v2.0")
print("===================================================")
with open("dna_samples.txt", "r") as file:
    whole_file_read = file.read()
    file.seek(0)
    seq1 = file.readline()
    file.seek(0)
    seq2 = file.readline()
    file.seek(0)
    whole_file_readlines = file.readlines()
    file.seek(0)
    print(f"========READ()============\n{whole_file_read}")
    print(f"=======READLINE()=========\nSequence 1: {seq1}\nSequence 2: {seq2}")
    print(f"=======READLINES()========\n{whole_file_readlines}")
    print("=======LINE IN FILE=========")
    for line in file:
        print(f"Sequence: {line.strip()}")
