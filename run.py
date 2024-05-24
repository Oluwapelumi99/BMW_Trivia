# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

from rich import print 
print('[bold blue]Welcome to my BMW Trivia!!')
score = 0 
start_trivia = True
print('[bold blue]Do you want to start quiz?')
while start_trivia:
    try:
        continue_trivia = input(" yes/no  ")
        if continue_trivia.lower() == 'yes':
            print('[bold blue] Brace yourself for a challenge!')
            break  
        elif continue_trivia.lower() == 'no':           
            print('[bold blue] Sad to see you go this time')
            start_trivia = False
    except:
        print('[bold white] Wrong input. Please try again..')

def get_user_answer_0(user_answer):
    if answer.lower() == 'a':
        print(f"[bold blue]Welldone! {user_answer} is the correct answer")
        global score
        score += 1
    else:
        print('[italic bold white]"Sorry...option a is the correct answer"')    
 
answer= input('[bold blue]1. What does BMW stand for? \n A. Bayerische Motoren Werke \n B. Brunswick Motoren Werke \n C. Borgholzzhausen Motoren Werke\n D. Berlin Motorenn Werke\n Pick your answer: ')
get_user_answer_0(answer)

def get_user_answer_0(user_answer):
    if answer.lower() == 'd':
        print(f"[bold blue]Welldone! {user_answer} is the correct answer")
        global score
        score += 1
    else:
        print('[italic bold white]"Sorry...option d is the correct answer"')    
 
answer= input('[bold blue]2. What color is the BMW logo \n A. Blue & gold \n B. Red & gold \n C. Red & White \n D. Blue & white \n Pick your answer: ')
get_user_answer_0(answer)

def get_user_answer_2(user_answer):
    if answer.lower() == 'b':
        print(f"[bold blue]Welldone! {user_answer} is the correct answer")
        global score
        score += 1
    else:
        print('[bold white]"Sorry...option b is the correct answer"')
answer = input('[bold blue]3. What is the slogan of BMW? \n A. The Ultimate Driving Power \n B. Sheer Driving Pleasure\n'
                  'C. Enjoy the Ride \n D. Joy of discovery \n Pick your answer: ')
get_user_answer_2(answer)    
   
def get_user_answer_3(user_answer):
    if answer.lower() == 'c':
        print(f"[bold blue]Welldone! {user_answer} is the correct answer")
        global score
        score += 1
    else:
        print('[bold white]"Sorry...option c is the correct answer"')
answer = input('[bold white]4. What is the BMW M series? \n A. A line of electric cars \n B. An SUV for off-roading \n' 
                'C. A line of performance cars \n D. A line of luxury sedan \n Pick your answer: ')
get_user_answer_3(answer)  


def get_user_answer_4(user_answer):
    if answer.lower() == 'd':
        print(f"[bold blue]Welldone! {user_answer} is the correct answer")
        global score
        score += 1
    else:
        print('[blue]"Sorry...option c is the correct answer"')
answer = input('[bold white]5. What was the name of BMW\'s first car? \n A. 3 Series \n B. 5 Series \n' 
                'C. 7 Series\n D. Dixi \n Pick your answer: ')
get_user_answer_4(answer)  

def get_user_answer_5(user_answer):
    if answer.lower() == 'c':
        print(f"[bold blue]Welldone! {user_answer} is the correct answer")
        global score
        score += 1
    else:
        print('[blue]"Sorry...option c is the correct answer"')
answer = input('[bold white]6. What year was the BMW 3 Series first intoduced? \n A. 1969 \n B. 1961 \n' 
                'C. 1975\n D. 1984 \n Pick your answer: ')
get_user_answer_5(answer)  

def get_user_answer_6(user_answer):
    if answer.lower() == 'c':
        print(f"[bold blue]Welldone! {user_answer} is the correct answer")
        global score
        score += 1
    else:
        print('[blue]"Sorry...option c is the correct answer"')
answer = input('[bold white]7. How far could BMW\'s first all-electric car drive before running out of battery? \n A. 79 miles\n B. 59 miles \n C. 19 miles\n D. 39 miles\n Pick your answer: ')
get_user_answer_6(answer) 

def get_user_answer_7(user_answer):
    if answer.lower() == 'b':
        print(f"[bold blue]Welldone! {user_answer} is the correct answer")
        global score
        score += 1
    else:
        print('[blue]"Sorry...option b is the correct answer"')
answer = input('[bold white]8. What is BMW\'s Formula One racing team called? \n A. BMW Motorsport \n B. BMW Sauber F1 Team \n C. BMW M Racing\n D. BMW Racing Team \n Pick your answer: ')
get_user_answer_7(answer)

def get_user_answer_8(user_answer):
    if answer.lower() == 'd':
        print(f"[bold blue]Welldone! {user_answer} is the correct answer")
        global score
        score += 1
    else:
        print('[blue]"Sorry...option d is the correct answer"')
answer = input('[bold white]9. What is BMW\'s headquartwes shaped like? \n A. A Radiator \n B. A catalytic converter \n C. A Piston\n D. A Four-Cylinder Engine \n Pick your answer: ')
get_user_answer_8(answer)

