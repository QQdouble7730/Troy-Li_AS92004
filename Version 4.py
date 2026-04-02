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

#Name check
player_data = input("What is your name? "),

#Age check
while True:
    try:
        age = int(input("how old are you ... please enter your age !: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid half-width integer.")

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

    "1. Who hasn't attended Tsukinomori Girls' Academy?": ["A, Takamatsu Tomori", "B, Nagasaki Soyo", "C, Togawa Sakiko", "D, Wakaba Mutsumi"],

    "2. What are Nagasaki Soyo's plans after CRYCHIC disbanded?": ["A. Form a new band", "B. Reviving CRYCHIC", "C. Take a year off from school", "D. Transferring schools"],

    "3. What is this movie adapted from?": ["A. Animated series:𝑩𝒂𝒏𝑮 𝑫𝒓𝒆𝒂𝒎! 𝑰𝒕'𝒔 𝑴𝒚𝑮𝑶!!!!!", "B. Novel:𝑩𝒂𝒏𝑮 𝑫𝒓𝒆𝒂𝒎! 𝑺𝒕𝒂𝒓 𝑩𝒆𝒂𝒕", "C. Comic:𝑩𝒂𝒏𝑮 𝑫𝒓𝒆𝒂𝒎! 𝑰𝒕'𝒔 𝑴𝒚𝑮𝑶!!!!! 𝑷𝒓𝒂𝒚𝒊𝒏𝒈 𝒇𝒐𝒓 𝑺𝒖𝒏𝒔𝒉𝒊𝒏𝒆 𝒊𝒏 𝒕𝒉𝒆 𝑹𝒂𝒊𝒏", "D. The true story of the punk rock band MyGO!!!!!" ],

    "4. In Tomori's recollection, which band's song did Wakaba Mutsumi sing in karaoke?": ["A. Roselia", "B. Morfonica", "C. Pastel Palettes", "D. Ave Mujica"],

    "5. MyGO attended a concert hosted by whom?": ["A. Popipa and Afterglow", "B. Popipa and Roselia", "C. Afterglow and PasPal", "D. Afterglow and Morfonica"],

    "6. Who didn’t Takamatsu Tomori give band-aids to?": ["A．Chihaya Anon", "B. Togawa Sakiko", "C. Shiina Taki", "D. Nagasaki Soyo"],

    "7. Which of the following characters correctly corresponds to their respective clubs?": ["A. Takamatsu Tomori, Light Music Club", "B. Chihaya Anon, Astronomy Club", "C. Nagasaki Soyo, Wind Music Club", "D. Togawa Sakiko, Wind Music Club"],

    "8. 𝑩𝒂𝒏𝑮 𝑫𝒓𝒆𝒂𝒎! 𝑰𝒕'𝒔 𝑴𝒚𝑮𝑶!!!!!—𝑺𝒊𝒏𝒈𝒊𝒏𝒈 …𝑳𝒆𝒕 𝒖𝒔 𝒃𝒆 𝒐𝒖𝒓 𝒑𝒐𝒆𝒎 & 𝑭𝑰𝑳𝑴 𝑳𝑰𝑽𝑬's ending theme song is": ["A. Speed", "B. Shiori", "C. Hitoshizuku", "D. Mayoiuta"],

    "9. Which of the following statements is correct in these two movies?": ["A. Chihaya Anon has never met Togawa Sakiko.", "B. Shiina Taki has never met Misumi Uika.", "C. Takamatsu Tomori has never met Yahata Umiri.", "D. Kaname Rāna has never met Wakaba Mutsumi."],

    "10. Which of the following statements is correct?": ["A. The band name 𝑴𝒚𝑮𝑶 has four exclamation marks after it.", "B. The youngest member of the band 𝑴𝒚𝑮𝑶 is Kaname Rakuna.", "C. The band 𝑴𝒚𝑮𝑶 has never played Kaname Rāna.", "D. The band 𝑴𝒚𝑮𝑶 has a keyboard instrument."],

    "11. Which band's poster is in the astronomy classroom at Haneoka Girls' Academy?": ["A. Morfonica", "B. RAISE A SUILEN", "C. Roselia", "D. MyGO!!!!!"],

    "12. Which song was Takamatsu Tomori's first attempt at writing lyrics?": ["A. 𝑨 𝒔𝒐𝒏𝒈 𝒂𝒃𝒐𝒖𝒕 𝒘𝒂𝒏𝒕𝒊𝒏𝒈 𝒕𝒐 𝒃𝒆𝒄𝒐𝒎𝒆 𝒉𝒖𝒎𝒂𝒏", "B. 𝑯𝒂𝒓𝒖𝒉𝒊𝒌𝒂𝒈𝒆 (𝑺𝒑𝒓𝒊𝒏𝒈 𝑺𝒖𝒏𝒍𝒊𝒈𝒉𝒕)", "C. 𝑼𝒕𝒂𝒌𝒐𝒕𝒐𝒃𝒂", "D. 𝑺𝒐𝒏𝒈 𝒐𝒇 𝑷𝒓𝒐𝒗𝒊𝒏𝒈 𝑫𝒆𝒔𝒕𝒊𝒏𝒚"]
}

#Answers
answers = {

"1. Who hasn't attended Tsukinomori Girls' Academy?": "A",

"2. What are Nagasaki Soyo's plans after CRYCHIC disbanded?": "B",

"3. What is this movie adapted from?": "A",

"4. In Tomori's recollection, which band's song did Wakaba Mutsumi sing in karaoke?": "C",

"5. MyGO attended a concert hosted by whom?": "A",

"6. Who didn’t Takamatsu Tomori give band-aids to?": "D",

"7. Which of the following characters correctly corresponds to their respective clubs?": "C",

"8. 𝑩𝒂𝒏𝑮 𝑫𝒓𝒆𝒂𝒎! 𝑰𝒕'𝒔 𝑴𝒚𝑮𝑶!!!!!—𝑺𝒊𝒏𝒈𝒊𝒏𝒈 …𝑳𝒆𝒕 𝒖𝒔 𝒃𝒆 𝒐𝒖𝒓 𝒑𝒐𝒆𝒎 & 𝑭𝑰𝑳𝑴 𝑳𝑰𝑽𝑬's ending theme song is": "A",

"9. Which of the following statements is correct in these two movies?": "D",

"10. Which of the following statements is correct?": "B",

"11. Which band's poster is in the astronomy classroom at Haneoka Girls' Academy?": "C",

"12. Which song was Takamatsu Tomori's first attempt at writing lyrics?": "B"
}

#Quiz and Scoring

score = 0

for question, options in questions.items():


    print(question)


    for option in options:


        print(option)


    answer = input("Type there").upper()

    list.append( answer );

    if answer == answers[question]:


        print("Correct！")


        score += 1


    else:


        print(f"Wrong！Correct: {answers[question]}")


print(f"{player_data}'s score is：{score}/{len(questions)}")

#Store and display test results
a = input("Do you want to see your answer and the correct answer?").lower()
if a == "yes":
    print("Your answer:")
    print (list)
    print("The correct answer:A, B, A, C, A, D, C, A, D, B, C, B")
    exit()
else:
    exit()

