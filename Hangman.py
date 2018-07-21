import random

animals = ['tiger', 'lion', 'duck', 'spider','dolphin','crab','monkey','tucan','ant']
colors = ['pink', 'purple', 'blue','green', 'yellow', 'turqoise', 'red', 'grey', 'navy']
#men = [hangman1, hangman2, hangman3, hangman4, hangman5, hangman6, hangman7]

def hangman1():
    print("╔════════════════════════╗       ")
    print("║                        ║       ")
    print("║                        ║       ")
    print("║                        ║       ")
    print("║                                ")
    print("║                                ")
    print("║                                ")
    print("║                                ")
    print("║                                ")
    print("║                                ")
    print("║                                ")
    print("║                                ")
    print("║                                ")
    print("║                                ")
    print("║                                ")
    print("║                                ")
    print("║                                ")
    print("╨─────────────────────────────   ")
def hangman2():
    print("╔════════════════════════╗       ")
    print("║                        ║       ")
    print("║                        ║       ")
    print("║                        ║       ")
    print("║                        _       ")
    print("║                      (• •)     ")
    print("║                                ")
    print("║                                ")
    print("║                                ")
    print("║                                ")
    print("║                                ")
    print("║                                ")
    print("║                                ")
    print("║                                ")
    print("║                                ")
    print("║                                ")
    print("║                                ")
    print("╨─────────────────────────────   ")
def hangman3():
    print("╔════════════════════════╗       ")
    print("║                        ║       ")
    print("║                        ║       ")
    print("║                        ║       ")
    print("║                        _       ")
    print("║                      (• •)     ")
    print("║                        │       ")
    print("║                        │       ")
    print("║                        │       ")
    print("║                        │       ")
    print("║                        │       ")
    print("║                                ")
    print("║                                ")
    print("║                                ")
    print("║                                ")
    print("║                                ")
    print("║                                ")
    print("╨─────────────────────────────   ")
def hangman4():
    print("╔════════════════════════╗       ")
    print("║                        ║       ")
    print("║                        ║       ")
    print("║                        ║       ")
    print("║                        _       ")
    print("║                      (• •)     ")
    print("║                        │       ")
    print("║                      / │       ")
    print("║                     /  │       ")
    print("║                    /   │       ")
    print("║                        │       ")
    print("║                                ")
    print("║                                ")
    print("║                                ")
    print("║                                ")
    print("║                                ")
    print("║                                ")
    print("╨─────────────────────────────   ")
def hangman5():
    print("╔════════════════════════╗       ")
    print("║                        ║       ")
    print("║                        ║       ")
    print("║                        ║       ")
    print("║                        _       ")
    print("║                      (• •)     ")
    print("║                        │       ")
    print("║                      / │\      ")
    print("║                     /  │ \     ")
    print("║                    /   │  \    ")
    print("║                        │       ")
    print("║                                ")
    print("║                                ")
    print("║                                ")
    print("║                                ")
    print("║                                ")
    print("║                                ")
    print("╨─────────────────────────────   ")
def hangman6():
    print("╔════════════════════════╗       ")
    print("║                        ║       ")
    print("║                        ║       ")
    print("║                        ║       ")
    print("║                        _       ")
    print("║                      (• •)     ")
    print("║                        │       ")
    print("║                      / │\      ")
    print("║                     /  │ \     ")
    print("║                    /   │  \    ")
    print("║                        │       ")
    print("║                       /        ")
    print("║                      /         ")
    print("║                                ")
    print("║                                ")
    print("║                                ")
    print("║                                ")
    print("╨─────────────────────────────   ")
def hangman7():
    print("╔════════════════════════╗       ")
    print("║                        ║       ")
    print("║                        ║       ")
    print("║                        ║       ")
    print("║                        _       ")
    print("║                      (• •)     ")
    print("║                        │       ")
    print("║                      / │\      ")
    print("║                     /  │ \     ")
    print("║                    /   │  \    ")
    print("║                        │       ")
    print("║                       / \      ")
    print("║                      /   \     ")
    print("║                                ")
    print("║                                ")
    print("║                                ")
    print("║                                ")
    print("╨─────────────────────────────   ")
men = [hangman2, hangman3, hangman4, hangman5, hangman6, hangman7]

