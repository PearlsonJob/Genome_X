#PROJECT HELIX DNA BATCH ANALYZER
#Author: J Pearlson Job
print("Welcome to DNA BATCH ANALYZER v1.0")
sample_count=int(input("How many DNA samples are available?\n"))
if sample_count >0:
    for count in range(1,sample_count+1):
        print ("Analyzing DNA Sample",count,'of',sample_count) 
        if count%2==0:
            print("TYPE:EVEN")
        else:
            print("TYPE:ODD")
    print("DNA Batch Analysis of",sample_count,"Samples are Complete")
else:
    print("Invalid Entry! Please enter a VALID SAMPLE COUNT")
