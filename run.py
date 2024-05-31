from rich import print
import gspread
from google.oauth2.service_account import Credentials
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('bmw-trivia')


def get_welcome_message():
    """
    Prints welcome message to the terminal when code runs.
    """
    print('[bold blue] Brace yourself for some BMW history:thumbsup: !\n'
      '\nRead instructions carefully.\n'
      '\n'
      ' There are 20 questions in this Quiz.\n'
      '\n Pick your answer by inputing an option between A-D.\n Goodluck! \n')


def get_ascii():
    """
    Prints ascii after welcome message.
    """
    print("""
                           *+*********++                           
                       +**+*   ** +*   *+**+                       
                     **+       **++*       +**                     
                   ***+*+      * + **     *+ +**                   
                 +*++*+*+*+  ####***+*  **+** ++*+                 
                +*+ +*+**+########     +*  ***+ +*+                
                *+    ++##########       ++      +*                
               *+      *##########        ++      +*               
               *+     *###########         ++     +*               
              +*      ############          *      *+              
              +*      *          ############      *+              
               *+     ++         ###########*     +*               
               **      +         ##########*      +*               
               +*+      ++       ##########      +*+               
                +*+       *+     ########       **+                
                 **+        +*+*+*#####        +*+                 
                   ***                        **                   
                     **+                   +***                    
                       +**+*           *+**+                       
                          ++**********+++                          
"""'\n')


def start_trivia(score):
    """
    Asks if user wants to start quiz and gets and validates user input.
    """
    username = ''
    start_trivia = True
    while start_trivia:
        continue_trivia = input("Do you want to start quiz? yes/no \n  ")
        if continue_trivia.lower() == 'yes':
            username = get_username()
            break
        elif continue_trivia.lower() == 'no':
            print('[bold blue] Sad to see you go')
            quit()
        else:
            print('[bold blue] Wrong input. Please input yes or no')
    score = game_loop(score)
    return username, score


def get_username():
    """
    Get names inputs from the user
    """
    while True:
        print('[bold blue]Name must be less than 20 characters'
              ' and more than 2 characters.Your name must not contain'
              ' any special characters or spaces\n')
        print('[bold blue]For example: '' [bold white]Christopher \n')
        name = input('Enter your name to start the quiz: \n').strip()
        print(f'[bold blue] Hello {name}!. Let\'s play!!')
        
        if valid_name(name):
            break
    return name


def valid_name(name):
    """
    Gets Username and validates it.
    """
    if len(name) > 20:
        print('[bold blue]Name should be less than 20 characters\n')
        return False

    if len(name) < 3:
        print('[bold blue]Name must be at least 3 characters\n')
        return False

    if name.isalnum():
        print('[bold blue]Name should not contain any numbers')

    if not name.isalpha():
        print('[bold blue]Name should not contain any special characters or numbers\n')
        return False
    return True


