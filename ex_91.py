count = 0
dictionary_words = dict()
fhand = open('words.txt')
for line in fhand:
    words = line.split()
    for word in words:
        count += 1
        if word in dictionary_words:
            continue
        dictionary_words[word] = count

strCheck = input("Enter a word: ")


if strCheck in dictionary_words:
    print('True')
else:
    print('False')
