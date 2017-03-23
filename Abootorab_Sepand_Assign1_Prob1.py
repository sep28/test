#Sep Abootorab 01/30/17 Section 007 Using the Print Function

#Ask user to input 3 names
name1 = input ("Please enter name 1: ")
name2 = input ("Pleasue enter name 2: ")
name3 = input ("Please enter name 3: ")

#return the names in every possible order
print()
print ("Here are the names in every possible order: ")
print()
print ("1.", name1, name2, name3)
print ("2.", name1, name3, name2)
print ("3.", name2, name1, name3)

print()

print("4.")
print(name2)
print(name3)
print(name1)

print()

print("5.")
print(name3)
print(name2)
print(name1)

print()

print("6.")
print(name3)
print(name1)
print(name2)

print()

print(name1, name2, name3, sep="! ", end = "! ")

