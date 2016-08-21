from sys import exit
import random

def prologue():
    print ("\n\tYou wake up in a mystery place")
    print ("\t You don't know were you are")
    print ("\n\nYou found a note")
    print ("You found a sword")
    print Main_beginning()


def Main_beginning():
    inventory = ["Sword"]
    next = raw_input("\n*Writte Read*  ")
    if next == "Read":
        print ("\n\nHELP ME!")
        print Beginning()

    elif next == "inventory":
        print inventory

    else:
        print("\nWhat?")
        print Main_beginning()


def Beginning():
    print ("\n\nYou are in a Dark place, There are three ways to go")
    next = raw_input("Town, Cementery, Dungeon ")
    if next == "Town":
        print Town()

    elif next == "Cementery":
        print Cementery()

    elif next == "Dungeon":
        print Dungeon()

    elif next == "final":
        print final()

    else:
        print ("\nWhat?")
        print Beginning()

def final():
    print ("\n\tYou've defeat the Minotaurus, Cthulhu, and the Giant Spider")
    next = raw_input("Final room ahead *Type final*")
    if next == "final":
        print FinalRoom()

def FinalRoom():
    print ("\n\tNow you're in the final room")
    print ("\n\tThe Titan has awoken")
    print ("\nTitan:Oh, you apeared, This was just a test for you, Take this code: X313F-R2SF1-4F1S4-AX4BR-43GGD\nAnd you will recive every simgle thing is steam")
    print ("\nGaben: Thanks man, you saved my life, that MOTHERF*CKING GIANT, kindnaped me and brought me here to this abyss")
    print ("\nGaben: I think you should kill him")
    print ("\nTitan: Hahaha, Nice joke m8, really funny and now go fuck yourselfe")
    print ("\nIt's not a joke this little man came from far far away to rescute me, he defeat every enemy and now he is here, infront of you.")
    print ("\nGabem: What do you think you will fight him?")
    next = raw_input("*yes or no* ")
    if next == "yes":
        dead("Dude, It's a MOTHERF*CKING TITAN.")
    else:
        print ("\nTITAN: Little man, you're really smart.")
        print ("\nTITAN: Remember i'm a MOTHERF*CKING TITAN, No body can defeat me, but now, we are friend")
        print ("\nTITAN: Hey, Gaben, Sorry for kindnaped you, i just wawnted some Dota 2 items")
        print ("\n\n\t\tShitty Final, Good Job.")
        dead("End?")


