import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('football_info')

data = {
    "man united": SHEET.worksheet("man_utd").get_all_values(),
    "man city": SHEET.worksheet("man_city").get_all_values(),
    "chelsea": SHEET.worksheet('chelsea').get_all_values(),
    "liverpool": SHEET.worksheet('liverpool').get_all_values()
}

options = ['return', 'age', 'goals scored', 'apperances', 'clean sheets', 'goalkeepers', 'defenders', 'midfielders', 'forwards', 'home']

def user_commands():
    """
    gives commands the user is able to input to receive different data sets
    """

    options = 'man united, man city, liverpool, chelsea'   
    print(f"1: {options}")

    team_name = input("Please enter a string:\n")
    print(f"You have entered {team_name}\n")

    while team_name not in data:
        print("You entered a wrong option, Please enter a correct option")
        print(f"1: {options}")
        team_name = input()

    print(tabulate(data[team_name]))
    

def user_commands_2():

    options_1 = 'goalkeepers, defenders, midfielders, forwards, home'
    print(f"1: {options_1}")

    position = input("Please enter a string:\n")
    print(f"You have entered {position}\n")

    while position not in (options):
        print("You entered a wrong option, Please enter a correct option")
        print(f"1: {options_1}")
        position = input()

    if position == 'home':
        main()

    res = [i for i in data['man united'] if "Forward" in i]
    
    print(tabulate(res))

print("Hi! Welcome to a football stats generator")
print("The available options are as follows:")

def top_scorer():
    """
    Takes the goal scoring data from the spreadsheet and present it's to the user
    with the list ordered by the most goals scored per team down to the least goals scored
    """
    options = 'man united, man city, liverpool, chelsea'   
    print(f"1: {options}")
    team_name = input("Please enter team name to see top scorers for that team:\n")
    print(f"you have entered: {team_name}")

    res = [i for i in data['chelsea'] if "Goals Scored" in i]
    res.col()
    print(tabulate(res))

    

def main():
    """
    Run all program functions
    """
    user_commands()
    user_commands_2()
    top_scorer()

main()
