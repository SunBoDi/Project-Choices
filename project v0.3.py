option1 = []
option2 = []
question = ""
choice = ""

def journey():
    global option1, option2, choice, question
    if len(option1) == 0:
        print("This game is based on yes or no choices.")
        print("At the end of each scene, choose and type 'yes' or 'no' to continue,")
        print("unless instructed otherwise.")
        print("If you die, you must start over.")
        print("Make sure to read EVERYTHING.")
        game_start = input("Are you ready to begin?: ")
        if game_start == "yes":
            option1.append(1)
        else:
            exit()
    if len(option1) == 1:
        space()
        print("You're reaching the end of your life.")
        print("You can feel it in your weary bones and weak muscles.")
        print("But before you kick the bucket, there are some things you want to do.")
        name = input("But first, what is your name?: ")
        space()
        print("You, " + name + ", wish to go on an adventure.")
        print("You pack quickly, taking only the essentials and the little money you have left.")
        print("You head for the town square and there you meet a caravan.")
        print("For the entirety of your wallet, the caravan agrees to take you north with them.")
        print("You remember the tales of the elders, about sasquatches and yetis")
        print("in the nothern mountains.")
        question = ("Do you want to go with the caravan?: ")
        decision()
    if len(option1) == 2:
        print("Yes")
    if len(option2) == 1:
        print("no")

    
def space():
    print("")

def time_jump():
    print("")
    print("")
    print("                    Some time later...                    ")
    print("")
    print("")

def decision():
    global option1, option2, choice, question
    while choice != "yes" or "no":
        choice = input(question)
        if choice == "yes":
            option1.append(1)
            break
        if choice == "no":
            option2.append(1)
            break
            
journey()
