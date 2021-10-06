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

team_name = ""
position = ""
top_stats = ""


def user_commands():
    """
    gives commands the user is able to input to receive different data sets
    """
    options = 'Man United, Man City, Liverpool, Chelsea'
    print(f"1: {options}")

    team_name = input("Please Enter A Team Name:\n").casefold()
    print(f"You Have Entered {team_name}\n")

    while team_name not in data:
        print("You Entered a Wrong Option, Please Enter A Correct Option")
        print(f"1: {options}")
        team_name = input()

    print(tabulate(data[team_name]))
    return team_name


def user_commands_2(team_name):
    """
    function to see players of a set position
    from data received from first input.
    Players can be goalkeepers, defenders, midfielders or forwards
    """
    options_1 = 'goalkeeper, defender, midfielder,\nforward, home'
    print(f"1: {options_1}")

    position = input("\nPlease Enter a Position:\n").casefold()
    print(f"You Have Entered {position}\n")

    while position.casefold() not in (options_1):
        print("\nYou Entered a Wrong Option, Please Enter a Correct Option")
        print(f"1: {options_1}")
        position = input()

    if position.casefold() == 'home':
        print("Hi! Welcome to a Football Stats Generator")
        print("The Available Options Are As Follows:")
        main()

    res = [i for i in data[team_name] if position.capitalize() in i]
    print(tabulate(res))

print("Hi! Welcome To a Football Stats Generator\n")
print("The Available Options Are As Follows:\n")


def top_scorers():
    """
    Takes the goal scoring data from the
    spreadsheet and present it to the user
    with the list ordered by the most goals
    scored per team.
    """
    goal_scorers = []

    options = '\nman united, man city, liverpool, chelsea, home'
    print(f"{options}")
    team_name = input("\nPlease Enter Team To See Top Goal Scorers:\n").casefold()
    print(f"you have entered: {team_name}")

    if team_name == 'home':
        print("Hi! Welcome To a Football Stats Generator\n")
        print("The Available Options Are As Follows:\n")
        main()

    while team_name not in (options):
        print("\nYou Entered a Wrong Option, Please Enter a Correct Option")
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
    function to compare players appearances and return
    a value if their appearances after over 100 for their team.
    It then prints the results to the terminal/console
    """
    player_apps = []

    options = 'man united, man city, liverpool, chelsea, home'
    print(f"1: {options}")
    team_name = input("\nEnter Team To See Players With 100 Appearances:\n").casefold()
    print(f"You Have Entered: {team_name}")

    if team_name == 'home':
        print("Hi! Welcome to a Football Stats Generator\n")
        print("The Available Options Are As Follows:\n")
        main()

    while team_name not in (options):
        print("\nYou Entered a Wrong Option, Please Enter a Correct Option")
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
    team_name = input("\nPlease Team To See Players Ages:\n").casefold()
    print(f"You Have Entered: {team_name}")

    if team_name == 'home':
        print("Hi! Welcome to a Football Stats Generator\n")
        print("The Available Options Are As Follows:\n")
        main()

    while team_name not in (options):
        print("\nYou Entered a Wrong Option, Please Enter a Correct Option")
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

#
# 'def overall_top_stats():


#    options = 'most goals, most appearances, most clean sheets, home'
#    print(f"1: {options}")
#    top_stats = input("Enter an Option To See The Overall Top Players:\n")
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
    """
    Gives user option to go back to start or exit program
    """
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
    # 'overall_top_stats()
    repeat()

main()
