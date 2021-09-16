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

def user_commands():
    """
    gives commands the user is able to input to receive different data sets
    """

    options = 'man united, man city, liverpool, chelsea'   
    print(f"1: {options}")

    options_2 = 'goalkeepers, defenders, midfielders, forwards'
    print(f"2: {options_2}")

    options_3 = 'appearances, goals scored, clean sheets, age'
    print(f"3: {options_3}")

    value = input("Please enter a string:\n")
    print(f"You have entered {value}\n")

    if value in ['man united', 'man city', 'liverpool', 'chelsea']:
        print(tabulate(data[value]))
    elif value not in ['man united', 'man city', 'liverpool', 'chelsea']:
        print("You have not entered a correct option!")
    else:
        exit()


    options = 'Back, Top Scorers, Appearances'
    print(f"Next Options:")

print("Hi! Welcome to a football stats generator")
print("The available options are as follows:")

def user_commands_2():

    options_1 = 'goalkeepers, defenders, midfielders, forwards'
    print(f"1: {options_1}")

    options_2 = 'appearances, goals scored, clean sheets, age'
    print(f"2: {options_2}")

    value = input("Please enter a string:\n")
    print(f"You have entered {value}\n")


def main():
    """
    Run all program functions
    """
    user_commands()
    user_commands_2()

main()
