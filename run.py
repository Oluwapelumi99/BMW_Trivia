# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from rich import print
import gspread
# import os
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('secrets.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Bmw_trivia')

print('[bold blue]WELCOME TO MY BMW TRIVIA!!! :dance:') 

# import ascii_magic
# output = ascii_magic.from_images_file('IMG_9484.JPG',columns=200,char='#') 
# ascii_magic.to_terminal(output) 
score = 0
start_trivia = True
while start_trivia:
    try:
        continue_trivia = str(input("[bold blue]Do you want to start quiz? yes/no\n  "))
        if continue_trivia.lower() == 'yes':
            print('[bold blue] Brace yourself for a challenge :thumbsup:! \n Read instructions carefully. \n There are 20 questions in this Quiz, pick your answer by inputing an option between A-D.\n Goodluck!')
            break  
        elif continue_trivia.lower() == 'no':
            print('[bold blue] Sad to see you go this time')
            start_trivia == False                     
    except Exception:
        print('[bold white] Wrong input. Please try again..')       
def get_user_answer_0(user_answer):
    if answer.lower() == 'a':
        print(f"[bold blue]Welldone! {user_answer} is the correct answer :smile:")
        global score
        score += 1
    else:
        print('[italic bold blue]Sorry...option a is the correct answer :frown:')    
 
answer= input('[bold blue]1. What does BMW stand for? \n A. Bayerische Motoren Werke \n B. Brunswick Motoren Werke \n C. Borgholzzhausen Motoren Werke\n D. Berlin Motorenn Werke\n Pick your answer: \n ')
get_user_answer_0(answer)

def get_user_answer_0(user_answer):
    if answer.lower() == 'd':
        print(f"[bold blue]Welldone! {user_answer} is the correct answer :smile:")
        global score
        score += 1
    else:
        print('[italic bold blue]"Sorry...option d is the correct answer"')    
 
answer= input('[bold blue]2. What color is the BMW logo \n A. Blue & gold \n B. Red & gold \n C. Red & White \n D. Blue & white \n Pick your answer: \n ')
get_user_answer_0(answer)

def get_user_answer_2(user_answer):
    if answer.lower() == 'b':
        print(f"[bold blue]Welldone! {user_answer} is the correct answer :smile:")
        global score
        score += 1
    else:
        print('[bold blue]"Sorry...option b is the correct answer"')
answer = input('[bold blue]3. What is the slogan of BMW? \n A. The Ultimate Driving Power \n B. Sheer Driving Pleasure\n C. Enjoy the Ride \n D. Joy of discovery \n Pick your answer: \n ')
get_user_answer_2(answer)    
   
def get_user_answer_3(user_answer):
    if answer.lower() == 'c':
        print(f"[bold blue]Welldone! {user_answer} is the correct answer :smile:")
        global score
        score += 1
    else:
        print('[bold blue]"Sorry...option c is the correct answer"')
answer = input('[bold white]4. What is the BMW M series? \n A. A line of electric cars \n B. An SUV for off-roading \n C. A line of performance cars \n D. A line of luxury sedan \n Pick your answer: \n ')
get_user_answer_3(answer)  


def get_user_answer_4(user_answer):
    if answer.lower() == 'd':
        print(f"[bold blue]Welldone! {user_answer} is the correct answer :smile:")
        global score
        score += 1
    else:
        print('[blue]"Sorry...option c is the correct answer"')
answer = input('[bold blue]5. What was the name of BMW\'s first car? \n A. 3 Series \n B. 5 Series \n C. 7 Series\n D. Dixi \n Pick your answer: \n ')
get_user_answer_4(answer)  

def get_user_answer_5(user_answer):
    if answer.lower() == 'c':
        print(f"[bold blue]Welldone! {user_answer} is the correct answer :smile:")
        global score
        score += 1
    else:
        print('[blue]"Sorry...option c is the correct answer"')
answer = input('[bold blue]6. What year was the BMW 3 Series first intoduced? \n A. 1969 \n B. 1961 \n C. 1975\n D. 1984 \n Pick your answer: \n')
get_user_answer_5(answer)  

def get_user_answer_6(user_answer):
    if answer.lower() == 'c':
        print(f"[bold blue]Welldone! {user_answer} is the correct answer :smile:")
        global score
        score += 1
    else:
        print('[blue]"Sorry...option c is the correct answer"')
answer = input('[bold blue]7. How far could BMW\'s first all-electric car drive before running out of battery? \n A. 79 miles\n B. 59 miles \n C. 19 miles\n D. 39 miles\n Pick your answer: \n')
get_user_answer_6(answer) 

def get_user_answer_7(user_answer):
    if answer.lower() == 'b':
        print(f"[bold blue]Welldone! {user_answer} is the correct answer :smile:")
        global score
        score += 1
    else:
        print('[blue]"Sorry...option b is the correct answer"')
answer = input('[bold white]8. What is BMW\'s Formula One racing team called? \n A. BMW Motorsport \n B. BMW Sauber F1 Team \n C. BMW M Racing\n D. BMW Racing Team \n Pick your answer: \n')
get_user_answer_7(answer)

def get_user_answer_8(user_answer):
    if answer.lower() == 'd':
        print(f"[bold blue]Welldone! {user_answer} is the correct answer :smile:")
        global score
        score += 1
    else:
        print('[blue]"Sorry...option d is the correct answer"')
answer = input('[bold blue]9. What is BMW\'s headquartwes shaped like? \n A. A Radiator \n B. A catalytic converter \n C. A Piston\n D. A Four-Cylinder Engine \n Pick your answer: \n')
get_user_answer_8(answer)

