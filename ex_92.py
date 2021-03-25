#Exercise 2: Write a program that categorizes each mail message by which day of the week
#the commit was done. To do this look for lines that start with “From”, then look for the
#third word and keep a running count of each of the days of the week. At the end of the
#program print out the contents of your dictionary (order does not matter).
#Sample Line:
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Sample Execution:
#python dow.py
#Enter a file name: mbox-short.txt
#{'Fri': 20, 'Thu': 6, 'Sat': 1}

f1 = input("Enter File: ")
dates = []
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
    dates.append(word[2])

for days in dates:
    if days not in counts:
        counts[days] = 1
    else:
        counts[days] += 1

print(counts)
