with open("wordlist.txt", "r") as f:
    wordlist = sorted(word.strip(",")
for line in f for word in line.split())

def guessWord(word):
    first_guess = "salet"
    letterdict = {}
    final = "01234"
    strlist = ""
    bestscore = 0
    bestword = ""
    guesses = 1



    for x in range(5):
        if first_guess[x] == word[x]:
            final = final.replace(str(x), first_guess[x])
            for item in wordlist:
                if first_guess[x] != item[x]:
                    wordlist.remove(item)
        elif first_guess[x] in word:
            for item in wordlist:
                if first_guess[x] == item[x]:
                    wordlist.remove(item)
            for item in wordlist:
                if first_guess[x] not in item:
                    wordlist.remove(item)
        else:
            for item in wordlist:
                if first_guess[x] in item:
                    wordlist.remove(item)

    for i in wordlist:
        strlist = strlist + i
    for item in strlist:
        if item in letterdict:
            letterdict[item] += 1
        else:
            letterdict[item] = 1

    for z in wordlist:
        currword = list(z)
        currscore = 0
        for y in currword:
            currscore += letterdict[y]
        if currscore > bestscore:
            bestscore = currscore
            bestword = z


    while final != word:
        letterdict = {}
        strlist = ""
        currguess = bestword
        for x in range(5):
            if currguess[x] == word[x]:
                final = final.replace(str(x), currguess[x])
                for item in wordlist:
                    if first_guess[x] != item[x]:
                        wordlist.remove(item)
            elif currguess[x] in word:
                for item in wordlist:
                    if currguess[x] == item[x]:
                        wordlist.remove(item)
                for item in wordlist:
                    if currguess[x] not in item:
                        wordlist.remove(item)

        bestscore = 0
        bestword = ""

        for i in wordlist:
            strlist = strlist + i
        for item in strlist:
            if item in letterdict:
                letterdict[item] += 1
            else:
                letterdict[item] = 1

        for z in wordlist:
            currword = list(z)
            currscore = 0
            for y in currword:
                currscore += letterdict[y]
            if currscore > bestscore:
                bestscore = currscore
                bestword = z
        guesses += 1

    print(final)
    print(guesses)


guessWord("store")