def get_user_answer_9(user_answer):
    if answer.lower() == 'a':
        print(f"[bold blue]Welldone! {user_answer} is the correct answer")
        global score
        score += 1
    else:
        print('[blue]"Sorry...option a is the correct answer"')
answer = input('[bold white]10. What was BMW\'s first product? \n A. Aircraft Engine \n B. Spark plug \n C. A Tractor\n D. Motorcycle \n Pick your answer: ')
get_user_answer_9(answer)

def get_user_answer_10(user_answer):
    if answer.lower() == 'b':
        print(f"[bold blue]Welldone! {user_answer} is the correct answer")
        global score
        score += 1
    else:
        print('[blue]"Sorry...option b is the correct answer"')
answer = input('[bold white]11. What grille design has become a defining feature of BMW\'s automobiles? \n A. Heart grille \n B. Kidney grille \n C. Pharynx grille\n D. Liver grille \n Pick your answer: ')
get_user_answer_10(answer)


def get_user_answer_11(user_answer):
    if answer.lower() == 'd':
        print(f"[bold blue]Welldone! {user_answer} is the correct answer")
        global score
        score += 1
    else:
        print('[blue]"Sorry...option d is the correct answer"')
answer = input('[bold white]12. What race did the BMW 328 win in 1936? \n A. Alpine Rally \n B. Österreichise Alpenfahrt \n C. Mille Miglia\n D. Eifelrennen \n Pick your answer: ')
get_user_answer_11(answer)

def get_user_answer_12(user_answer):
    if answer.lower() == 'd':
        print(f"[bold blue]Welldone! {user_answer} is the correct answer")
        global score
        score += 1
    else:
        print('[blue]"Sorry...option d is the correct answer"')
answer = input('[bold white]13. Which BMW features vertically sliding doors? \n A. M1 \n B. E12 \n C. I8\n D. Z1 \n Pick your answer: ')
get_user_answer_12(answer)

def get_user_answer_13(user_answer):
    if answer.lower() == 'a':
        print(f"[bold blue]Welldone! {user_answer} is the correct answer")
        global score
        score += 1
    else:
        print('[blue]"Sorry...option a is the correct answer"')
answer = input('[bold white]14. What is the largest BMW ever built? \n A. X7\n B. M12 \n C. Z4\n D. E90 \n Pick your answer: ')
get_user_answer_13(answer)

def get_user_answer_14(user_answer):
    if answer.lower() == 'd':
        print(f"[bold blue]Welldone! {user_answer} is the correct answer")
        global score
        score += 1
    else:
        print('[blue]"Sorry...option d is the correct answer"')
answer = input('[bold white]15. Which BMW was known as a "bubble car"? \n A. HEINKEL KABINE\n B. ATTICA \n C. PULI\n D. ISETTA \n Pick your answer: ')
get_user_answer_14(answer)

def get_user_answer_15(user_answer):
    if answer.lower() == 'd':
        print(f"[bold blue]Welldone! {user_answer} is the correct answer")
        global score
        score += 1
    else:
        print('[blue]"Sorry...option d is the correct answer"')
answer = input('[bold white]16. What year was BMW founded? \n A. 1926 \n B. 1896 \n C. 1906\n D. 1916 \n Pick your answer: ')
get_user_answer_15(answer)

def get_user_answer_16(user_answer):
    if answer.lower() == 'c':
        print(f"[bold blue]Welldone! {user_answer} is the correct answer")
        global score
        score += 1
    else:
        print('[blue]"Sorry...option c is the correct answer"')
answer = input('[bold white]17. What was BMW\'s first motorcycle? \n A. K100 \n B. K1 \n C. R32\n D. R12 \n Pick your answer: ')
get_user_answer_16(answer)

def get_user_answer_17(user_answer):
    if answer.lower() == 'a':
        print(f"[bold blue]Welldone! {user_answer} is the correct answer")
        global score
        score += 1
    else:
        print('[blue]"Sorry...option a is the correct answer"')
answer = input('[bold white]18. The 303 was the first BMW with a ______. \n A. V6 Engine\n B. V8 Engine\n C. V4 Engine\n D. V12 Engine \n Pick your answer: ')
get_user_answer_17(answer)

def get_user_answer_18(user_answer):
    if answer.lower() == 'c':
        print(f"[bold blue]Welldone! {user_answer} is the correct answer")
        global score
        score += 1
    else:
        print('[blue]"Sorry...option c is the correct answer"')
answer = input('[bold white]19. What was the company\'s first post WW11 vehicle? \n A. BMW Z1 \n B. BMW 326 \n C. BMW 501\n D. BMW 700 \n Pick your answer: ')
get_user_answer_18(answer)

def get_user_answer_19(user_answer):
    if answer.lower() == 'b':
        print(f"[bold blue]Welldone! {user_answer} is the correct answer")
        global score
        score += 1
    else:
        print('[blue]"Sorry...option b is the correct answer"')
answer = input('[bold white]20. Which BMW was almost a Lamborghini? \n A. E12\n B. M1\n C. Z1\n D. I8 \n Pick your answer: ')
get_user_answer_19(answer)


def get_result(user_score):
    print(f'[bold blue]You got {user_score} out of 20 questions right! ')
    print('You got ' + str((user_score/4) *100) + '%. ')
get_result(score)   











