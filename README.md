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

## Creating a google spreadsheet

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

<img width="1710" alt="Screenshot 2024-06-01 at 01 54 56" src="https://github.com/Oluwapelumi99/BMW_Trivia/assets/156908824/819a6d59-e043-4a12-a12a-e472e5e9e5c4">

- Leaderboard top 5 is then printed to the terminal after the game ends from the values gottten from the scoreboard spread sheet.

<img width="761" alt="Screenshot 2024-06-01 at 02 18 48" src="https://github.com/Oluwapelumi99/BMW_Trivia/assets/156908824/f9ad5c93-8f15-45d7-ad9e-a4bee2c10a31">


#### Ascii

- Ascii of BMW logo was generated using https://www.ascii-art-generator.org been added to the quiz to display in the terminal after the welcome message has been printed to the screen to give a more detailed idea of what the quiz is about. 
<img width="750" alt="Screenshot 2024-05-31 at 21 09 27" src="https://github.com/Oluwapelumi99/BMW_Trivia/assets/156908824/5f47ff10-f24b-4461-815c-1db7a9fd8b51">

## Testing


## Manual testing
- I have added the input function and I have put measures in place to make sure the right details are inputed.
#### Input Validation

###### Start game Input
Input validation has also been used with while loops to check if they want to start the quiz and keeps asking if a wrong input is inputed.
- This is a screenshot of the prompt that asks users if they want to start the quiz.

<img width="750" alt="Screenshot 2024-06-01 at 02 12 45" src="https://github.com/Oluwapelumi99/BMW_Trivia/assets/156908824/c42e7655-36c4-4073-83c4-5e8cbd4167ad">

- This is what happens when yes is inputed after user has been asked if they want to start the game.
It can be seen that the quiz starts and prints the first question of the quiz to the terminal.

<img width="756" alt="Screenshot 2024-06-01 at 02 13 21" src="https://github.com/Oluwapelumi99/BMW_Trivia/assets/156908824/c93978a8-e72b-48f3-b889-362d189e6aa3">

- A screenshot of what happens when no is inputed to the terminal. It can be seen that the quiz ends.

<img width="762" alt="Screenshot 2024-06-01 at 02 14 05" src="https://github.com/Oluwapelumi99/BMW_Trivia/assets/156908824/0d539a09-9437-49dd-a674-4a8c1ce67765">

- This is what happens when nothing was inputed to the terminal.
<img width="755" alt="Screenshot 2024-06-01 at 02 15 44" src="https://github.com/Oluwapelumi99/BMW_Trivia/assets/156908824/dcbfde2b-2b81-4ed8-8436-b655e8ad1bdf">

- This is what happens when anything asides yes or no is inputed onto the terminal.
<img width="751" alt="Screenshot 2024-06-01 at 02 15 13" src="https://github.com/Oluwapelumi99/BMW_Trivia/assets/156908824/acee0500-f199-48be-988d-3e60ef6dcc4a">

###### Name Input
- I have added some input validation using the if statement and the while loop. User has been requested to input their names and their input will have to be validated.

- This is a picture of the prompt for users to input their names and which also shows the accepted inputs

<img width="751" alt="Screenshot 2024-05-27 at 22 29 51" src="https://github.com/Oluwapelumi99/Rock--paper-scissors/assets/156908824/854eb771-fb04-4f88-a88e-feac6cea40d7">

- This is a picture of what is printed after user inputs any special characters or numbers, which then prompts them again to input the correct characters because a while loop has been used.

<img width="737" alt="Screenshot 2024-05-27 at 21 34 36" src="https://github.com/Oluwapelumi99/Rock--paper-scissors/assets/156908824/ca7adab6-5996-479e-a3e1-10c916f723f7">

- This is a screenshot of what happens when a user inputs more than 20 characters

<img width="750" alt="Screenshot 2024-05-27 at 22 42 24" src="https://github.com/Oluwapelumi99/Rock--paper-scissors/assets/156908824/f9810060-b4b3-42d6-a7b5-59eff330b760">

- This is a screenshot of what happens when the user inputs a name less than 3 as 3 is the least number of characters that can be entered.

