# PROJECT HELIX DNA SAMPLE COUNTER
# Author: Pearlson Job J  
print ("Welcome to Genome X DNA Sample counter")
sample_count=int(input("How many DNA Samples are there?\n"))
count=0
if sample_count >0:
    while count<sample_count:
        count=count+1            
        print("Processing DNA Sample",count, "of",sample_count)
    print ("All",sample_count,"DNA Samples have been processed successfully")
elif sample_count<=0:
    print("Invalid Entry.Please Enter a Valid Sample count")