def Town():
    town_key = False
    print ("\nNow you are in the town")
    next = raw_input("Go *up, left or right* ")
    def Town_up():
        print ("\n*You kept walking to forward ")
        print ("You saw a knight and now he will fight you")
        next = raw_input("Will fight *yes or no* ")

        if next == "yes":
            print ("\nYou won the fight and there is a note")
            next = raw_input("Pick it up? *yes or no* ")


            if next == "yes":
                print ("\nour boss is the the castle, i think he is really hangry")
                next = raw_input("You need to go back *Type back* ")

                if next == "back":
                    print Town()


            else:
                print ("Ok, Now you are in the main village of the Town")
                print Town()
        else:
            print ("\n\tYou died")
            print Beginning()

    def Town_left():
        print("\nYou turn left")
        print("There are three guards")
        next = raw_input("What will you do? *fight, stealth, run* ")
        if next == "fight":
            print("\nYou are strong!!")
            print("You found a key")
            next = raw_input("Take it?")
            if next == "yes":
                print ("*Now you a have the key of the castle*")
                next = raw_input("*Type back* ")
                print Town()
            else:
                print("\nYou needed that key. Ok We're going again")
                print Town_left()
        elif next == "stealth":
            print ("\nOne knight have a key")
            next = raw_input("Select one *G1, G2, G3* ")
            if next == "G2":
                print("\nOk, you got the key")
                next = raw_input("*Now type back*")
                print Town()
            else:
                print("\n\tYou died")
                print Beginning()

        elif next == "run":
            print("\nYOU ARE A FUCKING PUSSY. Ok, Restarting...")
            print Town_left()

    def Town_right():
        print("\n There is a Giant castle")
        next = raw_input("Enter to the castle? ")
        if next == "yes":
            print Castle()
        else:
            print("\nFucking pussy")
            print Town_right()

    def Castle():
        print("\n\tThe Minotaurus has awaken")
        print("\nPrepare to fight")
        print Minotaurus()

    def Minotaurus():
        print ("'My name is Minotaurus and i'll kill BECAUSE I'M BORED")
        print ("*Minotaurus is running to you*")
        next = raw_input("\n*roll right, Jump* ")
        if next == "roll left":
            print ("\nDodged Now ATTACK")
            next = raw_input("*Type ATTACK* ")
            if next == "ATTACK":
                print ("\n*The Minotaurus got just a little bit of damage*")
                print ("Find another way to kill him")
                print ("\n*There is candle in the roof go to the rope and cut it*")

        elif next == "roll right":
            print ("\nDodged, Now ATTACK")
            next = raw_input("*Type ATTACK* ")
            if next == "ATTACK":
                print ("\n*The Minotaurus got just a little bit of damage*")
                print ("Find another way to kill him")
                print ("\n*There is candle in the roof go to the rope and cut it*")
                print ("\nCareful the Minotaurus is looking you")
                next = raw_input("Run to the candle or Dodge the Minotaurus *run or dodge*")
                if next == "run":
                    print ("Keep running to the candle")
                    next = raw_input("\nThe Minotaurus is running to you, Keep running? *yes* ")
                    if next == "yes":
                        print ("\nNow you are infront of the rope and the Minotaurus is under the candle")
                        next = raw_input("Dodge it *Type Dodge* ")
                        if next == "Dodge":
                            print("\nNow cut the Rope")
                            next = raw_input("Cut the rope *Type cut* ")
                            if next == "cut":
                                print("\n\tThe candle fell down and crashed with the Minotaurus")
                                print("Minotaurus: I'm going to die, HUMAN, go the the cave my brother is there he has the other key, HE WILL KILL YOU")
                                print("\n\t You did it! You defeated the Minotaurus")
                                print("\n\t Now you have the first key")
                                print("\nNow go the Dark room and keep fighting")
                                next = raw_input("Type back ")
                                if next == "back":
                                    print Beginning()

                                else:
                                    print Beginning()
                            else:
                                dead("You didn't cut the rope")
                        else:
                            dead("You didn't Dodge")
                    else:
                        dead("You didn't run")
                else:
                    dead("You didn't run")
            else:
                dead("You didn't Attack")

        elif next == "roll left":
            dead("Why? IDK you just died")

        elif next == "jump":
            dead("You can't jump that height")

    if next == "up":
        print Town_up()

    elif next == "left":
        print Town_left()

    elif next == "right":
        print Town_right()

    else:
        print("\nWhat?")
        print Town()


def Cementery():
    print ("\tThe Cementery is full of tumbstones you can only walk forward")
    print ("\n\nYou are in the Cementery")
    next = raw_input("Go *up* ")
    if next == "up":
        print ("\nYou kept walking forward")
        next = raw_input("You found a Ghost will fight him? ")
        if next == "no":
            print ("\nGood decision, you found a note")
            next = raw_input("read it? ")
            if next == "yes":
                print ("\n\tWrong was GO BACK")
                print ("\n\nYou kept walking forward until you found something spooky, a Big,  Big hole.")
                print ("\n\t There is Cthulhu")
                next = raw_input("Go? *Type Go* ")
                if next == "Go":
                    print ("\n\n\tYou threw into the battle")
                    print Cthulhu()

                else:
                    dead("You died")
            else:
                dead("\nYou lose into the Cementery")
        else:
            dead("\nHow the hell are you going to fight a Ghost??")
    else:
        dead("\nYou don't know were you are, and you died")

