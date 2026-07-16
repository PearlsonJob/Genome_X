#Project Helix- DNA Reporter
#Author: J Pearlson Job
def display_title():
    print("===================================")
    print("     PROJECT HELIX DNA REPORTER")
    print("===================================")
def analyze_sample(sample_number):
    count=1
    for count in range(1,sample_number+1):
        print("Analyzing DNA Sample",count,"of",sample_number,"Sample(s)")
        if count%2==0:
            print("TYPE:EVEN")
        else:
            print("TYPE:ODD")
sample_number=int(input("How many DNA Samples do you want to analyze?\n"))
display_title()
analyze_sample(sample_number)
print("DNA Report Complete !")
    
