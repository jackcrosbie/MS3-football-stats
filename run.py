import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate
import pyinputplus as pyip

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

team_name = ""
position = ""
top_stats = ""

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
    return team_name 

def user_commands_2(team_name):

    options_1 = 'goalkeeper, defender, midfielder,\nforward, home'
    print(f"1: {options_1}")

    position = input("\nPlease enter a string:\n")
    print(f"You have entered {position}\n")

    while position not in (options_1):
        print("\nYou entered a wrong option, Please enter a correct option")
        print(f"1: {options_1}")
        position = input()

    if position == 'home':
        print("Hi! Welcome to a Football Stats Generator")
        print("The available options are as follows:")
        main()   

    res = [i for i in data[team_name] if position.capitalize() in i]
    print(tabulate(res))

print("Hi! Welcome to a football stats generator")
print("The available options are as follows:")

def top_scorers():
    """
    Takes the goal scoring data from the spreadsheet and present it's to the user
    with the list ordered by the most goals scored per team to the least.
    """
    goal_scorers = []

    options = 'man united, man city, liverpool, chelsea, home'   
    print(f"1: {options}")
    team_name = input("\nPlease enter team name to see top scorers for that team:\n")
    print(f"you have entered: {team_name}")

    if team_name == 'home':
        print("Hi! Welcome to a football stats generator")
        print("The available options are as follows:")
        main() 

    while team_name not in (options):
        print("\nYou entered a wrong option, Please enter a correct option")
        print(f"1: {options}")
        team_name = input()

    for row in data[team_name]:
        if "Goals Scored" in row:
            continue
        if int(row[3]) > 0:
            goal_scorers.append(row)


    goal_scorers.sort(key=lambda x: int(x[3]))
    goal_scorers.reverse()
    goal_scorers[:4]
    print(tabulate(goal_scorers))

def appearances():
    """
    function to compare players appearances and return a value if their appearances after over 100 for their team.
    It then prints the results to the terminal/console
    """
    player_apps = []

    options = 'man united, man city, liverpool, chelsea, home'   
    print(f"1: {options}")
    team_name = input("\nPlease enter team name to see players with over 100 appearances for that team:\n")
    print(f"you have entered: {team_name}")

    if team_name == 'home':
        print("Hi! Welcome to a football stats generator")
        print("The available options are as follows:")
        main()

    while team_name not in (options):
        print("\nYou entered a wrong option, Please enter a correct option")
        print(f"1: {options}")
        team_name = input()

    for row in data[team_name]:
        if "Appearances" in row:
            continue
        if int(row[2]) > 100:
            player_apps.append(row)


    player_apps.sort(key=lambda x: int(x[2]))
    player_apps.reverse()
    player_apps[:4]
    print(tabulate(player_apps))

def ages():
    """
    This function organising players within a team by their ages.
    Oldest at the top to the youngest at the bottom
    """
    player_ages = []

    options = 'man united, man city, liverpool, chelsea, home'   
    print(f"1: {options}")
    team_name = input("\nPlease enter team name to see players ages in an ordered list:\n")
    print(f"you have entered: {team_name}")

    if team_name == 'home':
        print("Hi! Welcome to a football stats generator")
        print("The available options are as follows:")
        main()

    while team_name not in (options):
        print("\nYou entered a wrong option, Please enter a correct option")
        print(f"1: {options}")
        team_name = input()

    for row in data[team_name]:
        if "Age" in row:
            continue
        if int(row[5]) > 0:
            player_ages.append(row)

    player_ages.sort(key=lambda x: int(x[5]))
    player_ages.reverse()
    player_ages[:4]
    print(tabulate(player_ages))


#def overall_top_stats():
#
#
#    options = 'most goals, most appearances, most clean sheets, home'
#    print(f"1: {options}")
#    top_stats = input("Please enter an option to see the overall top players:\n")
#    print(f"you have entered: {top_stats}")

#    if top_stats == 'home':
#        print("Hi! Welcome to a football stats generator")
#        print("The available options are as follows:")
#        main()

#    while top_stats not in options:
#        print("You entered a wrong option, Please enter a correct option")
#        print(f"1: {options}")
#        top_stats = input()
    
#    for value in data.keys():
#        for row in data[value]:
#            if f"{top_stats}" in row:
#                continue
#            if int(row[""]) > 50:
#                overall_top_stats.append(row)

#        overall_top_stats.sort(key=lambda x: int(x[3]))
#        overall_top_stats.reverse()
#        overall_top_stats[:10]
#        print(tabulate[top_stats])

def repeat():
    
    print("Do you want to go back to the start?")
    ans = input()
    if ans == 'yes':
        main()
    elif ans == 'no':
        exit()




def main():
    """
    Run all program functions
    """
    team_name = user_commands()
    user_commands_2(team_name)
    top_scorers()
    appearances()
    ages()
    #overall_top_stats()
    repeat()

main()