def get_user_answer_9(user_answer):
    if answer.lower() == 'a':
        print(f"[bold blue]Welldone! {user_answer} is the correct answer :smile:")
        global score
        score += 1
    else:
        print('[blue]"Sorry...option a is the correct answer"')
answer = input('[bold blue]10. What was BMW\'s first product? \n A. Aircraft Engine \n B. Spark plug \n C. A Tractor\n D. Motorcycle \n Pick your answer: \n')
get_user_answer_9(answer)

def get_user_answer_10(user_answer):
    if answer.lower() == 'b':
        print(f"[bold blue]Welldone! {user_answer} is the correct answer :smile:")
        global score
        score += 1
    else:
        print('[blue]"Sorry...option b is the correct answer"')
answer = input('[bold blue]11. What grille design has become a defining feature of BMW\'s automobiles? \n A. Heart grille \n B. Kidney grille \n C. Pharynx grille\n D. Liver grille \n Pick your answer: \n')
get_user_answer_10(answer)

def get_user_answer_11(user_answer):
    if answer.lower() == 'd':
        print(f"[bold blue]Welldone! {user_answer} is the correct answer :smile:")
        global score
        score += 1
    else:
        print('[blue]"Sorry...option d is the correct answer"')
answer = input('[bold blue]12. What race did the BMW 328 win in 1936? \n A. Alpine Rally \n B. Österreichise Alpenfahrt \n C. Mille Miglia\n D. Eifelrennen \n Pick your answer: \n')
get_user_answer_11(answer)

def get_user_answer_12(user_answer):
    if answer.lower() == 'd':
        print(f"[bold blue]Welldone! {user_answer} is the correct answer :smile:")
        global score
        score += 1
    else:
        print('[blue]"Sorry...option d is the correct answer"')
answer = input('[bold blue]13. Which BMW features vertically sliding doors? \n A. M1 \n B. E12 \n C. I8\n D. Z1 \n Pick your answer: \n')
get_user_answer_12(answer)

def get_user_answer_13(user_answer):
    if answer.lower() == 'a':
        print(f"[bold blue]Welldone! {user_answer} is the correct answer :smile:")
        global score
        score += 1
    else:
        print('[blue]"Sorry...option a is the correct answer"')
answer = input('[bold blue]14. What is the largest BMW ever built? \n A. X7\n B. M12 \n C. Z4\n D. E90 \n Pick your answer: \n')
get_user_answer_13(answer)

def get_user_answer_14(user_answer):
    if answer.lower() == 'd':
        print(f"[bold blue]Welldone! {user_answer} is the correct answer :smile:")
        global score
        score += 1
    else:
        print('[blue]"Sorry...option d is the correct answer"')
answer = input('[bold blue]15. Which BMW was known as a "bubble car"? \n A. HEINKEL KABINE\n B. ATTICA \n C. PULI\n D. ISETTA \n Pick your answer: \n')
get_user_answer_14(answer)

def get_user_answer_15(user_answer):
    if answer.lower() == 'd':
        print(f"[bold blue]Welldone! {user_answer} is the correct answer :smile:")
        global score
        score += 1
    else:
        print('[blue]"Sorry...option d is the correct answer"')
answer = input('[bold blue]16. What year was BMW founded? \n A. 1926 \n B. 1896 \n C. 1906\n D. 1916 \n Pick your answer: \n')
get_user_answer_15(answer)

def get_user_answer_16(user_answer):
    if answer.lower() == 'c':
        print(f"[bold blue]Welldone! {user_answer} is the correct answer :smile:")
        global score
        score += 1
    else:
        print('[blue]"Sorry...option c is the correct answer"')
answer = input('[bold blue]17. What was BMW\'s first motorcycle? \n A. K100 \n B. K1 \n C. R32\n D. R12 \n Pick your answer: \n')
get_user_answer_16(answer)

def get_user_answer_17(user_answer):
    if answer.lower() == 'a':
        print(f"[bold blue]Welldone! {user_answer} is the correct answer :smile:")
        global score
        score += 1
    else:
        print('[blue]"Sorry...option a is the correct answer"')
answer = input('[bold blue]18. The 303 was the first BMW with a ______. \n A. V6 Engine\n B. V8 Engine\n C. V4 Engine\n D. V12 Engine \n Pick your answer: \n')
get_user_answer_17(answer)

def get_user_answer_18(user_answer):
    if answer.lower() == 'c':
        print(f"[bold blue]Welldone! {user_answer} is the correct answer :smile:")
        global score
        score += 1
    else:
        print('[blue]"Sorry...option c is the correct answer"')
answer = input('[bold blue]19. What was the company\'s first post WW11 vehicle? \n A. BMW Z1 \n B. BMW 326 \n C. BMW 501\n D. BMW 700 \n Pick your answer: \n')
get_user_answer_18(answer)

def get_user_answer_19(user_answer):
    if answer.lower() == 'b':
        print(f"[bold blue]Welldone! {user_answer} is the correct answer :smile:")
        global score
        score += 1
    else:
        print('[blue]"Sorry...option b is the correct answer"')
answer = input('[bold blue]20. Which BMW was almost a Lamborghini? \n A. E12\n B. M1\n C. Z1\n D. I8 \n Pick your answer: \n')
get_user_answer_19(answer)


def get_result(user_score):
    print(f'[bold blue]You got {user_score} out of 20 questions right! ')
    print(f'[bold blue]You got {user_score /20 *100}%')
get_result(score)   













