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

#manu = SHEET.worksheet('man_utd')
#manc = SHEET.worksheet('man_city')
#chelsea = SHEET.worksheet('chelsea')
#livepool = SHEET.worksheet('liverpool')

def user_commands():
    """
    gives commands the user is able to input to receive different data sets
    """
    print("Hi! Welcome to a football stats generator")
    print("The available options are as follows")
    
    manu = SHEET.worksheet('man_utd')
    manc = SHEET.worksheet('man_city')
    chelsea = SHEET.worksheet('chelsea')
    livepool = SHEET.worksheet('liverpool')

    options = ['man united, man city, liverpool, chelsea']
        
    for i in range(len(options)):
        print(str(i+1) + ":", options[i])


    value = input("Please enter a string:\n")
    print(f"You have entered {value}")
        
        

user_commands()

#def input_commands ()
   # """
   # Sets up the different string options that can be used as commands.
    #Tells the user whether what they inputted in a valid command and if not,
    #returns a message telling them it is not valid
    #"""