quiz_questions = [
    {
        'question': '1. What does BMW stand for?'
        '\n---------------------------'
        '\n',
        'choices': [
            'A. Bayerische Motoren Werke',
            'B. Brunswick Motoren Werke',
            'C. Borgholzzhausen Motoren Werke',
            'D. Berlin Motorenn Werke\n',
        ],
        'correct_answer':'A',
        'incorrect_answer':
            [
                'B',
                'C',
                'D',
            ],
        'incorrect_input':'',
        'comment': 'BMW stands for Bayerische Motoren Werke,'
        ' or translated into English,Bavarian Motor Works\n',
    },
    {
        "question": '2. What color is the BMW logo?'
        '\n-----------------------------'
        '\n',
        'choices': [
            'A. Blue & gold',
            'B. Red & gold',
            'C. Red & White',
            'D. Blue & white\n',
        ],
        'correct_answer': 'D',
        'incorrect_answer': ['A', 'B', 'C'],
        'comment': 'While many think the blue and white checkered'
        ' design is representative of a spinning aircraft propeller,'
        '\nit is in fact a combination of the Rapp Motorenwerke company'
        ' from which BMW grew, and the colors of the Bavarian flag.\n',
    },
    {
        'question': "3. What is the slogan of BMW?"
        '\n-----------------------------'
        '\n',
        'choices': [
           'A. The Ultimate Driving Power',
           'B. Sheer Driving Pleasure',
           'C. Enjoy the Ride',
           'D. Joy of discovery\n',
        ],
        'correct_answer': 'B',
        'incorrect_answer': ['A', 'C', 'D'],
        'comment': 'The BMW slogan “Sheer Driving Pleasure” has evolved'
        ' over the years from various brand claims in German.'
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
          'D. A line of luxury sedan\n',
        ],
        'correct_answer': 'C',
        'incorrect_answer': ['A', 'B', 'D'],
        'comment': 'The “M” in the BMW M Series stands for'
        ' “Motorsport”, and the M Series was originally created to'
        ' facilitate BMW\'s racing program.'
        '\nOver time, the BMW M program began to supplement their vehicle'
        ' lineup with modified vehicle models, which are now available to the'
        ' general public.'
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
          'D. Dixi\n',
      ],
      'correct_answer': 'D',
      'incorrect_answer': ['A', 'B', 'C'],
      'comment': 'BMW became an automobile manufacturer in 1928 when it'
      ' purchased Fahrzeugfabrik Eisenach,'
      '\nwhich built Austin Sevens at that time under licence(under the'
      ' Dixi marque). The first car'
      'sold as a BMW was a rebadged Dixi called the BMW 3/15.\n',
    },
    {
     'question': '6. What year was the BMW 3 Series first intoduced?'
     '\n--------------------------------------------------'
     '\n',
     'choices': [
         'A. 1969',
         'B. 1961',
         'C. 1975',
         'D. 1984\n',
     ],
     'correct_answer': 'C',
     'incorrect_answer': ['A', 'B', 'D'],
     'comment': 'The BMW 3 Series is a line of compact executive cars'
     ' manufactured by the German automaker BMM'
     'since May 1975.\nIt is the successor to the 02 Series and has been'
     ' produced in seven generations.\n',
    },
    {
     'question': '7. How far could BMW\'s first all-electric car drive before'
     ' running out of battery?'
     '\n--------------------------------------------------------------------'
     '--------------',
     'choices': [
        'A. 79 miles',
        'B. 59 miles',
        'C. 19 miles',
        'D. 39 miles\n',
     ],
     'correct_answer': 'C',
     'incorrect_answer': ['A', 'B', 'D'],
     'comment': 'Conceived as a prototype in 1969, the BMW 1602e premiered at'
     ' the 1972 Olympic Games in Munich'
     '. The battery powered Beemer could accelerate\nfrom 0-31mph in'
     ' 8.0 seconds, toppped out at 62mph, and had'
     'a range of about 19miles.\n',
    },
    {
      'question': '8. What was BMW\'s Formula One racing team called?'
      '\n-----------------------------------------------',
      'choices': [
        'A. BMW Motorsport',
        'B. BMW Sauber F1 Team ',
        'C. BMW M Racing',
        'D. BMW Racing Team\n',
      ],
      'correct_answer': 'B',
      'incorrect_answer': ['A', 'C', 'D'],
      'comment': 'BMW Sauber were a constructor which competed in the Formula'
      ' One World Championship between'
      '2006 and 2009.\nThe team emerged as a result of the purchase of the'
      ' Sauber team by BMW in 2006.\n',
    },
    {
      'question': '9. What is BMW\'s headquartwes shaped like?'
      '\n-----------------------------------------',
      'choices': [
          'A. Radiator',
          'B. catalytic converter',
          'C. A Piston',
          'D. A Four-Cylinder Engine\n',
      ],
      'correct_answer': 'D',
      'incorrect_answer': ['A', 'B', 'C'],
      'comment': 'In 1973, the manufacturer opened its'
      ' distinctive \'four-cylinder\'building in Munich,'
      'Germany.\nIt is often cited as one of the most notable examples of'
      ' architecture in Munich.\n',
    },
    {
      'question': '10. What was BMW\'s first product?'
      '\n--------------------------------',
      'choices': [
          'A. Aircraft Engine',
          'B. Spark plug',
          'C. A Tractor',
          'D. Motorcycle\n',
      ],
      'correct_answer': 'A',
      'incorrect_answer': ['B', 'C', 'D'],
      'comment': 'The BMW IIIa aircraft engine was known for\n'
      ' good fuel economy and high-altitude performance'
      '\n The resulting orders for IIIa engines from the\n'
      ' German military caused rapid expansion for BMW.\n',
    },
    {
     'question': '11. What grille design has become a defining feature'
     ' of BMW\'s automobiles?'
     '\n----------------------------------------------------------------'
     '----------',
     'choices': [
        'A. Heart grille',
        'B. Kidney grille',
        'C. Pharynx grille',
        'D. Liver grille\n',
     ],
     'correct_answer': 'B',
     'incorrect_answer': ['A', 'C', 'D'],
     'comment': 'The \"Kidney grille\", first used in BMW\'s'
     '1933 model 303, is named after kidneys because of its identical'
     'dual structure, rather than the single grille design that was used'
     ' by most cars at the time.\n',
    },
    {
      'question': '12. What race did the BMW 328 win in 1936?'
      '\n------------------------------------------',
      'choices': [
          'A. Alpine Rally',
          'B. Österreichise Alpenfahrt',
          'C. Mille Miglia',
          'D. Eifelrennen\n',
      ],
      'correct_answer': 'D',
      'incorrect_answer': ['A', 'B', 'C'],
      'comment': 'The 328 was first introdeced at the Eifelrennen'
      'race at the Nürburgring in 1936, where Ernst Henne drove\nit'
      ' to win the 2.0-litre class. The 328 had more than 100 class'
      ' wins in 1937, including thr RAC Tourist Trophy,the'
      '\nÖsterreichische Alpenfahrt,and the La Turbie hillclimb\n',
    },
    {
      'question': '13. Which BMW features vertically sliding doors?'
      '\n------------------------------------------------',
      'choices': [
          'A. M1',
          'B. E12',
          'C. I8',
          'D. Z1\n',
      ],
      'correct_answer': 'D',
      'incorrect_answer': ['A', 'B', 'C'],
      'comment': 'The BMW Z1 roadster was one of BMW Technik GmbH\'s'
      ' first big projects. In addition to the unique door design,'
      '\nthe Z1 body featured several other innovations: removable plastic'
      ' body panels, a flat undertray, a roll-hope integrated\ninto the'
      ' windscreen surround and continuously zinc welded seams.\n',
    },
    {
      'question': '14. What is the largest BMW ever built?'
      '\n---------------------------------------',
      'choices': [
          'A. X7',
          'B. M12',
          'C. Z4',
          'D. E90\n',
      ],
      'correct_answer': 'A',
      'incorrect_answer': ['B', 'C', 'D'],
      'comment': 'With standard seating for seven, the BMW X7 is more than'
      ' just the biggest BMW ever built. It is advertised as the most'
      ' comfortable and luxurious Sports activity Vehicle in its class\n',
    },
    {
      'question': '15. Which BMW was known as a bubble car?'
      '\n----------------------------------------',
      'choices': [
          'A. HEINKEL KABINE',
          'B. ATTICA',
          'C. PULI',
          'D. ISETTA\n',
      ],
      'correct_answer': 'D',
      'incorrect_answer': ['A', 'B', 'C'],
      'comment': 'In 1955, the BMW Isetta became the world\'s first'
      ' mass-production car to achieve a fuel consumption of 3L/100km\n'
      '(94mpg; 78mpg). It was the top-selling single-cylinder car in the'
      ' world,with 161,728 units sold\n',
    },
    {
      'question': '16. What year was BMW founded?'
      '\n------------------------------',
      'choices': [
          'A. 1926',
          'B. 1896',
          'C. 1906',
          'D. 1916\n',
      ],
      'correct_answer': 'D',
      'incorrect_answer': ['A', 'B', 'C'],
      'comment': 'BMW\'s corporate history considers the founding date'
      ' of Bayerische Flugzeugwerke(7 March 1916) to be the birth of the'
      ' company.\n',
    },
    {
      'question': '17. What was BMW\'s first motorcycle?'
      '\n------------------------------------',
      'choices': [
          'A. K100',
          'B. K1',
          'C. R32',
          'D. R12\n',
      ],
      'correct_answer': 'C',
      'incorrect_answer': ['A', 'B', 'D'],
      'comment': 'BMW bega production of motorcycles in 1923, with the R32'
      ' model. The R32 established the boxer-twin, shaft-drive\npowertrain'
      ' layout that BMW would use for many years to come.\n',
    },
    {
      'question': '18. The 303 was the first BMW with a ______.'
      '\n--------------------------------------------',
      'choices': [
          'A. V6 Engine',
          'B. V8 Engine',
          'C. V4 Engine',
          'D. V12 Engine\n',
      ],
      'correct_answer': 'A',
      'incorrect_answer': ['B', 'C', 'D'],
      'comment': 'The 303 was the first BMW to use a straight-6 engine.'
      'The M78 1182 cc six-cylinder engine was developed frim the'
      'four-cylinder engine used in the 3/20.\n',
    },
    {
      'question': '19. What was the company\'s first post WW11 vehicle?'
      '\n---------------------------------------------------',
      'choices': [
          'A. BMW Z1',
          'B. BMW 326',
          'C. BMW 501',
          'D. BMW 700\n',
      ],
      'correct_answer': 'C',
      'incorrect_answer': ['A', 'B', 'D'],
      'comment': 'The BMW 501 served an important function: it helped'
      ' re-establish the automaker\'s reputation for creating'
      ' high-quality, performance-orineted cars\n',
    },
    {
      'question': '20. Which BMW was almost a Lamborghini?'
      '\n---------------------------------------',
      'choices': [
          'A. E12',
          'B. M1',
          'C. Z1',
          'D. I8\n',
      ],
      'correct_answer': 'B',
      'incorrect_answer': ['A', 'C', 'D'],
      'comment': 'Lambourghini was supposed to BMW in building a racing car,'
      ' but the agreement dissolved in 1978 due to the italian automaker\'s'
      ' finanacial issues. BMW completed the project and the M1 became the'
      ' first mid-engine car in the line-up.\n',
    },
]


