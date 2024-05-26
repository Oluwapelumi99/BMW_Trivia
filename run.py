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
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Bmw_trivia')
def get_username(name):
    return input(name)
def print_name(value_name):
    print(value_name)
name = get_username('Enter your name:')
print_name(f'[bold blue]Hello {name}. WELCOME TO MY BMW TRIVIA!!! :smile:')
  
# import ascii_magic
# output = ascii_magic.from_images_file('IMG_9484.JPG',columns=200,char='#') 
# ascii_magic.to_terminal(output) 
score = 0
start_trivia = True
while start_trivia:
    try:
        continue_trivia = str(input("Do you want to start quiz? yes/no\n  "))
        if continue_trivia.lower() == 'yes':
            print('[bold blue] Brace yourself for a challenge :thumbsup:! \n Read instructions carefully. \n There are 20 questions in this Quiz, pick your answer by inputing an option between A-D.\n Goodluck!')
            break  
        elif continue_trivia.lower() == 'no':
            print('[bold blue] Sad to see you go this time')
            start_trivia == False                     
    except Exception:
        print('[bold white] Wrong input. Please try again..')       
question_1 = "1. What does BMW stand for? \n A. Bayerische Motoren Werke \n B. Brunswick Motoren Werke \n C. Borgholzzhausen Motoren Werke\n D. Berlin Motorenn Werke"
question_2 = "2. What color is the BMW logo? \n A. Blue & gold \n B. Red & gold \n C. Red & White \n D. Blue & white"
question_3 = "3. What is the slogan of BMW? \n A. The Ultimate Driving Power \n B. Sheer Driving Pleasure\n C. Enjoy the Ride \n D. Joy of discovery"
question_4 = "4. What is the BMW M series? \n A. A line of electric cars \n B. An SUV for off-roading \n C. A line of performance cars \n D. A line of luxury sedan"
question_5 = "5. What was the name of BMW\'s first car? \n A. 3 Series \n B. 5 Series \n C. 7 Series\n D. Dixi"
question_6 = "6. What year was the BMW 3 Series first intoduced? \n A. 1969 \n B. 1961 \n C. 1975\n D. 1984"
question_7 = "7. How far could BMW\'s first all-electric car drive before running out of battery? \n A. 79 miles\n B. 59 miles \n C. 19 miles\n D. 39 miles"
question_8 = "8. What is BMW\'s Formula One racing team called? \n A. BMW Motorsport \n B. BMW Sauber F1 Team \n C. BMW M Racing\n D. BMW Racing Team"
question_9 = "9. What is BMW\'s headquartwes shaped like? \n A. A Radiator \n B. A catalytic converter \n C. A Piston\n D. A Four-Cylinder Engine"
question_10 = "10. What was BMW\'s first product? \n A. Aircraft Engine \n B. Spark plug \n C. A Tractor\n D. Motorcycle"
question_11 = "11. What grille design has become a defining feature of BMW\'s automobiles? \n A. Heart grille \n B. Kidney grille \n C. Pharynx grille\n D. Liver grille"
question_12 = "12. What race did the BMW 328 win in 1936? \n A. Alpine Rally \n B. Österreichise Alpenfahrt \n C. Mille Miglia\n D. Eifelrennen"
question_13 = "13. Which BMW features vertically sliding doors? \n A. M1 \n B. E12 \n C. I8\n D. Z1"
question_14 = "14. What is the largest BMW ever built? \n A. X7\n B. M12 \n C. Z4\n D. E90"
question_15 = "15. Which BMW was known as a bubble car? \n A. HEINKEL KABINE\n B. ATTICA \n C. PULI\n D. ISETTA"
question_16 = "16. What year was BMW founded? \n A. 1926 \n B. 1896 \n C. 1906\n D. 1916"
question_17 = "17. What was BMW\'s first motorcycle? \n A. K100 \n B. K1 \n C. R32\n D. R12"
question_18 = "18. The 303 was the first BMW with a ______. \n A. V6 Engine\n B. V8 Engine\n C. V4 Engine\n D. V12 Engine"
question_19 = "19. What was the company\'s first post WW11 vehicle? \n A. BMW Z1 \n B. BMW 326 \n C. BMW 501\n D. BMW 700"
question_20 = "20. Which BMW was almost a Lamborghini? \n A. E12\n B. M1\n C. Z1\n D. I8"
questions = {question_1: 'a', question_2: 'd',question_3: 'b', question_4: 'c', question_5: 'd', question_6: 'c', question_7: 'c', question_8: 'b', question_9: 'd', 
             question_10:'a', question_11: 'b', question_12: 'd', question_13:'d', question_14: 'a', question_15: 'd', question_16: 'd', question_17: 'c', 
             question_18: 'a', question_19: 'c', question_20:'b'}
comments =  {question_1: 'BMW stands for Bayerische Motoren Werke, or translated into English,Bavarian Motor Works', 
             question_2: 'While many think the blue and white checkered design is representative of a spinning aircraft propeller,' 
             'it is in fact a combination of the Rapp Motorenwerke company from which BMW grew, and the colors of the Bavarian flag.',
             question_3: 'The BMW slogan “Sheer Driving Pleasure” has evolved over the years from various brand claims in German.' 
             'The term “pleasure” first appeared in the 1930s in BMW ads.', question_4: '', question_5: '', question_6: '', question_7: '', question_8: '', question_9: '', 
             question_10:'', question_11: '', question_12: '', question_13:'', question_14: '', question_15: '', question_16: '', question_17: '', 
             question_18: '', question_19: '', question_20:''}
for i in questions and comments:
    print(i)
    answer = input("pick you answer: \n")
    if answer.lower() == questions[i]:
        print(f"[bold blue]Welldone! {answer}i s the correct answer :smile:\n{comments[i]}")
        score += 1
    else:
        print(f'[bold blue]Sorry {questions[i]} is the correct answer :thumbsdown:')
def get_result(user_score):
    print(f'[bold blue]You got {user_score} out of 20 questions right! ')
    print(f'[bold blue]You got {user_score /20 *100}%')
get_result(score)   