def Cthulhu():
     Cthulhu_Dead = False
     print ("Cthulhu: You will die")

     def Tower1():
         print ("\nNow you are in the Tower1")
         print ("There are three points to shoot")
         next = raw_input("P1, P2, P3 ")
         if next == "P3":
             print ("The hit was Super effectve, now go to  the next tower")

         else:
              dead("That wasn't the point")

     def Tower2():
         print ("\nNow you are in the Tower1")
         print ("There are three points to shoot")
         next = raw_input("P1, P2, P3 ")
         if next == "P1":
             print ("\nThe hit was Super effectve, now go to  the next tower")

         else:
             dead("That wasn't the point")

     def Tower3():
         print("\nrYou are in the Tower3")
         print("there are three points to shoot")
         next = raw_input("P1, P2, P3 ")
         if next == "P2":
             print ("You killed Cthulhu")
             print ("\n\nCthulhu died")
             print ("\nCthulhu: You are strong!, i think you are trying to rescute that man")
             print ("Well, go to the Dungeon, to find th last key")
             next = raw_input("(POSE LIKE A MOTHERF*CKING CHAMPION) then go the dark room *Type back* ")
             if next == "back":
                 print Beginning()

     next = raw_input("Cthulhu is trying to smash you whith his foot *run or jump* ")
     if next == "run":
         print ("\nYou dodged it, now Skeletons are appearing")
         next = raw_input("Keep running or fight? *run* ")
         if next == "run":
             print ("\nYou dodged all the Skeletons")
             print ("Cthulhu can't see you")
             next = raw_input("\nkill skeletons, climb Cthulhu? ")
             if next == "kill skeletons":
                 print ("\nYou killed all the skeletons, Cthulhu is trying to smash you again")
                 next = raw_input("*dodge*")
                 if next == "dodge":
                     print ("\n\t While dodging you found a ULTRA LASER BAZOOKA")
                     print ("\nYou need to find a good angle")
                     print ("More skeletons are appearing, you stated to run, Cthulhu tried to smash, but he fail")
                     print ("\nThere are three good places: Tower1, Tower2, Tower3")
                     while True:
                         next = raw_input("Tower1, Tower2 , Tower3 ")
                         if next == "Tower1":
                             print Tower1()

                         elif next == "Tower2":
                             print Tower2()

                         elif next == "Tower3":
                             print Tower3()
                             Cthulhu_Dead = True
                         else:
                            dead("\n Cthulhu killed you")
                 else:
                    dead("\nYou didn't dodge")
             else:
                 dead("\nHow the hell are you goint to climb a FUCKING MYTICAL BEAST")
         else:
             dead("\nYou didn't run")
     else:
         dead("\nFuck your logic")


