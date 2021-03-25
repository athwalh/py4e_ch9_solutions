#Exercise 4: Add code to the above program to figure out who has the most messages in the
#file. After all the data has been read and the dictionary has been created, look
#through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops) to
#find who has the most messages and print how many messages the person has.

f1 = input("Enter File: ")
emails = []
counts = dict()
maxima = None

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

for key in counts:
    if maxima is None or counts[key] > maxima :
        maxima = counts[key]
        largestMail = key

print(largestMail,maxima)
