import time
options = ["potato", "test", "cheese", "spam", "eggs"]
global userinput

def difficultyselect():
    global userinput
    while True:
        userinput = input("Please select a difficulty, easy or hard: ")
        userinput = userinput.lower().strip()
        if userinput in ("easy", "hard"):
            break
        else:
            print("Please enter a valid difficulty")
            continue

def easy():
        global easydoinput
        print(*options, sep = ", ")
        while True:
            easydoinput = input("Please enter an option from the list above: ")
            easydoinput = easydoinput.lower().strip()
            if easydoinput in options:
                break
            else:     
                print("Please enter a valid option")
                continue        

def easydo():
    easyanswer = input(f"Is {easydoinput} what you were thinking of? ")
    easyanswer = easyanswer.lower().strip()
    if easyanswer == "yes":
        print("Knew it!")
    else:
        print("What the hell?")

def harddo():
    global indexalpha
    indexalpha = 0
    print(*options, sep = ", ")
    print("Please think of an option from the list above")
    time.sleep(4)
    while True:
        print(f"Is your option {options[indexalpha]}?")   
        isyours = input("Please enter yes or no: ")
        isyours = isyours.lower().strip()
        if isyours == "yes":
            print("Knew it! Good game.")                    #ADD PLAY AGAIN FEATURE
            break
        elif isyours == "no":
            indexalpha = indexalpha + 1
            continue


#END OF FUNCTION DEFINITIONS

difficultyselect()
if userinput == "easy":
    easy()
    easydo()


if userinput == "hard":
    harddo()