print("                        ")
print("       WELCOME TO       ")
print("        HANGMAN         ")
print("________________________")
print(" Select your difficulty ")
unit = input("Easy, Medium or Hard ")
if unit == "Easy":
    unit2 = input("animals or colors ")
    if unit2 == "animals":
        randomanimal= animals[random.randint(0, len(animals))]
        #print(randomanimal)
        correctanswers = 0
        x = 0
        blank = []
        while x < len(randomanimal):
            blank.append("_")
            x += 1
        # print(blank.join(""))
        tries = 0
        while tries < 6:
            print(blank, tries)
            userletter = input ("pick a letter ")
            x = 0
            correct = False
            while x < len(randomanimal):
                if userletter == randomanimal[x]:
                    correct = True
                    blank[x] = userletter
                    break
                x += 1
            if correct:
                print("you got it right!")
                correctanswers += 1
            else:
                print("you got it wrong")
                men[tries]()
                tries += 1
            if correctanswers == len(randomanimal):
                print("YOU WIN!")
                break

            if tries == 6:
                print("YOU LOSE")

    if unit2 =="colors":
        randomcolor= colors[random.randint(0, len(colors))]
        #print(randomanimal)
        correctanswers = 0
        x = 0
        blank = []
        while x < len(randomcolor):
            blank.append("_")
            x += 1
        # print(blank.join(""))
        tries = 0
        while tries < 6:
            print(blank, tries)
            userletter = input ("pick a letter ")
            x = 0
            correct = False
            while x < len(randomcolor):
                if userletter == randomcolor[x]:
                    correct = True
                    blank[x] = userletter
                    break
                x += 1
            if correct:
                print("you got it right!")
                correctanswers += 1
            else:
                print("you got it wrong")
                men[tries]()
                tries += 1
            if correctanswers == len(randomcolor):
                print("YOU WIN!")
                break

            if tries == 6:
                print("YOU LOSE")


if unit == "Medium":
    unit3 = input("animals or colors ")
    if unit3 == "animals":
        randomanimal= animals[random.randint(0, len(animals))]
        #print(randomanimal)
        correctanswers = 0
        x = 0
        blank = []
        while x < len(randomanimal):
            blank.append("_")
            x += 1
        # print(blank.join(""))
        tries = 0
        while tries < 6:
            print(blank, tries)
            userletter = input ("pick a letter ")
            x = 0
            correct = False
            while x < len(randomanimal):
                if userletter == randomanimal[x]:
                    correct = True
                    blank[x] = userletter
                    break
                x += 1
            if correct:
                print("you got it right!")
                correctanswers += 1
            else:
                print("you got it wrong")
                men[tries]()
                tries += 1
            if correctanswers == len(randomanimal):
                print("YOU WIN!")
                break

            if tries == 6:
                print("YOU LOSE")

    if unit3 =="colors":
        randomcolor= colors[random.randint(0, len(colors))]
        #print(randomanimal)
        correctanswers = 0
        x = 0
        blank = []
        while x < len(randomcolor):
            blank.append("_")
            x += 1
        # print(blank.join(""))
        tries = 0
        while tries < 6:
            print(blank, tries)
            userletter = input ("pick a letter ")
            x = 0
            correct = False
            while x < len(randomcolor):
                if userletter == randomcolor[x]:
                    correct = True
                    blank[x] = userletter
                    break
                x += 1
            if correct:
                print("you got it right!")
                correctanswers += 1
            else:
                print("you got it wrong")
                men[tries]()
                tries += 1
            if correctanswers == len(randomcolor):
                print("YOU WIN!")
                break

            if tries == 6:
                print("YOU LOSE")


if unit == "Hard":
    unit4 = input("animals or colors ")
    if unit4 == "animals":
        randomanimal= animals[random.randint(0, len(animals))]
        #print(randomanimal)
        correctanswers = 0
        x = 0
        blank = []
        while x < len(randomanimal):
            blank.append("_")
            x += 1
        # print(blank.join(""))
        tries = 0
        while tries < 6:
            print(blank, tries)
            userletter = input ("pick a letter ")
            x = 0
            correct = False
            while x < len(randomanimal):
                if userletter == randomanimal[x]:
                    correct = True
                    blank[x] = userletter
                    break
                x += 1
            if correct:
                print("you got it right!")
                correctanswers += 1
            else:
                print("you got it wrong")
                men[tries]()
                tries += 1
            if correctanswers == len(randomanimal):
                print("YOU WIN!")
                break

            if tries == 6:
                print("YOU LOSE")

    if unit4 =="colors":
        randomcolor= colors[random.randint(0, len(colors))]
        #print(randomanimal)
        correctanswers = 0
        x = 0
        blank = []
        while x < len(randomcolor):
            blank.append("_")
            x += 1
        # print(blank.join(""))
        tries = 0
        while tries < 6:
            print(blank, tries)
            userletter = input ("pick a letter ")
            x = 0
            correct = False
            while x < len(randomcolor):
                if userletter == randomcolor[x]:
                    correct = True
                    blank[x] = userletter
                    break
                x += 1
            if correct:
                print("you got it right!")
                correctanswers += 1
            else:
                print("you got it wrong")
                men[tries]()
                tries += 1
            if correctanswers == len(randomcolor):
                print("YOU WIN!")
                break
            if tries == 6:
                print("YOU LOSE")