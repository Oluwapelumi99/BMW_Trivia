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
# def get_username(name):
#     return input(name)
# def print_name(value_name):
#     print(value_name)
# name = get_username('Enter your name to start the quiz:').upper
# print_name(f'[bold blue]Hello {name}. WELCOME TO MY BMW TRIVIA!!! :smile:')
  
# import ascii_magic
# output = ascii_magic.from_images_file('IMG_9484.JPG',columns=200,char='#') 
# ascii_magic.to_terminal(output)

score = 0
start_trivia = True
while start_trivia:
    try:
        continue_trivia = input("Do you want to start quiz? yes/no\n  ")
        if continue_trivia.lower() == 'yes':
            break  
        elif continue_trivia.lower() == 'no':
            print('[bold blue] Sad to see you go this time')
            start_trivia == False                   
    except KeyError:
        print('[bold blue] Wrong input. Please input yes or no')
        
print('[bold blue] Brace yourself for some BMW history:thumbsup: !'
'\n'
'\n Read instructions carefully.'
'\n'
'There are 20 questions in this Quiz,'
'\n pick your answer by inputing an option between A-D.\n Goodluck!')       
# question_1 = "1. What does BMW stand for? \n A. Bayerische Motoren Werke \n B. Brunswick Motoren Werke \n C. Borgholzzhausen Motoren Werke\n D. Berlin Motorenn Werke"
# question_2 = "2. What color is the BMW logo? \n A. Blue & gold \n B. Red & gold \n C. Red & White \n D. Blue & white"
# question_3 = "3. What is the slogan of BMW? \n A. The Ultimate Driving Power \n B. Sheer Driving Pleasure\n C. Enjoy the Ride \n D. Joy of discovery"
# question_4 = "4. What is the BMW M series? \n A. A line of electric cars \n B. An SUV for off-roading \n C. A line of performance cars \n D. A line of luxury sedan"
# question_5 = "5. What was the name of BMW\'s first car? \n A. 3 Series \n B. 5 Series \n C. 7 Series\n D. Dixi"
# question_6 = "6. What year was the BMW 3 Series first intoduced? \n A. 1969 \n B. 1961 \n C. 1975\n D. 1984"
# question_7 = "7. How far could BMW\'s first all-electric car drive before running out of battery? \n A. 79 miles\n B. 59 miles \n C. 19 miles\n D. 39 miles"
# question_8 = "8. What is BMW\'s Formula One racing team called? \n A. BMW Motorsport \n B. BMW Sauber F1 Team \n C. BMW M Racing\n D. BMW Racing Team"
# question_9 = "9. What is BMW\'s headquartwes shaped like? \n A. A Radiator \n B. A catalytic converter \n C. A Piston\n D. A Four-Cylinder Engine"
# question_10 = "10. What was BMW\'s first product? \n A. Aircraft Engine \n B. Spark plug \n C. A Tractor\n D. Motorcycle"
# question_11 = "11. What grille design has become a defining feature of BMW\'s automobiles? \n A. Heart grille \n B. Kidney grille \n C. Pharynx grille\n D. Liver grille"
# question_12 = "12. What race did the BMW 328 win in 1936? \n A. Alpine Rally \n B. Österreichise Alpenfahrt \n C. Mille Miglia\n D. Eifelrennen"
# question_13 = "13. Which BMW features vertically sliding doors? \n A. M1 \n B. E12 \n C. I8\n D. Z1"
# question_14 = "14. What is the largest BMW ever built? \n A. X7\n B. M12 \n C. Z4\n D. E90"
# question_15 = "15. Which BMW was known as a bubble car? \n A. HEINKEL KABINE\n B. ATTICA \n C. PULI\n D. ISETTA"
# question_16 = "16. What year was BMW founded? \n A. 1926 \n B. 1896 \n C. 1906\n D. 1916"
# question_17 = "17. What was BMW\'s first motorcycle? \n A. K100 \n B. K1 \n C. R32\n D. R12"
# question_18 = "18. The 303 was the first BMW with a ______. \n A. V6 Engine\n B. V8 Engine\n C. V4 Engine\n D. V12 Engine"
# question_19 = "19. What was the company\'s first post WW11 vehicle? \n A. BMW Z1 \n B. BMW 326 \n C. BMW 501\n D. BMW 700"
# question_20 = "20. Which BMW was almost a Lamborghini? \n A. E12\n B. M1\n C. Z1\n D. I8"
# questions = {question_1: 'a', question_2: 'd',question_3: 'b', question_4: 'c', question_5: 'd', question_6: 'c', question_7: 'c', question_8: 'b', question_9: 'd', 
#              question_10:'a', question_11: 'b', question_12: 'd', question_13:'d', question_14: 'a', question_15: 'd', question_16: 'd', question_17: 'c', 
#              question_18: 'a', question_19: 'c', question_20:'b'}
# comments =  {question_1: 'BMW stands for Bayerische Motoren Werke, or translated into English,Bavarian Motor Works', 
#              question_2: '',
#              question_3: 'The BMW slogan “Sheer Driving Pleasure” has evolved over the years from various brand claims in German.' 
#              '\nThe term “pleasure” first appeared in the 1930s in BMW ads.', 
#              question_4: 'The “M” in the BMW M Series stands for “Motorsport”, and the M Series was originally created to facilitate BMW\'s racing program.' 
#              '\nOver time, the BMW M program began to supplement their vehicle lineup with modified vehicle models, which are now available to the general public.', 
#              question_5: 'BMW became an automobile manufacturer in 1928 when it purchased Fahrzeugfabrik Eisenach,' 
#              '\nwhich built Austin Sevens at that time under licence (under the Dixi marque). The first car sold as a BMW was a rebadged Dixi called the BMW 3/15.', 
#              question_6: 'The BMW 3 Series is a line of compact executive cars manufactured by the German automaker BMW since May 1975.'
#              '\nIt is the successor to the 02 Series and has been produced in seven generations.', 
#              question_7: 'Conceived as a prototype in 1969, the BMW 1602e premiered at the 1972 Olympic Games in Munich. The battery powered Beemer could accelerate'
#              '\nfrom 0-31mph in 8.0 seconds,toppped out at 62mph, and had a range of about 19miles.', 
#              question_8: 'BMW Sauber were a constructor which competed in the Formula One World Championship between 2006 and 2009.' 
#              '\nThe team emerged as a result of the purchase of the Sauber team by BMW in 2006.', 
#              question_9: 'In 1973, the manufacturer opened its distinctive \'four-cylinder\'building in Munich, Germany.'
#              '\nIt is often cited as one of the most notable examples of architecture in Munich.', 
#              question_10: 'The BMW IIIa aircraft engine was known for good fuel economy and high-altitude performance.'
#              '\n The resulting orders for IIIa engines from the German military caused rapid expansion for BMW.', 
#              question_11: 'The \"Kidney grille\", first used in BMW\'s 1933 model 303, is named after kidneys because of its identical'
#              '\ndual structure, rather than the single grille design that was used by most cars at the time.', 
#              question_12: 'The 328 was first introdeced at the Eifelrennen race at the Nürburgring in 1936, where Ernst Henne drove'
#              '\nit to win the 2.0-litre class. The 328 had more than 100 class wins in 1937, including thr RAC Tourist Trophy,the'
#              '\nÖsterreichische Alpenfahrt,and the La Turbie hillclimb.', 
#              question_13: 'The BMW Z1 roadster was one of BMW Technik GmbH\'s first big projects. In addition to the unique door design,'
#              '\nthe Z1 body featured several other innovations: removable plastic body panels, a flat undertray, a roll-hope integrated'
#              '\ninto the windscreen surround and continuously zinc welded seams.', 
#              question_14: 'With standard seating for seven, the BMW X7 is more than just the biggest BMW ever built. It is advertised as '
#              '\n the most comfortable and luxurious Sports activity Vehicle in its class', 
#              question_15: 'In 1955, the BMW Isetta became the world\'s first mass-production car to achieve a fuel consumption of 3L/100km'
#              '\n(94mpg; 78mpg). It was the top-selling single-cylinder car in the world,with 161,728 units sold.', 
#              question_16: 'BMW\'s corporate history considers the founding date of Bayerische Flugzeugwerke(7 March 1916) to be the birth of the company.', 
#              question_17: 'BMW bega production of motorcycles in 1923, with the R32 model. The R32 established the boxer-twin, shaft-drive'
#              '\npowertrain layout that BMW would use for many years to come.', 
#              question_18: '', 
#              question_19: '', 
#              question_20: '' }
# for i in questions and comments:
#     print(i)
#     answer = input("pick you answer: \n")
#     if answer.lower() == questions[i]:
#         print(f"[bold blue]Welldone! {answer} is the correct answer :smile:\n{comments[i]}")
#         score += 1
#     else:
#         print(f'[bold blue]Sorry {questions[i]} is the correct answer :thumbsdown:\n{comments[i]}')
quiz_questions = [
    {
        'question': '1. What does BMW stand for?'
        '\n---------------------------'
        '\n',
        'choices' : [
            'A. Bayerische Motoren Werke',
            'B. Brunswick Motoren Werke', 
            'C. Borgholzzhausen Motoren Werke',
            'D. Berlin Motorenn Werke'
            '\n',
        ],
        'correct_answer':'A',
        'comment': 'BMW stands for Bayerische Motoren Werke, or translated into English,Bavarian Motor Works'
        '\n',
    },
    {
        "question": '2. What color is the BMW logo?'
        '\n-----------------------------'
        '\n', 
        'choices' : [
            'A. Blue & gold', 
            'B. Red & gold',
            'C. Red & White', 
            'D. Blue & white'
            '\n',
        ],
        'correct_answer': 'D',
        'comment': ''
        '\n',        
    },
    {    'question': "3. What is the slogan of BMW?"
        '\n-----------------------------'
        '\n',
        'choices': [
           'A. The Ultimate Driving Power',
           'B. Sheer Driving Pleasure',
           'C. Enjoy the Ride',
           'D. Joy of discovery'
           '\n', 
        ],
        'correct_answer': 'B',
        'comment': 'The BMW slogan “Sheer Driving Pleasure” has evolved over the years from various brand claims in German.'
        '\nThe term “pleasure” first appeared in the 1930s in BMW ads'
        '\n',
    },
    {
        'question': '4. What is the BMW M series?'
        '\n----------------------------'
        '\n',
        'choices': [
          'A. A line of electric cars',          
          'B. An SUV for off-roading',
          'C. A line of performance cars',
          'D. A line of luxury sedan'
          '\n', 
        ],
        'correct_answer': 'C',
        'comment': 'The “M” in the BMW M Series stands for “Motorsport”, and the M Series was originally created to facilitate BMW\'s racing program.' 
        '\nOver time, the BMW M program began to supplement their vehicle lineup with modified vehicle models, which are now available to the general public.'
        '\n',
    },
    {
      'question': '5. What was the name of BMW\'s first car?'
      '\n---------------------------------------'
      '\n',
      'choices': [
          'A. 3 Series',
          'B. 5 Series',
          'C. 7 Series',
          'D. Dixi'
          '\n',
      ],
      'correct_answer': 'D',
      'comment': 'BMW became an automobile manufacturer in 1928 when it purchased Fahrzeugfabrik Eisenach,' 
            '\nwhich built Austin Sevens at that time under licence (under the Dixi marque). The first car sold as a BMW was a rebadged Dixi called the BMW 3/15.'
            '\n',
 
    },
    {
     'question': '6. What year was the BMW 3 Series first intoduced?'
     '\n--------------------------------------------------'
     '\n',
     'choices': [
         'A. 1969',
         'B. 1961',
         'C. 1975',
         'D. 1984'
         '\n',
     ],
     'correct_answer': 'C',
     'comment': 'The BMW 3 Series is a line of compact executive cars manufactured by the German automaker BMW since May 1975.'
             '\nIt is the successor to the 02 Series and has been produced in seven generations.'
             '\n',  
    },
    {  
     'question': '7. How far could BMW\'s first all-electric car drive before running out of battery?'
     '\n----------------------------------------------------------------------------------',
     'choices': [
        'A. 79 miles',
        'B. 59 miles', 
        'C. 19 miles',
        'D. 39 miles'
        '\n', 
     ],
     'correct_answer': 'C',
     'comment': 'Conceived as a prototype in 1969, the BMW 1602e premiered at the 1972 Olympic Games in Munich. The battery powered Beemer could accelerate'
             '\nfrom 0-31mph in 8.0 seconds,toppped out at 62mph, and had a range of about 19miles.'
             '\n',
    },
    {
      'question': '8. What is BMW\'s Formula One racing team called?'
      '\n-----------------------------------------------',
      'choices': [
        'A. BMW Motorsport',
        'B. BMW Sauber F1 Team ',
        'C. BMW M Racing',
        'D. BMW Racing Team'
        '\n',  
      ],
      'correct_answer': 'B',
      'comment': 'BMW Sauber were a constructor which competed in the Formula One World Championship between 2006 and 2009.' 
              '\nThe team emerged as a result of the purchase of the Sauber team by BMW in 2006.'
              '\n',
    },
    {
      'question': '9. What is BMW\'s headquartwes shaped like?'
      '\n-----------------------------------------',
      'choices': [
          'A. Radiator',
          'B. catalytic converter', 
          'C. A Piston',
          'D. A Four-Cylinder Engine',
       '\n',   
      ],
      'correct_answer': 'D',
      'comment': 'In 1973, the manufacturer opened its distinctive \'four-cylinder\'building in Munich, Germany.'
             '\nIt is often cited as one of the most notable examples of architecture in Munich.'
             '\n',  
    },
    {
      'question': '10. What was BMW\'s first product?'
      '\n--------------------------------',
      'choices': [
          'A. Aircraft Engine',
          'B. Spark plug',
          'C. A Tractor',
          'D. Motorcycle'
          '\n',
      ],
      'correct_answer': 'A',
      'comment': 'The BMW IIIa aircraft engine was known for good fuel economy and high-altitude performance.'
             '\n The resulting orders for IIIa engines from the German military caused rapid expansion for BMW.'
             '\n',  
    },
    {
     'question': '11. What grille design has become a defining feature of BMW\'s automobiles?'
     '\n--------------------------------------------------------------------------',
     'choices': [
        'A. Heart grille',
        'B. Kidney grille',
        'C. Pharynx grille',
        'D. Liver grille'
     ],
     'correct_answer': 'B',
     'comment': 'The \"Kidney grille\", first used in BMW\'s 1933 model 303, is named after kidneys because of its identical'
              '\ndual structure, rather than the single grille design that was used by most cars at the time.'
              '\n',   
    },
    {
      'question': '12. What race did the BMW 328 win in 1936?'
      '\n------------------------------------------',
      'choices': [
          'A. Alpine Rally',
          'B. Österreichise Alpenfahrt',
          'C. Mille Miglia',
          'D. Eifelrennen'
          '\n',
      ],
      'correct_answer': 'D',
      'comment': 'The 328 was first introdeced at the Eifelrennen race at the Nürburgring in 1936, where Ernst Henne drove'
              '\nit to win the 2.0-litre class. The 328 had more than 100 class wins in 1937, including thr RAC Tourist Trophy,the'
             '\nÖsterreichische Alpenfahrt,and the La Turbie hillclimb.'
             '\n',  
    },
    
    {
      'question': '13. Which BMW features vertically sliding doors?'
      '\n------------------------------------------------',
      'choices': [
          'A. M1',
          'B. E12',
          'C. I8',
          'D. Z1'
       '\n',   
      ],
      'correct_answer': 'D',
      'comment': 'The BMW Z1 roadster was one of BMW Technik GmbH\'s first big projects. In addition to the unique door design,'
            '\nthe Z1 body featured several other innovations: removable plastic body panels, a flat undertray, a roll-hope integrated'
            '\ninto the windscreen surround and continuously zinc welded seams.'
            '\n',  
    },
    {
      'question': '14. What is the largest BMW ever built?'
      '\n---------------------------------------',
      'choices': [
          'A. X7',
          'B. M12',
          'C. Z4',
          'D. E90'
       '\n',   
      ],
      'correct_answer': 'A',
      'comment': 'With standard seating for seven, the BMW X7 is more than just the biggest BMW ever built. It is advertised as '
             '\n the most comfortable and luxurious Sports activity Vehicle in its class'
             '\n',  
    },
    {
      'question': '15. Which BMW was known as a bubble car?'
      '\n----------------------------------------',
      'choices': [
          'A. HEINKEL KABINE',
          'B. ATTICA',
          'C. PULI',
          'D. ISETTA'
       '\n',   
      ],
      'correct_answer': 'D',
      'comment': 'In 1955, the BMW Isetta became the world\'s first mass-production car to achieve a fuel consumption of 3L/100km'
                '\n(94mpg; 78mpg). It was the top-selling single-cylinder car in the world,with 161,728 units sold'
                '\n',  
    },
    {
      'question': '16. What year was BMW founded?'
      '\n------------------------------',
      'choices': [
          'A. 1926',
          'B. 1896',
          'C. 1906',
          'D. 1916'
       '\n',   
      ],
      'correct_answer': 'D',
      'comment': 'BMW\'s corporate history considers the founding date of Bayerische Flugzeugwerke(7 March 1916) to be the birth of the company.'
      '\n',  
    },
    {
      'question': '17. What was BMW\'s first motorcycle?'
      '\n------------------------------------',
      'choices': [
          'A. K100',
          'B. K1',
          'C. R32',
          'D. R12'
       '\n',   
      ],
      'correct_answer': 'C',
      'comment': 'BMW bega production of motorcycles in 1923, with the R32 model. The R32 established the boxer-twin, shaft-drive'
              '\npowertrain layout that BMW would use for many years to come.'
              '\n',  
    },
    {
      'question': '18. The 303 was the first BMW with a ______.'
      '\n--------------------------------------------',
      'choices': [
          'A. V6 Engine',
          'B. V8 Engine',
          'C. V4 Engine',
          'D. V12 Engine'
       '\n',   
      ],
      'correct_answer': 'A',
      'comment': ''
      '\n',  
    },
    {
      'question':'19. What was the company\'s first post WW11 vehicle?'
      '\n---------------------------------------------------',
      'choices': [
          'A. BMW Z1',
          'B. BMW 326',
          'C. BMW 501',
          'D. BMW 700'
       '\n',   
      ],
      'correct_answer': 'C',
      'comment': ''
      '\n',  
    },
    {
      'question': '20. Which BMW was almost a Lamborghini?'
      '\n---------------------------------------',
      'choices': [
          'A. E12',
          'B. M1',
          'C. Z1',
          'D. I8'
       '\n',   
      ],
      'correct_answer': 'B',
      'comment': ''
      '\n',  
    },
         
]
print('---------------------------')
for quiz_question in quiz_questions:
    print(quiz_question['question'])
    for answer in quiz_question['choices']:
        print(answer)
        
    user_answer = input('Pick your answer: \n').upper()
    
    if user_answer == quiz_question['correct_answer']:
        print(f'[bold blue]Well done! {user_answer} is the correct answer :smile: \n{quiz_question['comment']}')
        score += 1
    else:
        print(f'[bold blue]Sorry {quiz_question['correct_answer']} is the correct answer :thumbsdown: \n{quiz_question['comment']}')
# def get_result(user_score):
#     print(f'[bold blue] Hi {name} you got {user_score} out of 20 questions right! ')
#     print(f'[bold blue]You got {user_score /20 *100}%')
# get_result(score)

# def get_user_choice(play_again):
#     if choice.lower() == 'yes':
#         print(f'[bold blue]You have decided to end the quiz. Your final percentage is {user_score /20 *100}%')
#        
#     else:
#         continue
# choice = input('Do you try again? yes/no: ')
# get_user_choice(choice)








