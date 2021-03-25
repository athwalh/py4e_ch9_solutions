#Exercise 3: Write a program to read through a mail log,
#build a his- togram using a dictionary to count how many messages have
#come from each email address, and print the dictionary.


f1 = input("Enter File: ")
emails = []
counts = dict()

try:
    fhand = open(f1)
except:
    print("File could not be processed")
    exit()

for line in fhand:
    line = line.rstrip()
    if not line.startswith("From "): continue
    word = line.split()
    emails.append(word[1])

for mail in emails:
    if mail not in counts:
        counts[mail] = 1
    else:
        counts[mail] += 1

print(counts)
