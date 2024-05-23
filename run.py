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


def get_user_answer(user_answer):
    if answer.lower() == 'a':
        print(f"Correct! {user_answer} is the correct answer")
answer = input('[blue]What does BMW stand for? \n A.Bayerische Motoren Werke \n B. \n Pick your answer: ')
get_user_answer(answer)  
      

