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
SHEET = GSPREAD_CLIENT.open('football_info')

def user_commands():
    """
    gives commands the user is able to input to receive different data sets
    """
    
    manu = SHEET.worksheet('man_utd').get_all_values()
    manc = SHEET.worksheet('man_city').get_all_values()
    chelsea = SHEET.worksheet('chelsea').get_all_values()
    liverpool = SHEET.worksheet('liverpool').get_all_values()
    goalkeepers = SHEET.worksheet('goalkeepers').get_all_values()

    options = ['man united, man city, liverpool, chelsea']    
    for i in range(len(options)):
        print(str(i+1) + ":", options[i])

    options_2 = ['goalkeepers, defenders, midfielders, forwards']
    for i in range(len(options_2)):
        print(str(i+2) + ":", options_2[i])
    
    options_3 = ['appearances, goals scored, clean sheets, age']
    for i in range(len(options_3)):
        print(str(i+3) + ":", options_3[i])

    value = input("Please enter a string:\n")
    print(f"You have entered {value}")


    if value == 'man united':
        print(manu)
    elif value == 'man city':
        print(manc)
    elif value == 'liverpool':
        print(liverpool)
    elif value == 'chelsea':
        print(chelsea)
    elif value == 'appearances':
        print(chelsea)
    elif value == 'goals scored':
        print(chelsea)
    elif value == 'clean sheets':
        print(chelsea)
    elif value == 'age':
        print(chelsea)
    else:
        print('Not an available option: Please enter correct option.')  

    return options  
        
print("Hi! Welcome to a football stats generator")
print("The available options are as follows")


def main():
    user_commands()
    #manu_options()
    #manc_options()
    

main()