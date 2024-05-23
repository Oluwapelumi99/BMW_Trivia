# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

from rich import print 
print('[bold blue]Welcome to my BMW Trivia!!')

continue_trivia = input('Do you want to start quiz? yes or no  ')
if continue_trivia.lower() == 'yes':
    print('[bold white] Brace yourself for a challenge!')
elif continue_trivia.lower() == 'no':
    print('[bold white] Sad to see you go this time')  
else:
    print('[bold white] Wrong input. Please try again..')


def get_user_answer_1(user_answer):
    if answer.lower() == 'a':
        print(f"[bold blue]Welldone! {user_answer} is the correct answer")
    else:
        print('[italic bold white]"Sorry option a is the correct answer"')    
 
answer= input('[bold blue]1. What does BMW stand for? \n A.Bayerische Motoren Werke \n B. \n Pick your answer: ')
get_user_answer_1(answer)


def get_user_answer_2(user_answer):
    if answer.lower() == 'b':
        print(f"[bold blue]Welldone! {user_answer} is the correct answer")
    else:
        print('[bold white]"Sorry option b is the correct answer"')
answer = input('[bold white]2. What is the slogan of BMW? \n A. The Ultimate Driving Power \n B. Sheer Driving Pleasure \n C. Enjoy the Ride \n D. Joy of discovery \n Pick your answer: ')
get_user_answer_2(answer)    
   
def get_user_answer_3(user_answer):
    if answer.lower() == 'c':
        print(f"[bold blue]Welldone! {user_answer} is the correct answer")
    else:
        print('[bold white]"Sorry option c is the correct answer"')
answer = input('[bold white]2. What is the BMW M series? \n A. A line of electric cars \n B. An SUV for off-roading \n C. A line of performance cars \n D. A line of luxury sedan \n Pick your answer: ')
get_user_answer_3(answer)  


def get_user_answer_4(user_answer):
    if answer.lower() == 'd':
        print(f"[bold blue]Welldone! {user_answer} is the correct answer")
    else:
        print('[blue]"Sorry option c is the correct answer"')
answer = input('[bold white]2. What was the name of BMW\'s first car? \n A. 3 Series \n B. 5 Series \n C. 7 Series\n D. Dixi \n Pick your answer: ')
get_user_answer_4(answer)  

def get_user_answer_5(user_answer):
    if answer.lower() == 'c':
        print(f"[bold blue]Welldone! {user_answer} is the correct answer")
    else:
        print('[blue]"Sorry option c is the correct answer"')
answer = input('[bold white]2. What year was the BMW 3 Series first intoduced? \n A. 1969 \n B. 1961 \n C. 1975\n D. 1984 \n Pick your answer: ')
get_user_answer_5(answer)  
