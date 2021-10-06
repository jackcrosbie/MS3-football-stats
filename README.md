# Football Stats Generator

![image](https://user-images.githubusercontent.com/82109134/136013574-1346778b-ec4a-4780-ba92-fa79e4014566.png)

Live application can be found here: https://ms3-football-stats.herokuapp.com/

This is a command-line-interface application designed to pull statistical information on various premier league football teams.
The information can be sorted using a number of different options. This project has been designed for educational purposes and uses the Code Institutes mock terminal to run.

## UX

To begin planning this project I started first with UX, designing the logic of the programme based upon the user stories. As this is a command-line application there is no design featured as HTML & CSS have not been used and the programme runs off a generic code institute mock terminal. Due to the lack of design I concentrated on making the text as neat, tidy and appropriately spaced as possible. This meant it was all clear and easy to read.

![image](https://user-images.githubusercontent.com/82109134/136013623-8c382f82-96ea-4ad5-af8c-039632b10c55.png)

### Strategy

User Stories:
- As a user I want to view statistics for each premier league football team
- As a user I want to be able to break down the statistics into various categories
- As a user I want the option to go back to the start of the program while using it
- As a user I want to be able to compare statistics across different teams
- As a user I want to the data presented in a clear easy to read table

### Structure

## Features

### Players List
The first option presented to you when using this program is to view the entire player list of one of the teams listed on the program.
The players are ordered by position and you can see relevant information for each player. Attached is a screenshot where I inputted 'man united' and got the information on each player for their team:
![image](https://user-images.githubusercontent.com/82109134/136015443-d2abafc4-1ba0-4cd1-8580-3ee35b2eea2a.png)

### Players Position List
After this you are then presented with another string of choices. These options are based on position and let you filter players by position from the team you have previously picked. For the example below I picked the midfielders of man united:
![image](https://user-images.githubusercontent.com/82109134/136016076-0c787230-2379-4137-994c-161a7a203007.png)

### Top Scorers
The next set of options that appear enable you to filter the information via the 'goals scored' column in the google spreadsheet. Again you picked one of the various team names and you will be presented with a list of the top goal scorers ordered in most goals scored to least.
The example below is the top goal scorers for liverpool:

![image](https://user-images.githubusercontent.com/82109134/136016567-c746995c-155e-4fe3-b954-6739b4869217.png)

### Appearances
This option enabled you to filter the information by players who have made over 100 appearances for their club. This option will only show players who have made 100+ appearances for their team. The below example is players who have made over 100 appearances for man city

![image](https://user-images.githubusercontent.com/82109134/136018334-d0629f1c-7006-40c5-9301-99750d8b24b0.png)


### Players Ages
By inputting a team in this option you get the full team list back to you organised in an ordered list with the eldest player at the top of the list and the youngest player at the bottom. The example below is the players ages for the team chelsea:

![image](https://user-images.githubusercontent.com/82109134/136018669-722bbac1-255b-4e1c-80fd-2efeeac536bd.png)

### Home Function
After the first set of options are inputted into the terminal, from then on, you get a home option which when entered will bring you to the start of the program again.
Upon reaching the end of all the options the terminal asks you 'would you like to go back to the start?'. If you answer 'yes' to this it will bring you back to the start and you can enter different sets of options to receive different data to what you previously received. If you say 'no' the program terminates.

![image](https://user-images.githubusercontent.com/82109134/136019119-ad3c98d0-492e-4ebd-82c5-928e0031983b.png)

Home option at the list of the list of strings/options:

![image](https://user-images.githubusercontent.com/82109134/136019271-463df243-20fa-4de4-8fff-887edd933534.png)

![image](https://user-images.githubusercontent.com/82109134/136019326-09cdd0dd-e8ce-4271-a8cb-1be6710dec85.png)

## Technologies Used

The following are a list of technologies I used to enable my project to work effectively

- Python:
  Python is the core language used and the basis of this entire project. All the code used was written using Python
  In addition to Python the following modules were also used:
    - Gspread: Used to access all the data stored on googlesheets.
    - Google Auth: Enabled the application to interact with googlesheets.
    - Tabulate: Used to present all the data in table form making it clearer and easier to read.
    - PD8: Used to validate, format and debug my Python code

- Github:
  Used Github to store the code and push it to the Heroku Terminal
  
- Gitpod:
  Used as the development envoirnment for the project
  
- Heroku:
  Used to deploy the project
  
 - Google Sheets:
   Used to store all the data for the project. The data is all drawn from the google sheet
   
- Pep8:
  Used to test my code to reveal any errors in my code format and written code
  
## Testing

*'As a user I want to view statistics for each premier league football team'*  
The first option when you run the program is to see the statistical breakdown of the teams listed

![image](https://user-images.githubusercontent.com/82109134/136047330-952b8105-5330-4522-bb5e-6cd88c05884c.png)

Above is an example where I entered 'man city'


*'As a user I want to be able to break down the statistics into various categories'*  
This is done throughout the program. Once you pull the inital data from the first list of options you can break that down further to show players based on a position you select

![image](https://user-images.githubusercontent.com/82109134/136049054-b6b4a430-361f-4728-9a09-cd998c4d1b14.png)  

Above example is 'man city' players filtered by their position as a 'forward'

![image](https://user-images.githubusercontent.com/82109134/136049429-37c333a7-6ae2-4d40-8ce6-a0e4a97e35c6.png)  

The image above now shows the option to see a teams top goal scorers

![image](https://user-images.githubusercontent.com/82109134/136050109-b37e5453-943c-45f9-8064-afd458075c96.png)  

Above image shows the option to see players who have made over 100 appearances for the team selected

![image](https://user-images.githubusercontent.com/82109134/136050248-7914f4c6-adea-45bd-aada-8b4d41f46be9.png)  

Example above shows the option to break down the selected team in order from age (oldest to youngest)


*'As a user I want the option to go back to the start of the program while using it'*  
After the inital list of options I added a home option which will bring you back to the start of the program when entered.
As well as this I have entered an option to return to the start once the program has reached the end (shown below)

![image](https://user-images.githubusercontent.com/82109134/136050700-876b6739-887d-4cd9-adae-8bb831f5ac0b.png)

Home option in most of the option lists:  
![image](https://user-images.githubusercontent.com/82109134/136050844-8c869f3f-3f4c-42d8-b527-6d684cc62365.png)   
![image](https://user-images.githubusercontent.com/82109134/136052397-d29762e2-f1ad-4531-a805-530ea65e7d2d.png)  
![image](https://user-images.githubusercontent.com/82109134/136052635-d2fe5c4f-7ec1-4de3-ac40-91eac5e2914e.png)  


*'As a user I want to be able to compare statistics across different teams'*



*'As a user I want to the data presented in a clear easy to read table'*
Using tabulate I was able to get my data presented in a clear uniformed manner.  
This made the information easy to read and compare. Examples of the tables are below:  

![image](https://user-images.githubusercontent.com/82109134/136053043-1ba93d2b-7e98-423e-a390-4736e8217fc7.png)  

![image](https://user-images.githubusercontent.com/82109134/136053206-e4023040-2c30-404f-84ad-8172561ec074.png)  

![image](https://user-images.githubusercontent.com/82109134/136053276-33b2687d-9f83-4bbd-80c6-77336a2ec0d3.png)  


## Bugs and Fixes

- Gspread and Tabulate Errors:
  Upong the inital deployment of my project I got 'ModuleNotFoundError: No module named gspread' and after that  
  i got 'ModuleNotFoundError: No module named tabulate'
  
  These occured due to errors in my requirements.txt file.  
  After doing some reading online I found the 'pip3 freeze > requirements.txt' command which put the proper information in my requirements.txt file and sorted the above
  stated issue.
  
 - Deployment Error:
   During the process of fixing the gspread and tabulate errors I must've accidentally deleted my package.json file which meant the subsequent builds failed. To fix this I  
   went back through build histoy, found the last successful build and when I compared this to the failing builds I saw the package.json file had gone missing. Copied the  
   information from the file in the successful build to my current directory and It enabled the builds to build successfully from there on.
   
  - PEP8 Python Validator:
    Upon completion of writing my code. I ran it through the PEP8 online validator. This pointed out errors in my syntax and whitespace after lines of code in some instances.  
    I tidied all this up and as a result my code is running through the validator with zero errors.
    
![image](https://user-images.githubusercontent.com/82109134/136267008-77ab1458-a9f2-48a3-91bf-1c4334d329ba.png)


## Deployment

The master branch of this repository has been used for the deployed version of this application.

Using Github & Gitpod
To deploy my command-line interface application, I had to use the Code Institute Python Essentials Template, as this enables the application to be properly viewed on Heroku using a mock terminal.

- Click the Use This Template button.  
-  Add a repository name and brief description.
-  Click the Create Repository from Template to create your repository.
-  To create a Gitpod workspace you then need to click Gitpod, this can take a few minutes.
-  When you want to work on the project it is best to open the workspace from Gitpod (rather than Github) as this will open your previous workspace rather than creating a new one. You should pin the workspace so that it isn't deleted.
-  Committing your work should be done often and should have clear/explanatory messages, use the following commands to make your commits:
   -  git add .: adds all modified files to a staging area
   -  git commit -m "A message explaining your commit": commits all changes to a local repository.
   -  git push: pushes all your committed changes to your Github repository.

### Creating an Application with Heroku

I followed the below steps using the Code Institute tutorial:

- The following command in the Gitpod CLI will create the relevant files needed for Heroku to install your project dependencies pip3 freeze --local > requirements.txt. Please note this file should be added to a .gitignore file to prevent the file from being committed.
1. Go to Heroku.com and log in; if you do not already have an account then you will need to create one.
2. Click the New dropdown and select Create New App.
3. Enter a name for your new project, all Heroku apps need to have a unique name, you will be prompted if you need to change it.
4. Select the region you are working in.

Heroku Settings You will need to set your Environment Variables - this is a key step to ensuring your application is deployed properly.

- In the Settings tab, click on Reveal Config Vars and set the following variables:
  - If using credentials you will need to add the credentials as a variable, the key is the name 'CREDS' and the value is the contents of your creds JSON
  - Add key: PORT & value 8000
- Buildpacks are also required for proper deployment, simply click Add buildpack and search for the ones that you require.
  - For this project, I needed to add Python and Node.js, in this order.

Heroku Deployment In the Deploy tab:

- Connect your Heroku account to your Github Repository following these steps:
  - Click on the Deploy tab and choose Github-Connect to Github.
  - Enter the GitHub repository name and click on Search.
  - Choose the correct repository for your application and click on Connect.
- You can then choose to deploy the project manually or automatically, automatic deployment will generate a new application every time you push a change to Github, whereas manual deployment requires you to push the Deploy Branch button whenever you want a change made.
- Once you have chosen your deployment method and have clicked Deploy Branch your application will be built and you should see the below View button, click this to open your application:

![image](https://user-images.githubusercontent.com/82109134/136269827-83c7590b-5b04-4ec0-887f-df7463a22ecc.png)


## Credits

All the code used is entirely original and written by me. However I drew on resources such as Stack Overflow to fix various bugs and issues i encountered.  
I also used the website https://pypi.org/project/tabulate/ to help me use tabulate for my project.

## Acknowledgements 

As always I want to thank my mentor Aaron Sinnott for his continued advice, support and feedback throughout this project.
I would also like to thank my peer Daisy Gunn for her support, advice and general encouragement.







