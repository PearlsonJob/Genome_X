#Day 4 of becoming the best AI Computational Biologist and the Best Big Data Biologist/Scientist.
# Special Mission: PROJECT HELIX: Volunteer Bio-Profile Intake System
#Author: J Pearlson Job
print("=========================================================================")
print("PROJECT HELIX: Volunteer Bio-Profile Intake System v1.0")
print("\nTHANKS FOR VOLUNTEERING FOR PROJECT HELIX!")
print("=========================================================================")
name= input("\nVolunteer's name: ")
age= int(input("Volunteer's age: "))
gender= input("Volunteer's gender: ")
course= input("Volunteer's course of study: ")
institution= input("Volunteer's institution name: ")
field_of_interest= input("Volunteer's field of interest: ")
fav_molecule= input("Volunteer's favorite molecule in the body: ")
print("\n=========VOLUNTEER BIO-PROFILE=========")
print("Name:", name.upper())  
print("Age:", age)  
if age <0 or age >120:
    print("Enter a VALID AGE.")
elif age >100:
    print("Please Verify the age you have entered.")
elif age >60:
    print("The volunteer is a SENIOR CITIZEN.")
elif age >= 18:
    print("The volunteer is an ADULT.")
elif age < 18:
    print("The volunteer is a MINOR.")
future_age=int(input("Enter the age from now you like to see yourself in the future: "))
print("In the future, you will be", age + future_age, "years old.")
print("Gender:", gender.upper())
print("Course of Study:", course.upper())
print("Institution:", institution.upper())
print("Field of Interest:", field_of_interest.upper())
print("Favorite Molecule:", fav_molecule.upper())
if fav_molecule.upper() == "DNA":
    print("Note: DNA is the molecule that carries genetic information in living organisms.")
elif fav_molecule.upper() == "RNA":
    print("Note: RNA is the molecule that plays a key role in protein synthesis.")
elif fav_molecule.upper() == "PROTEIN":
    print("Note: Proteins are the molecular machines that perform most cellular functions. All enzymes are proteins, and they catalyze biochemical reactions in the cell.")
else:
    print("Note: That's an interesting molecule!")
    new_molecule = input("Please enter a short note about your favorite molecule: ")
    print("\nThanks for sharing your valuable information!")
    print(" Here's what you had to say about your favorite molecule:")
    print(new_molecule)
print("\nThank you for volunteering for PROJECT HELIX! Your bio-profile has been successfully recorded.")
print("We appreciate your contribution to the advancement of computational biology and big data science.")
print("Your information will be kept confidential and used solely for research purposes.")
print("We look forward to collaborating with you in the future!\n Have a Woderful Day!")
print("=========================================================================")