def game_loop(score):
    """
    Gets quiz questions and answers and loops the game.
    """
    print('---------------------------')
    for quiz_question in quiz_questions:
        print(quiz_question['question'])
        for answer in quiz_question['choices']:
            print(answer)
        user_answer = True
        while user_answer:
            user_answer = input('Pick your answer: \n').upper()
            if user_answer == quiz_question['correct_answer']:
                print('[bold blue]Well done! ' + (user_answer) +
                      ' is the correct answer :smile: \n' +
                      (quiz_question['comment']))
                score += 1
                break
            elif user_answer in quiz_question['incorrect_answer']:
                print('[bold blue]Sorry ' + (quiz_question['correct_answer']) +
                      ' is the correct answer :thumbsdown: \n' +
                      (quiz_question['comment']))
                break
            else:
                print('[bold blue]Incorrect Input.'
                      'Please pick an option from A-D.')
                user_answer = True

    return score


def get_result(username, score):
    """
     Get users score and increment it by 1 with each correct
     answer and provide the total score after
     the player has completed the quiz.
    """
    print(f'[bold blue]Hi {username} you got {score}'
          ' out of 20 questions right! ')
    print(f'[bold blue]You got {score /20 *100}%')


def update_leaderboard(username, score):
    """
    Update Scoreboard worksheet to check for highest score
    """
    print('[bold blue]Updating score board....')
    scoreboard = SHEET.worksheet('scoreboard')
    scoreboard.append_row([username, score])
    scoreboard.sort((2, 'des'))
    print('[bold blue] Scoreboard updated successfully')


