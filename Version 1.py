#Version 1: Starting Quiz

#List initialization
list = []

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
print("This is a Trivia Quiz about the 2024 film 𝑩𝒂𝒏𝑮 𝑫𝒓𝒆𝒂𝒎! 𝑰𝒕'𝒔 𝑴𝒚𝑮𝑶!!!!!—𝑺𝒑𝒓𝒊𝒏𝒈 𝑺𝒖𝒏𝒔𝒉𝒊𝒏𝒆, 𝑳𝒐𝒔𝒕 𝑪𝒂𝒕 and 𝑩𝒂𝒏𝑮 𝑫𝒓𝒆𝒂𝒎! 𝑰𝒕'𝒔 𝑴𝒚𝑮𝑶!!!!!—𝑺𝒊𝒏𝒈𝒊𝒏𝒈 …𝑳𝒆𝒕 𝒖𝒔 𝒃𝒆 𝒐𝒖𝒓 𝒑𝒐𝒆𝒎 & 𝑭𝑰𝑳𝑴 𝑳𝑰𝑽𝑬.")

player_data = input("What is your name? "),


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
       print(f"Welcome {player_data}!") 
       print("""Get ready for a quiz! You can learn more here: https://zh.wikipedia.org/wiki/BanG_Dream!_It%27s_MyGO!!!!!#
(The English version of Wikipedia does not yet include content related to the movie version; please use another language to view it.)

https://bandori.miraheze.org/wiki/BanG_Dream!_It%27s_MyGO!!!!!_(Movie)

https://bandori.fandom.com/wiki/BanG_Dream!_It%27s_MyGO!!!!!_(Movie)""")
    else:
       print("""See you later, I highly recommend you watch these movies.
       https://zh.wikipedia.org/wiki/BanG_Dream!_It%27s_MyGO!!!!!#
(The English version of Wikipedia does not yet include content related to the movie version; please use another language to view it.)

https://bandori.miraheze.org/wiki/BanG_Dream!_It%27s_MyGO!!!!!_(Movie)

https://bandori.fandom.com/wiki/BanG_Dream!_It%27s_MyGO!!!!!_(Movie)""")
       exit()

#Questions
questions = {

    "1.Who hasn't attended Tsuki no Mori Girls' School?": ["A, Takamatsu Tomori", "B, Nagasaki Soyo", "C, Togawa Sakiko", "D, Wakaba Mutsumi"],


    "2.What are Nagasaki Soyo's plans after CRYCHIC disbanded?": ["A. Form a new band", "B. Reviving CRYCHIC", "C. Take a year off from school", "D. Transferring schools"],

    "3.What is this movie adapted from?": ["A. Animated series:𝑩𝒂𝒏𝑮 𝑫𝒓𝒆𝒂𝒎! 𝑰𝒕'𝒔 𝑴𝒚𝑮𝑶!!!!!", "B. Novel:𝑩𝒂𝒏𝑮 𝑫𝒓𝒆𝒂𝒎! 𝑺𝒕𝒂𝒓 𝑩𝒆𝒂𝒕", "C. Comic:𝑩𝒂𝒏𝑮 𝑫𝒓𝒆𝒂𝒎! 𝑰𝒕'𝒔 𝑴𝒚𝑮𝑶!!!!! 𝑷𝒓𝒂𝒚𝒊𝒏𝒈 𝒇𝒐𝒓 𝑺𝒖𝒏𝒔𝒉𝒊𝒏𝒆 𝒊𝒏 𝒕𝒉𝒆 𝑹𝒂𝒊𝒏", "D. The true story of the punk rock band MyGO!!!!!" ],

    "4.In Tomori's recollection, which band's song did Wakaba Mutsumi sing in karaoke?": ["A. Roselia", "B. Morfonica", "C. Pastel Palettes", "D. Ave Mujica"]
}

answers = {

"1.Who hasn't attended Tsuki no Mori Girls' School?": "A",


"2.What are Nagasaki Soyo's plans after CRYCHIC disbanded?": "B",

"3.What is this movie adapted from?": "A",

"4.In Tomori's recollection, which band's song did Wakaba Mutsumi sing in karaoke?": "C"
}

score = 0

for question, options in questions.items():


    print(question)


    for option in options:


        print(option)


    answer = input("Type there").upper()

    list.append( answer );

    if answer == answers[question]:


        print("correct！")


        score += 1


    else:


        print(f"wrong！Correct: {answers[question]}")


print(f"YOUR SCORE IS：{score}/{len(questions)}")

#Store and display test results
a = input("Do you want to see your answer and the correct answer?").lower()
if a == "yes":
    print ("1.Who hasn't attended Tsuki no Mori Girls' School?, 2.What are Nagasaki Soyo's plans after CRYCHIC disbanded?, 3.What is this movie adapted from?")
    print("Your answer:")
    print (list)
    print("The correct answer:A,B,A,C")
else:
    exit()

