# BMW TRIVIA

- This is a quiz about BMW.The quiz consists of 20 questions and 4 options each. It was inspired by my special interest in BMW cars. Bayerische Motoren Werke AG, commonly abbreviated to BMW, is a German multinational manufacturer of luxury vehicles and motorcycles headquartered in Munich, Bavaria, Germany. This quiz consists of some history about BMW which has been added after each question is answered. The history was added to provide more knowledge to any BMW lover who choose to play the quiz as the purpose of the whole quiz is to educate BMW fans.
- This quiz is targeted at car lovers who have special interest in BMW and want to know more of the company's history. 

# Table of Contents
- Colour Scheme
- Data structure

# Features
- Spreadsheet
- Acsii

## Testing

## Manual testing
- Input Validation
- Name Input
- Start game Input
- Answer Input
- Try again Input

## Validator testing
- Python
- Accessibility
- Unfixed bugs
- Technologies used

## Cloning and forking

### CLONING
- On (https://github.com), navigate to the greeen <> code button on the right side of the page.
- copy the URL for the repository.
- To clone the repository using HTTPS, under HTTPS copy the URL
- To clone the repository using an SSH key, Click SSH then copy the URL.
- To clone a repository using github cli, click github cli then copy the URL.
- Open Terminal
- Change the current working directory to the location where you want the cloned directory.
- Type 'git clone', and then pate the URL you copied earlier.
- Press enter to create a local clone.

### FORKING
- On (https://github.com), navigate to the repository.
- In the top-right corner of the page, click Fork.
- Under 'owner', select the dropdown menu and click an owner for forked repository.
- By default, forks are named the same as their upstream repositories. Optionally, to further distinguish your fork, in the 'Repository name' field,type a name.
- Optionally, in the 'Description' field, type a description of your fork.
- Optionally, select copy the default branch only.
- Click create fork.
## Deployment

## Credits

## Colour Scheme
- Some of the color of the text that comes up on the terminal has been changed to bold blue and bold white . The bold blue texts will be noticed when an answer is chosen. The bold blue texts have been used to highlight the comments which are the full answers to the question.
- Emojis have also been used in some cases where the user gets the answer right, a smile emoji has been used and when the wrong answer is chosen, A message saying the correct answer with a thumb_down emoji is printed to the screen.
- This color scheme was inspired by the BMW logo which is blue and white.
-The color scheme have been added by installing 'rich' from the terminal by inputting 'pip install rich' and we are able to access rich in our run.py by using 'from rich import print'.

## Data structure 
- The quiz questions and options have been put together using a LIST and a for loop was used to iterate over the list which contains the questions, options, corrects answers, incorrect answers and comments.

## Features

#### Google spreadsheet
- Google sheet has been added to this quiz to collect user name and score and sort the highest five in descending order and then finally print the leaderboard at the end of the quiz showing the Top 5.

<img width="1710" alt="Screenshot 2024-05-31 at 21 03 45" src="https://github.com/Oluwapelumi99/BMW_Trivia/assets/156908824/474d117c-3313-49a7-bb99-5552d372cf67">


#### Ascii

- Ascii of BMW logo was generated using https://www.ascii-art-generator.org been added to the quiz to display in the terminal after the welcome message has been printed to the screen to give a more detailed idea of what the quiz is about. 
<img width="750" alt="Screenshot 2024-05-31 at 21 09 27" src="https://github.com/Oluwapelumi99/BMW_Trivia/assets/156908824/5f47ff10-f24b-4461-815c-1db7a9fd8b51">

## Testing


## Manual testing
- I have added the input function and I have put measures in place to make sure the right details are inputed.
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


###### Answer input
- If the correct option is chosen from A-D, this is printed on the terminal.

<img width="750" alt="Screenshot 2024-05-30 at 00 11 44" src="https://github.com/Oluwapelumi99/BMW_Trivia/assets/156908824/7df2996a-cb10-4ba5-bbcd-4acd39395d97">

- if the incorrect option is chosen then this is printed to the terminal.

<img width="756" alt="Screenshot 2024-05-30 at 00 12 38" src="https://github.com/Oluwapelumi99/BMW_Trivia/assets/156908824/5d3fd2f2-3935-4fc1-badb-91945bfdcf75">

- However, if something else is printed to the terminal asides the correct and incorrect answer such as space, null, special characters,etc this is the ouput.

<img width="751" alt="Screenshot 2024-05-30 at 00 13 32" src="https://github.com/Oluwapelumi99/BMW_Trivia/assets/156908824/48dbc7c7-6dc7-4b73-90f0-29f344043b7b">


###### Try again input
- I have added the function make user decide if they want to play again, and the inputs are yes or no anything else will print incorrect inpput and will ask them to try again. The prompt keeps asking until they input the accepted detals.

- If yes is printed into the terminal to try the quiz agin, the quiz starts again.

<img width="783" alt="Screenshot 2024-05-30 at 00 23 41" src="https://github.com/Oluwapelumi99/BMW_Trivia/assets/156908824/bf8209fd-79d9-48ae-ae7c-bcbf02478e80">

- If no is printed into the terminal, the quiz ends and 'Sad to see you go' is printed to the terminal.

<img width="750" alt="Screenshot 2024-05-30 at 00 40 00" src="https://github.com/Oluwapelumi99/BMW_Trivia/assets/156908824/b34d67d2-2139-4f8f-b550-bb3a51efb6c3">

- However, if anything else asides yes or no is printed to the terminal, the input is not accepted and user is asked to input a valid response.

<img width="775" alt="Screenshot 2024-05-30 at 00 33 18" src="https://github.com/Oluwapelumi99/BMW_Trivia/assets/156908824/902c5c2c-2af7-4e73-866e-00e8ebcdbfc2">


## Validator Testing
#### Python
- I tested the python code with https://pep8ci.herokuapp.com/, which had the errors below.

<img width="1587" alt="Screenshot 2024-05-29 at 21 43 27" src="https://github.com/Oluwapelumi99/BMW_Trivia/assets/156908824/0eeaa24c-f87d-4e30-9653-73d3e19145a7">

- Errors have been fixed,excepts the blank spaces aeound the ascii area and this cannot be fixed as it will distort the ascii layout. Here is a screenshot.

<img width="1705" alt="Screenshot 2024-05-31 at 22 29 26" src="https://github.com/Oluwapelumi99/BMW_Trivia/assets/156908824/47471b5d-fea6-4b38-8e85-ba2e52117670">


#### Accessibility
- The output has been made accessible by picking colors that provide a good contrast against the terminal using https://www.rich.readthedocs.io

#### Unfixed bugs
- There are no unfixed bugs.

#### Technologies used
- https://www.gitpod.io/
- https://code.visualstudio.com
- Google spreadsheet was used to calculate and display the highest score to the terminal after they have finished answering all questions.
- https://www.heroku.com
- https://pep8ci.herokuapp.com/

## Cloning and forking.


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
- The https://www.rich.readthedocs.io app was used to add the color and emojis to the terminal.
- The template to run this code was created by code Institute.
- Ascii was generated from https://www.ascii-art-generator.org

