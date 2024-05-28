![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **March 14, 2023**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!

# BMW TRIVIA

- This is a quiz about BMW.The quiz consists of 20 questions and 4 options each. It was inspired by my special interest in BMW cars. Bayerische Motoren Werke AG, commonly abbreviated to BMW, is a German multinational manufacturer of luxury vehicles and motorcycles headquartered in Munich, Bavaria, Germany.This quiz consists of some history about BMW which has been added after each question have been answered.

# Table of Contents
- Colour Scheme
- Data structure

# Features
- Spreadsheet

## Testing

## Manual testing
- Input Validation
- Name Input
- Start game Input
- Answer Input
- Try again Input

## Bugs

- Solved bugs

## Validator testing
- Python
- Accessibility
- Unfixed bugs
- Technologies used

## Deployment

## Credits
- 


## Colour Scheme
- Some of the color of the text that comes up on the terminal has been changed to bold blue and bold white . The bold blue texts will be noticed when an aswer is chosen. The bold blue texts have been used to highlight the comments which are the full answers to the question.
- Emojis have also been used in some cases where the user gets the answer right, a smile emoji has been used and when the wrong answer is chosen, A message saying the correct answer with a thumb_down emoji is preinted to the screen.
- This color skim was inspired by the BMW logo which is blue and white.
-The color scheme have been added by installing 'rich' from the terminal by inputting 'pip install rich' and we are able to access rich in our run.py by using 'from rich import rich'.

## Data structure 
- The quiz questions and options have been put together using a LIST and a for loop was used to iterate over the list which contains the questions, options, corrects answers, incorrect answers and comments.

## Testing
- I have added some 

## Manual testing
#### Input Validation
###### Name Input
- I have added some input validation using the if statement and the while loop. User has been requested to input their names and their input will have to be validated.

- This is a picture of the prompt for users to input their names and which also shows the accepted inputs
<img width="751" alt="Screenshot 2024-05-27 at 22 29 51" src="https://github.com/Oluwapelumi99/Rock--paper-scissors/assets/156908824/854eb771-fb04-4f88-a88e-feac6cea40d7">

- This is a picture of what is printed after user inputs any special characters, which then prompts them again to input the correct characters because a while loop has been used.
<img width="737" alt="Screenshot 2024-05-27 at 21 34 36" src="https://github.com/Oluwapelumi99/Rock--paper-scissors/assets/156908824/ca7adab6-5996-479e-a3e1-10c916f723f7">

- This is a screenshot of what happens when a user inputs more than 20 characters
<img width="750" alt="Screenshot 2024-05-27 at 22 42 24" src="https://github.com/Oluwapelumi99/Rock--paper-scissors/assets/156908824/f9810060-b4b3-42d6-a7b5-59eff330b760">

- This is a screenshot of what happens when the user inputs a name less than 3 as 3 is the least number of characters that can be entered.
<img width="745" alt="Screenshot 2024-05-27 at 22 45 12" src="https://github.com/Oluwapelumi99/Rock--paper-scissors/assets/156908824/9e363925-2e28-4a70-852a-ee8f544ed2de">

- Finally, this is what happens when the user inputs the accepted details. It can be seen that the input is accepted and the code moves on to  the next code.
<img width="741" alt="Screenshot 2024-05-27 at 22 48 50" src="https://github.com/Oluwapelumi99/Rock--paper-scissors/assets/156908824/099b61b1-0039-4272-9b9a-599fdbb0e657">


###### Start game Input
Input validation has also been used with while loops to check if they want to start the quiz and keeps asking if a wrong input is inputed.
- This is a screenshot of the prompt that askes users if they want to start the quiz.
<img width="741" alt="Screenshot 2024-05-27 at 22 48 50" src="https://github.com/Oluwapelumi99/Rock--paper-scissors/assets/156908824/099b61b1-0039-4272-9b9a-599fdbb0e657">

- This is what happens when yes is inputed after user has been asked if they want to start the game.
It can be seen that the quiz starts and prints the first question of the quiz to the terminal.
<img width="752" alt="Screenshot 2024-05-27 at 22 58 29" src="https://github.com/Oluwapelumi99/Rock--paper-scissors/assets/156908824/70dc899a-f6be-4560-86a0-721363cc1eeb">

- A screenshot of what happens when no is inputed to the terminal. It can be seen that the quiz ends.
<img width="747" alt="Screenshot 2024-05-29 at 00 03 15" src="https://github.com/Oluwapelumi99/BMW_Trivia/assets/156908824/
d3716040-0e89-4a99-a8ad-a129b079c691">


- This is what happens when nothing was inputed to the terminal.
<img width="753" alt="Screenshot 2024-05-27 at 23 07 16" src="https://github.com/Oluwapelumi99/Rock--paper-scissors/assets/156908824/10a06842-f6e2-4718-b886-417e8cde8df5">

- This is what happens when anything asides yes or no is inputed onto the terminal.
<img width="749" alt="Screenshot 2024-05-27 at 23 08 59" src="https://github.com/Oluwapelumi99/Rock--paper-scissors/assets/156908824/9a5719a3-5f8a-42b2-b061-2da441ecc552">



## Validator Testing

#### Python
#### Accessibility
#### Unfixed bugs
#### Technologies used


## Deployment
- This project has been deployed to https://www.heroku.com because heroku is better with backend languages.
- The first step is to create an account on heroku and fill out the form provided.
- After submitting the form, an email will be sent to your email account to set password, then you can deploy your project.
- From the Heroku Dashboard, Click on the CREATE NEW APP. Then you name your app. I named mine BMW-Trivia and you select YOUR REGION, then click on 'CREATE APP'.
- Then  click on the SETTINGS tab on the next page.
- Then  create a CONFIG VAR which will contain credentials from the creds.Json file that was added to .gitignore because I wanted to keep it secret as I did not want it to be deployed on github. However, it has to be deployed to Heroku. This is so that Heroku can access the spreadsheet and connect to my APIs. You can skip this step if you do not have any cred.json file.
- After clicking on CONFIG VAR, Input "CREDS" in the space for 'KEYS' and they contents of the creds.json file is added to the 'VALUE' space.
- Then create another CONFIG VAR. The key is 'PORT' and the value is '8000'
- Then click 'ADD BUILDPACK' which is just below the space to add the config vars to help provide further dependencies needed outside of the ones in the requirement.txt file. The buildpacks are:
1. `heroku/python`
2. `heroku/nodejs`,
    these should be added in this order.
- Then move to the DEPLOY section on the heroku dashboard.
- Here choose to deploy from 'GITHUB' and confirm that you want to connect to github.
- Then search for your Github repository by typing in the name of the project. Mine is BMW_Trivia, then click search.
- Click 'CONNECT' to link up Heroku app to github repository code.
- Then scroll down and choose how you want to deploy, whether 'MANUALLY' by clicking the 'DEPLOY BRANCH' option or 'AUTOMATICALLY' by clicking the 'ENABLE AUTOMATIC DEPLOYS'. 
- After app has been succesfully deployed, a message comes up and there is a button called 'VIEW' which takes you to the terminal to run your code.
## Credits

