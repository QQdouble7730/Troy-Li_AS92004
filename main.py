#Version 1: Starting Quiz

#Variable and Constants
ADULTAGE = 18 #This is my constant - this sets my age for 'adult'
CHILD = 11 #This is my constant - this sets my age for 'child'

#Welcome text
print("""
      ███  ███   ██   ██  ███      ████    █ █ █ █ █
    ██   ██   ██  ██ ██  █   ██  ██    ██  █ █ █ █ █
    ██   ██   ██   ███   █       ██    ██  █ █ █ █ █
    ██   ██   ██    █    █  ███  ██    ██               
    ██   ██   ██   █      ██ █     ████    █ █ █ █ █
                      Trivia Quiz
""")
print("This is a Trivia Quiz about the 2024 film *BanG Dream! It's MyGO!!!!!—Spring Sunshine, Lost Cat* and *BanG Dream! It's MyGO!!!!!—Singing …Let Us Be Our Poem & FILM LIVE*.")
name = input("What is your name ... please enter your name !: ")
age = int(input("how old are you ... please enter your age !: "))

#Age check
if age > ADULTAGE:
   print("You are way too old for this quiz")
   exit()
if age < CHILD:
   print("You are way too young for this quiz")
   exit()
else:
     #Checking if the user is ready?
    ready = input("Are you ready to play?").lower()
    if ready == "yes":\
    #Giving instructions
       print("Perfect lets begin ... \nThis game is easy ... you just answer the questions with the options given \n Make sure you are spelling it correctly!")
    else:
       print("See you later then ... ")
       exit()
