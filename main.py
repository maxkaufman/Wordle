with open("wordlist.txt", "r") as f:
    copy = sorted(word.strip(",")
for line in f for word in line.split())



def guessWord(word):
    first_guess = "salet"
    letterdict = {}
    strlist = ""
    bestscore = 0
    bestword = ""
    guesses = 1
    wordlist = copy.copy()
    newwordlist = []

    for x in range(5):
        if first_guess[x] == word[x]:
            for i in range(len(wordlist)):
                item = wordlist[i]
                if len(item) > 1 and first_guess[x] != item[x]:
                    wordlist[i] = "0"
        elif first_guess[x] in word:
            for i in range(len(wordlist)):
                item = wordlist[i]
                if len(item) > 1 and first_guess[x] == item[x]:
                    wordlist[i] = "0"
            for i in range(len(wordlist)):
                item = wordlist[i]
                if len(item) > 1 and first_guess[x] not in item:
                    wordlist[i] = "0"
        else:
            for i in range(len(wordlist)):
                item = wordlist[i]
                if len(item) > 1 and first_guess[x] in item:
                    wordlist[i] = "0"

    for i in wordlist:
        if i != "0":
            newwordlist.append(i)

    for i in newwordlist:
        strlist = strlist + i
    for item in strlist:
        if item in letterdict:
            letterdict[item] += 1
        else:
            letterdict[item] = 1

    for z in newwordlist:
        currword = list(z)
        currscore = 0
        for y in currword:
            currscore += letterdict[y]
        if currscore > bestscore:
            bestscore = currscore
            bestword = z

    guesses += 1
    while bestword != word:
        wordlist = newwordlist
        looplist = []
        letterdict = {}
        strlist = ""
        currguess = bestword
        for x in range(5):
            if currguess[x] == word[x]:
                for i in range(len(wordlist)):
                    item = wordlist[i]
                    if len(item) > 1 and currguess[x] != item[x]:
                        wordlist[i] = "0"
            elif currguess[x] in word:
                for i in range(len(wordlist)):
                    item = wordlist[i]
                    if len(item) > 1 and currguess[x] == item[x]:
                        wordlist[i] = "0"
                for i in range(len(wordlist)):
                    item = wordlist[i]
                    if len(item) > 1 and currguess[x] not in item:
                        wordlist[i] = "0"
            else:
                for i in range(len(wordlist)):
                    item = wordlist[i]
                    if len(item) > 1 and currguess[x] in item:
                        wordlist[i] = "0"

        for i in wordlist:
            if i != "0":
                looplist.append(i)

        bestscore = 0
        bestword = ""

        for i in looplist:
            strlist = strlist + i
        for item in strlist:
            if item in letterdict:
                letterdict[item] += 1
            else:
                letterdict[item] = 1

        for z in looplist:
            currword = list(z)
            currscore = 0
            for y in currword:
                currscore += letterdict[y]
            if currscore > bestscore:
                bestscore = currscore
                bestword = z
        guesses += 1
    return guesses

def simulation():
    count = 0
    g1 = 0
    g2 = 0
    g3 = 0
    g4 = 0
    g5 = 0
    g6 = 0
    g7 = 0
    g8 = 0
    g9 = 0
    g10 = 0
    total = 0
    for i in copy:
        simguess = guessWord(i)
        total += simguess
        count += 1
        if simguess == 1:
            g1 += 1
        elif simguess == 2:
            g2 += 1
        elif simguess == 3:
            g3 += 1
        elif simguess == 4:
            g4 += 1
        elif simguess == 5:
            g5 += 1
        elif simguess == 6:
            g6 += 1
        elif simguess == 7:
            g7 += 1
        elif simguess == 8:
            g8 += 1
        elif simguess == 9:
            g9 += 1
        elif simguess == 10:
            g10 += 1


    print('1 -> ' + str(g1) + "\n" + '2 -> ' + str(g2) + "\n" + '3 -> ' + str(g3) + "\n" + '4 -> ' + str(g4) + "\n" + '5 -> ' + str(g5) + "\n" + '6 -> ' + str(g6) + "\n" + '7 -> ' + str(g7) + "\n" + '8 -> ' + str(g8) + "\n" + '9 -> ' + str(g9) + "\n" + '10 -> ' + str(g10) + "\n" + "avg -> " + str(total/count))

simulation()