<img width="745" alt="Screenshot 2024-05-27 at 22 45 12" src="https://github.com/Oluwapelumi99/Rock--paper-scissors/assets/156908824/9e363925-2e28-4a70-852a-ee8f544ed2de">

- Finally, this is what happens when the user inputs the accepted details. It can be seen that the input is accepted and the code moves on to  the next code.

<img width="752" alt="Screenshot 2024-06-01 at 02 32 06" src="https://github.com/Oluwapelumi99/BMW_Trivia/assets/156908824/ef691e67-74b1-4795-b62b-18d892bf6e44">


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

<img width="764" alt="Screenshot 2024-06-01 at 02 20 57" src="https://github.com/Oluwapelumi99/BMW_Trivia/assets/156908824/c151b9a6-0be2-4e3e-a5f7-9681af29cbb1">


- If no is printed into the terminal, the quiz ends and 'Sad to see you go' is printed to the terminal.

<img width="745" alt="Screenshot 2024-06-01 at 02 22 05" src="https://github.com/Oluwapelumi99/BMW_Trivia/assets/156908824/2a9524aa-8ae2-449f-9e42-16d5ccb81cff">

- However, if anything else asides yes or no is printed to the terminal, the input is not accepted and user is asked to input a valid response.

<img width="755" alt="Screenshot 2024-06-01 at 02 20 23" src="https://github.com/Oluwapelumi99/BMW_Trivia/assets/156908824/a16109f5-25b8-4bc9-9d16-dc11c8331e9c">


## Validator Testing
#### Python
- I tested the python code with https://pep8ci.herokuapp.com/, which had the errors below.

<img width="1587" alt="Screenshot 2024-05-29 at 21 43 27" src="https://github.com/Oluwapelumi99/BMW_Trivia/assets/156908824/0eeaa24c-f87d-4e30-9653-73d3e19145a7">

- Errors have been fixed,excepts the blank spaces from lines 32-51 around the ascii area and this cannot be fixed as it will distort the ascii layout. Here is a screenshot.

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

### Creating a google spreadsheet.
- Create a google account first and make sure to use a personal google account.
- Then set up your API - Application programme interface. This is so that python project can access our google sheet and get data from the sheet.
- In order to do this, go to (https://console.cloud.google.com/). Then the first thing is to create a new project and then give the project a name, then click create.
- Then click select project on the new project that pops up on the right side of the screen.
- From the side menu, then select API AND SERVICES and then select library.
- In order to access the spreadsheet, we need to enable google drive api and google sheets api.
- Search for the google drive api and google sheets api in the library then enable both.
- When the google drive api is enabled, on the next page click on create credentials
- Next, on credential type, click on google drive api
- What will you be processing? , application data
- For the "Are you planning to use this API with Compute Engine, Kubernetes Engine, App Engine, or Cloud Functions?" question, select No, I'm not using them
- Click Next
- On your credentials:
- Enter a service account name, name can be the name of your project 
- In the Role Dropdown box choose Basic > Editor then press Continue
- On the next page, click on the Service Account that has been created
- On the next page, click on the Keys tab
- Click on the Add Key dropdown and select Create New Key
- Select JSON and then click Create. This will trigger the json file with your API credentials in it to download to your machine.
- Search for the file in your computer
- After the google sheets api has been enabled, you do not need to create any credentials for that.
- Copy and paste the json file you downloaded earlier to your workspace.
- Open the json file and copy the client email without the code, go back to the spreadsheet and click the share button on the right top corner. Paste in the client's email, make sure the editor is selected and untick notify people and then click share.
- Rename the json file to 'creds.json' and add it to .gitignore so it cannot be tracked by git and should be kept secret.
- In order to use google sheet api, add 2 more dependencies to your project.
1. google oauth
2. gspread
- install these by using the command 'pip3 install gspread google-auth' in the terminal
- After the packages have been installed, access them by using the following commands at the top of the run.py file
- 'import gspread'
- 'from google.oauth2.services_account import Credentials'
- SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
- 'CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('bmw-trivia)'
- name in the sheet variable must be identical to the name of the googlesheet. As my sheet is named bmw_trivia, the sheet variable also contains bmw-trivia
- Now your sheet is connected to your project

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

