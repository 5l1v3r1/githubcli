#!/usr/bin/python
import requests, os, sys, time, webbrowser, getpass

# Import commands
from commands.get_repos import *
from commands.get_starred import *
from commands.search_user import *
from commands.clone import *
from commands.clone_all import *

api_url = 'https://api.github.com/'

error = '\033[31m[ERROR]\033[0m Invalid username or password'

banner = '''\033[37m
o          `O        o
O           o       O
o           O       o                                     O
O           O       O                                    oOo
o     o     o .oOo. o  .oOo  .oOo. `oOOoOO. .oOo.         o   .oOo.
O     O     O OooO' O  O     O   o  O  o  o OooO'         O   O   o
`o   O o   O' O     o  o     o   O  o  O  O O             o   o   O
 `OoO' `OoO'  `OoO' Oo `OoO' `OoO'  O  o  o `OoO'         `oO `OoO'


 .oOOOo.            o            o             Oo    OooOOo.  ooOoOOo
.O     o  o        O            O             o  O   O     `O    O
o              O   o            O            O    o  o      O    o
O             oOo  O            o           oOooOoOo O     .o    O
O   .oOOo O    o   OoOo. O   o  OoOo.       o      O oOooOO'     o
o.      O o    O   o   o o   O  O   o       O      o o           O
 O.    oO O    o   o   O O   o  o   O       o      O O           O
  `OooO'  o'   `oO O   o `OoO'o `OoO'       O.     O o'       ooOOoOo
\033[0m'''

info = '''
\033[37mCommands:\033[0m
    \033[37mGlobal:\033[0m
    clone <url>                       | Clone a repo
    clone all <username>              | Clone all user repos
    clear                             | Clear terminal screen
    exit/quit                         | Exit the console

    \033[37mUsers:\033[0m
    get repos <username>              | Get all users repos
    get starred <username>            | Get all users starred repos
    search <user>                     | Search for a repo or user

    \033[37mYour account:\033[0m
    delete <repo>                     | Delete a repo
    create <repo>                     | Create a repo
'''

def menu():
    try:
        while True:
            opt = raw_input('[#?] ')

            if opt == '?' or opt == 'help':
                print(info)
            elif opt == 'exit' or opt == 'quit':
                sys.exit(0)
            elif opt == 'clear':
                os.system('clear')
            elif opt.startswith('search '):
                username = opt.split(' ')[1]
                search_user(api_url, user, token, username)
            elif opt.startswith('get repos '):
                username = opt.split(' ')[2]
                get_repos(api_url, user, token, username)
            elif opt.startswith('get starred '):
                username = opt.split(' ')[2]
                get_starred(api_url, user, token, username)
            elif opt.startswith('clone all '):
                username = opt.split(' ')[-1]
                clone_all(api_url, user, token, username)
            elif opt.startswith('clone '):
                url = opt.split(' ')[1]
                clone(url)
            #elif opt.startswith('delete '):
            #    repo = opt.split(' ')[1]
            #    delete(api_url, user, token, repo)

            else:
                print('\033[31m[ERROR]\033[0m Invalid option')
    except KeyboardInterrupt:
        sys.exit(0)



def my_followers():
    # Parameters
    followers = []

    # Authenticate
    login = requests.get(api_url + 'user/followers', auth=(user, token))
    if login.status_code == 200:

        # Get all followers
        for follower in login.json():
            followers.append(follower)

        # Count followers and return
        return len(followers)
    else:
        print(error)

def my_emails():
    # Authenticate
    login = requests.get(api_url + 'user/emails', auth=(user, token))

    # Get Email
    for email in login.json():
        email = email['email']
        return email

def my_notifications():
    # Parameters
    notifications = []

    login = requests.get(api_url + 'notifications', auth=(user, token))

    # Get notifications
    for notification in login.json():
        notification.append(notification)
    return len(notifications)


def my_repos():
    # Parameters
    repos = []
    login = requests.get(api_url + 'user/repos', auth=(user, token))

    # Get notifications
    for url in login.json():
        repos.append(url)
    return len(repos)




# Login script start here
print('''
Please login with your credentials below.

Generate a token here: https://github.com/settings/tokens
''' )



try:
    user = raw_input('Username: ')
    token = getpass.getpass('Token: ')
    # Enter your details below and has the 2 lines above for static values
    #user = 'USERNAME'
    #token = 'TOKEN'

except KeyboardInterrupt:
    print('\n'); sys.exit(0)

testlogin = requests.get(api_url, auth=(user, token))

if testlogin.status_code == 200:
    print('Login \033[32m[OK]\033[0m')

    time.sleep(1)

    print(banner)

    print('''

    User:          %s
    Email:         %s
    Followers:     %s
    Notifications: %s
    Repos:         %s

    ''' % (user, my_emails(), my_followers(), my_notifications(), my_repos()))

    menu()
else:
    print(error); sys.exit(1)
