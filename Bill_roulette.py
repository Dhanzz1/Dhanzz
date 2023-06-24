import random
names_string = input("Give me everybody's names, separated by a comma\n")
names = names_string.split(", ")
payer = names[random.randint(0, len(names))-1]
print(f"The person who pays is {payer}")

##  Simplified code
##  random_choice = random.choice(names)
##  print(f"The person who pays is {random_choice}")
