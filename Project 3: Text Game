########
#######################
#Game Title: "Do your chores!"
#Setting: Your home, two floors
#Game Summary: 
#   You are doing homework then your mom texts you to do your chores. 
#   You go downstairs to the kitchen and do the dishes then you win.
#   If you get distracted through either a nap or goldifsh, you lose.
#   You must complete all of this before mom gets home.
#Global Variables: 
#   minutes (starts at 0 and increases by at least 2 every move. game ends at 20)
########################
#import modules
#######
import time
import os
########
#define functions
#######
def check_time():
    os.system('clear')
    global minutes
    minutes = minutes + 2
    if minutes >= 20:
        grounded()
    else:
        print("MOM WILL BE HOME IN", 20 - minutes, "MINUTES!!!")

def grounded():
    global minutes, washDishes
    print("You hear the garage door open and realize your fate. Mom's home.")
    print("GROUNDED")
    again = input("\nWould you like to restart? Say yes or no\n")
    if again.lower() == "yes":
        minutes = 0
        start()
    else:
        print("Thank you for playing!")

def start():
    os.system('clear')
    print("While you're doing your homework, Mom texts you,\n\t'I'll be home in 20 minutes...' \n'MAKE SURE ALL YOUR CHORES ARE FINISHED OR YOU'RE GROUNDED'")
    bedroom()

def bedroom():
    print("The main chore you have is to wash the dishes.")
    print("\nYou are currently in your bedroom")
    move = input("You should probably leave your room in order to not waste time. \nType 'hallway' to leave: ")
    if move.lower() == "hallway":
        hallway()
    else:
        #TODO: what should happen if they type something else?
        print("I don't quite understand. I'm assuming you want go to the hallway.")
        time.sleep(2)
        hallway()
        
def hallway():
    check_time()
    print("\nYou are in the hallway.")
    move = input("\nWhere would you like to go? Say one of these choices:\n\tmy room\n\tmom's room\n\tdownstairs\n")
    if move.lower() == "my room":
        bedroom()
    elif move.lower() == "mom's room":
        mom_room()
    elif move.lower() == "downstairs":
        living_room()
    else:
        #TODO: what should happen if they type something else?
        print("I don't quite understand. I'm assuming you want to stay put.")
        hallway()

def mom_room():
    check_time()
    print("\nApparently, you're in your mom's room.")
    print("Although it's probably smarter to do your chores, you feel drawn to your mom's California King with Cooling Gel Ventilated Memory Foam bed.")
    move = input("\nWhat would you like to do next? Type one of these choices:\n\tsleep\n\tleave\n")
    if move.lower() == "sleep":
        nap()
    elif move.lower() == "leave":
        hallway()
    else:
        #TODO: what should happen if they type something else?
        print("I don't quite understand. I'm assuming you want to stay put.")
        mom_room()

def nap():
    global time, minutes
    print("You crawl into the bed and pulled the blanket over your head.")
    time.sleep(1)
    print("Zzz")
    time.sleep(1)
    print("Zzz")
    time.sleep(1) 
    minutes = minutes + 30 
    check_time()


def living_room():
    check_time()
    print("You go to the living room.")
    move = input("Where would you like to go? Type one of these choices:\n\tupstairs\n\tkitchen\n")
    if move.lower() == "kitchen":
        kitchen()
    elif move.lower() == "upstairs":
        hallway()
    else:
        #TODO: what should happen if they type something else?
        print("I don't quite understand. I'm assuming you want to stay put.")
        living_room()

def kitchen():
    check_time()
    print("You go into the kitchen and see the sink full of dishes.")
    print("As you wonder how 3 people can use all these dishes, you see the Goldfish box and feel your stomach rumble.")
    move = input("\nWhat would you like to do next? Type one of these choices:\n\tgoldfish\n\tdishes\n\tleave\n")
    if move.lower() == "goldfish": 
        goldfish()
    elif move.lower() == "dishes":
        dishes() 
    elif move.lower() == "leave":
        living_room()
    else:
        print("I don't quite understand. I'll just assume you want to stay put")
        kitchen()

def goldfish():
    global minutes, time
    print("You grab the bag of Goldfish and go absolutely feral. ")   
    time.sleep(2)
    print("OM NOM NOM")
    time.sleep(2)
    print("CRUNCH CRUNCH CRUNCH") 
    time.sleep(2)
    print("As you go insane over the snack that smiles back, you lose track of time.")
    time.sleep(4)
    minutes = minutes + 10
    check_time()


def dishes():
    global time, minutes
    print("You put on gloves and get to work.")
    print('''
        °ﾟ❍º❍ 
        ❍°ﾟº❍ 
        °°''') 
    time.sleep(2) 
    print('''
        °ﾟ❍º❍ 
        ❍°ﾟº❍ 
        °°''') 
    print("You finished washing all the dishes")
    time.sleep(1)
    print("Since you finished washing dishes, you decide to sit on the couch.")
    time.sleep(1)
    print('''    .--..--..--..--..--..--.
    .' \  (`._   (_)     _   \
  .'    |  '._)         (_)  |
  \ _.')\      .----..---.   /
  |(_.'  |    /    .-\-.  \  |
  \     0|    |   ( O| O) | o|
   |  _  |  .--.____.'._.-.  |
   \ (_) | o         -` .-`  |
    |    \   |`-._ _ _ _ _\ /
    \    |   |  `. |_||_|   |
    | o  |    \_      \     |     -.   .-.
    |.-.  \     `--..-'   O |     `.`-' .'
  _.'  .' |     `-.-'      /-.__   ' .-'
.' `-.` '.|='=.='=.='=.='=|._/_ `-'.'
`-._  `.  |________/\_____|    `-.'
   .'   ).| '=' '='\/ '=' |
   `._.`  '---------------'
           //___\   //___\
             ||       ||
             ||_.-.   ||_.-.
            (_.--__) (_.--__)''')
    print("After watching Spongebob for the rest of the time, your mom comes home and sees the clean sink.")
    print("She tells you she's proud of you!")
    print("You won! CONGRATULATIONS\t")
    time.sleep(5)
    again = input("\nWould you like to restart? Type yes or no\n")
    if again.lower() == "yes":
        minutes = 0
        start()
    else:
        print("Thank you for playing!")
    
########
#main
#######
minutes = 0
start() 
