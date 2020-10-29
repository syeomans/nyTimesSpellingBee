puzzle = input("What's the center letter? ")
puzzle += input("Type the other 6 letters (no commas or spaces): ")

infile = open("words.txt", "r")

legalWords = []
pangrams = []
for word in infile.readlines():
    word = word[:-1]
    islegal = True
    ispangram = True
    for letter in word:
        if letter not in puzzle:
            islegal = False
            break
    if islegal and puzzle[0] not in list(word):
        islegal = False
        continue
    if islegal:
        for letter in puzzle:
            if letter not in list(word):
                ispangram = False
                break
    if islegal:
        legalWords.append(word)
    if islegal and ispangram:
        pangrams.append(word)
        
print("\nLegal words:\n")
print(legalWords)
print("\nPangrams:\n")
print(pangrams)

