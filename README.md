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