def Dungeon():
    print("\n\tNow you are in the dungeon")
    print ("\nThere are three ways to go, One door left, another door right, and a rope infront")
    next = raw_input("left, right, forward ")
    if next == "forward":
        print("\nYou used the rope to go down")
        print("There are a lot of spiders")
        next = raw_input("fight, run ")
        if next == "run":
            print ("\nOk, you relly know when to avoid a fight")
            print ("There is a giant guard")
            next = raw_input("talk, kill ")
            if next == "talk":
                print ("\nGuard: Oh... You aren't a monster And tell me brave warrior, what are you doing in this Dungeon?")
                next = raw_input("> ")
                print ("\nI know you are here to kill the Giant Spider, I'll help you.")
                print ("You kept walking until you found 5 ways")
                print ("\nGuard: Let's take the thrid one")
                next = int(raw_input("1, 2, 3, 4, 5 "))
                if next == 3:
                    print ("\nThere are a lot of spiders (Like 200)")
                    print ("You'll have to fight")
                    print ("Guard: Man, how many will you kill? ")
                    next = int(raw_input("> "))
                    if next < 100:
                        print ("Guard: Ok, don't worry, ill kill the others")
                        print ("\n\n\nYou killed all the spiders succesfully")
                        print ("\n\tThe Giant is poinsoned")
                        print ("\nThere are 4 ways")
                        print ("Guard: Take the fourth one")
                        next = int(raw_input("1, 2, 3, 4 "))
                        if next == 4:
                            print("\n\t*There is a Giant door*")
                            print ("\nGuard: The poison is killing me, but don't worry, we're goint to kill that spider, and you'll rescute your friend")
                            next = raw_input("Open the door *open* ")
                            if next == "open":
                                print ("\n\tThe Giant spider is there")
                                print ("\nWHAT'S THE PLAN LITTLE MAN?")
                                next = raw_input("> ")
                                print ("Guard: it does't looks like a good plan, ok, here's mine, i'll throw you the spider and you smash one of her eyes")
                                print ("\n\tThe guard threw you to the spider")
                                Eyes = 1
                                while Eyes < 8:
                                    next = int(raw_input("8 Eyes, select one "))
                                    print ("\nYou smashed that eyes")
                                    print ("The Guard is fighting bravely with the spider")
                                    next = raw_input("jump or keep smashing? ")
                                    if next == "jump":
                                        print ("\nThe giant threw you again to the spider, Select an eye")
                                    elif next == "keep smashing":
                                        print ("\nYou smashed 3 eyes more.")
                                        print ("The Guard smashed the others 4")
                                        print ("\n\tTHE GIANT SPIDER IS DOOOWN")
                                        Eyes = 8
                                        print ("\n\tThe Guard is Dying, You have to find the antidotes")
                                        antidotes = 0
                                        while antidotes < 10:
                                            next = int(raw_input("There are 20 rooms "))
                                            if next == 1:
                                                print ("This room is empty")
                                            elif next == 2:
                                                print ("You found one!")
                                                antidotes += 1
                                            elif next == 3:
                                                print ("You fount one!")
                                                antidotes += 1
                                            elif next == 4:
                                                print ("This room is empty")
                                            elif next == 5:
                                                print ("This room is empty")
                                            elif next == 6:
                                                print ("This room is empty")
                                            elif next == 7:
                                                print ("You found one!")
                                                antidotes += 1
                                            elif next == 8:
                                                print ("This room is empty")
                                            elif next == 9:
                                                print ("You found one!")
                                                antidotes += 1
                                            elif next == 10:
                                                print ("This room is empty")
                                            elif next == 11:
                                                print ("You found one")
                                                antidotes += 1
                                            elif next == 12:
                                                print("You found one")
                                                antidotes += 1
                                            elif next == 13:
                                                print ("This room is empty")
                                            elif next == 14:
                                                print("This room is empty")
                                            elif next == 15:
                                                print ("You found one!")
                                                antidotes += 1
                                            elif next == 16:
                                                print ("This room is empty")
                                            elif next == 17:
                                                print ("You found one!")
                                                antidotes += 1
                                            elif next == 18:
                                                print ("This room is empty")
                                            elif next == 19:
                                                print ("You found one!")
                                                antidotes += 1
                                            elif next == 20:
                                                print ("You found one!")
                                                antidotes += 1
                                            else:
                                                print ("That's not even a number.")

                                        if antidotes == 10:
                                            print ("\n\tYou saved the Guard")
                                            print ("\nGuard: Thanks, You saved my life, here's the key, Go to defeat the titan and rescute your friend")
                                            next = raw_input("Go to the dark room *type back* ")
                                            if next == "back":
                                                print final()
                                            else:
                                                print final()
                                        else:
                                            dead("Not enought antidotes")
            else:
                if next == "kill":
                    print ("\nYou kept walking until you found 5 ways")
                    next = int(raw_input("1, 2, 3, 4, 5 "))
                    if next == 3:
                        print ("\nThere are a lot of spiders (Like 200)")
                        print ("You'll have to fight")
                        dead("\nToo much spiders")
                    else:
                        dead("Wrong way")


        else:
            dead("\nYou died by the poinson")

    else:
        dead("\nThis is a Dungeon: is full of traps")







def dead(why):
    print why, "Good Job!"
    exit(0)


print prologue()
