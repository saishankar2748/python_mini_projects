import random 
randNo = random.randint(1,3)

if randNo == 1:
    comp ="r"
elif randNo == 2:
    comp = "p"
elif  randNo == 3:
    comp = "s"


def game_win(comp,you):
    if comp == "r":
        if you == "p":
            return True
        elif you == "s":
            return False
        else:
            return None
    elif comp == "p":
        if you == "s":
            return True
        elif you == "r":
            return False
        else:
            return None
    elif comp == "s":
        if you == "r":
            return True
        elif you == "p":
            return False
        else:
            return None

you = input("Enter your wish: rock(r) or paper(p) or scissor(s)")

res = game_win(comp,you)
print("computer choose {} and you choose {}".format(comp,you))

if res == True:
    print("You win !!")
elif res == False:
    print("You loose, better luck next time")
else:
    print("match drawn")