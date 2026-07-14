# Day 05 of becoming the best AI Computational Biologist and the Best Big Data Biologist/Scientist.
# Exercise : Calculations based of the input of 2 Different DNA Fragments
#Author: J Pearlson Job
print("=========================================================================")
DNA1_length=int(input("Enter the total length of the first DNA fragment in base pairs (bp): "))
DNA2_length=int(input("Enter the total length of the second DNA fragment in base pairs (bp): "))
total_length=DNA1_length + DNA2_length
print ("\n=========DNA LENGTH CALCULATOR=========")
print("\nThe total length of the DNA fragments is:", total_length, "base pairs.")
choice=input("Would you like to calculate the difference in length between the two DNA fragments? (yes/no): ")
if choice.lower() == "yes":
    length_difference=abs(DNA1_length - DNA2_length)
elif choice.lower() == "no":
     length_difference="Not calculated"
     print("OK, you chose not to calculate the difference in length.")
else:
     length_difference="Not calculated"
     print("Invalid input. Please enter 'yes' or 'no'.")
choice=input("Would you like to calculate the product of the lengths of the two DNA fragments? (yes/no): ")
if choice.lower() == "yes":
        length_product=DNA1_length * DNA2_length
elif choice.lower() == "no":
        length_product="Not calculated"
        print("OK, you chose not to calculate the product of the lengths.")
else:
        length_product="Not calculated"
        print("Invalid input. Please enter 'yes' or 'no'.") 
choice=input("Would you like to calculate the ratio of the lengths of the two DNA fragments? (yes/no): ")
if choice.lower() == "yes":
    if DNA2_length != 0:
        length_ratio=DNA1_length / DNA2_length
    else:
        length_ratio="Not calculated"
        print("Cannot calculate ratio: The length of the second DNA fragment is zero.")
elif choice.lower() == "no":
        length_ratio="Not calculated"
        print("OK, you chose not to calculate the ratio of the lengths.")
else:
        length_ratio="Not calculated"
        print("Invalid input. Please enter 'yes' or 'no'.")  
codon_count=total_length // 3
remaining_bases=total_length % 3
print("=========================================================================")
print("\n====================DNA LENGTH CALCULATOR RESULTS======================")
print("=========================================================================")
print("Total length :", total_length)    
print("Difference :", length_difference )
print("Product :", length_product)
print("Ratio :", length_ratio)
print("Codon count :", codon_count)
print("Remaining bases :", remaining_bases)
if remaining_bases == 0:
    print("STATUS:\n         The total length of the DNA fragments is divisible by 3, so there are no remaining bases.")
else:
    print("STATUS:\n         The total length of the DNA fragments is not divisible by 3, so there are", remaining_bases, "remaining bases.")

print("Thank you for using the DNA Length Calculator. Goodbye!")
print("=========================================================================")