def display_leaderboard():
    """
    Get 5 highest scores and display to the terminal
    """
    scoreboard = SHEET.worksheet('scoreboard')
    data = scoreboard.get_values('A2:B6')
    print('[bold blue]Leaderboard top 5')
    for index, entry in enumerate(data):
        print((f'{index + 1}: {entry[0]}  {entry[1]}pts'))
def start_2():
    score = 0
    username = ''
    get_result(username, score)
    update_leaderboard(username, score)
    display_leaderboard()
    play_again()

start_2()

def play_again():
    """
    Asks user if they want to play again, gets 
    user input and validates their input.
    """
    try_again = True
    while try_again:
        try_again = input('Would you like to try quiz again? yes/no\n ')
        if try_again.lower() == 'yes':
            break
        elif try_again == 'no':
            print(f'[bold blue]You have chosen to end the game. \nBye :smile:')
            quit()
        else:
            print('[bold blue] Wrong input. Please input yes or no')
            try_again = True
    start_2()

def start():
    """
    Calls all functions.
    """
    score = 0
    get_welcome_message()
    get_ascii()
    username, score = start_trivia(score)
    get_result(username, score)
    update_leaderboard(username, score)
    display_leaderboard()
    play_again()


start()


def start_2():
    score = 0
    username = ''
    get_result(username, score)
    update_leaderboard(username, score)
    display_leaderboard()
    play_again()

start_2()