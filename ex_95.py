#Exercise 5: This program records the address name (instead of the address) where the message
# was sent from instead of who the mail came from (i.e., the whole email address).
#At the end of the program, print out the contents of your dictionary.

f1 = input("Enter File: ")
emails = dict()



try:
    fhand = open(f1)
except:
    print("File could not be processed")
    exit()

for line in fhand:
	if line.startswith('From '):
		line = line.split()
		email = line[1]
		email = email.split('@')
		address = email[1]
		emails[address] = emails.get(address,0) + 1
print (emails)
