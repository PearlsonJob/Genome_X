#Project Helix DNA BATCH FILTER
#Author: J Pearlson Job
dna_lengths=[450,1200,750,1800,950,2100,600]
print ("==============================================")
print ("        PROJECT HELIX DNA BATCH FILTER ")
print ("==============================================")
count=0
total=0
average=0
specialset=[]
print("THE DNA SAMPLES LENGTHS ARE:")
for length in dna_lengths:
    print(length)
    if length >= 1000:
        count+=1
        specialset.append(length)
        total+=length

print("==============================================")
print("The list of all DNA Samples are:", dna_lengths)
print("The list of DNA Samples with length >= 1000 are:", specialset)
print("Number of DNA samples with length >= 1000:", count)
print("Total length of DNA samples with length >= 1000:", total)
if count > 0:
    average = total / count
    print("Average length of DNA samples with length >= 1000:", average)
    print("The Longest DNA sample length in the special set is:", max(specialset))
    print("The Shortest DNA sample length in the special set is:", min(specialset))
