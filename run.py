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
        print(f"Welldone! {user_answer} is the correct answer")
    else:
        print('[blue]"Sorry option a is the correct answer"')    
 
answer= input('[bold blue]1. What does BMW stand for? \n A.Bayerische Motoren Werke \n B. \n Pick your answer: ')
get_user_answer_1(answer)

def get_user_answer_2(user_answer):
    if answer.lower() == 'b':
        print(f"Welldone! {user_answer} is the correct answer")
    else:
        print('[blue]"Sorry option b is the correct answer"')
answer = input('[bold white]2. What is the slogan of BMW? \n A. The Ultimate Driving Power \n B. Sheer Driving Pleasure \n C. Enjoy the Ride \n D. Joy of discovery \n Pick your answer: ')
get_user_answer_2(answer)    
   
      

