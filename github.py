#!/usr/bin/python
# Link to docs:
# requests: http://docs.python-requests.org/en/master/user/quickstart/
# API:      https://developer.github.com/v3/
import requests, os, sys, time, getpass, readline

# Import commands
from commands.get_repos import *
from commands.get_starred import *
from commands.search_user import *
from commands.clone import *
from commands.clone_all import *
from commands.delete_repo import *
from commands.create_repo import *
from commands.edit_repo import *
from commands.get_followers import *
from commands.get_following import *
from commands.find_repos import *
from commands.profile import *
from commands.delete_all import *
from commands.follow import *
from commands.block import *
from commands.get_issues import *
from commands.get_commits import *

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
    get followers <username>          | Get all users who are following this user
    get following <username>          | Get all users who this user is following
    get issues <username> <repo>      | Show issues for this repo
    get commits <username> <repo>     | Show all commits for this repo
    search <user>                     | Search for a user
    find <string>                     | Search for repositories by string
    follow <username>                 | Follow this user
    unfollow <username>               | Unfollow this user
    block <username>                  | Block this user
    unblock <username>                | Unblock this user
    blocks                            | Show all blocked users

    \033[37mYour account:\033[0m
    profile                           | Show your profile
    delete <repo>                     | Delete a repo
    create <repo>                     | Create a repo
    edit repo/item/string             | Valid Items: name, description, homepage, private
    donothitenternow                  | Do Not Hit Enter Now -> DELETES ALL REPOS !!
'''

def menu():
    try:

        while True:
            opt = raw_input('[github] > ')

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
            elif opt.startswith('delete '):
                repo = opt.split(' ')[1]
                delete_repo(api_url, user, token, repo)
            elif opt.startswith('create '):
                repo = opt.split(' ')[1]
                create_repo(api_url, user, token, repo)
            elif opt.startswith('edit '):
                repo = opt.split('/')[0][5:]
                item = opt.split('/')[1]
                value = opt.split('/')[2]
                edit_repo(api_url, user, token, item, value, repo)
            elif opt.startswith('get followers '):
                username = opt.split(' ')[-1]
                get_followers(api_url, user, token, username)
            elif opt.startswith('get following '):
                username = opt.split(' ')[-1]
                get_following(api_url, user, token, username)
            elif opt.startswith('find '):
                string = opt.replace('find ', '')
                string = string.replace(' ', '+')
                find_repos(api_url, user, token, string)
            elif opt.startswith('profile'):
                profile(api_url, user, token)
            elif opt == 'donothitenternow':
                delete_all(api_url, user, token)
            elif opt.startswith('follow '):
                username = opt.split(' ')[1]
                follow(api_url, user, token, username)
            elif opt.startswith('unfollow '):
                username = opt.split(' ')[1]
                unfollow(api_url, user, token, username)
            elif opt.startswith('block '):
                username = opt.split(' ')[1]
                block(api_url, user, token, username)
            elif opt.startswith('unblock '):
                username = opt.split(' ')[1]
                unblock(api_url, user, token, username)
            elif opt == 'blocks':
                blocks(api_url, user, token)
            elif opt.startswith('get issues '):
                owner = opt.split(' ')[2]
                repo = opt.split(' ')[3]
                get_issues(api_url, user, token, owner, repo)
            elif opt.startswith('get commits '):
                username = opt.split(' ')[2]
                repo = opt.split(' ')[3]
                get_commits(api_url, token, username, repo)
            else:
                print('\033[31m[ERROR]\033[0m Invalid option')
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print('\033[31m[ERROR]\033[0m %s' % e)
        return menu()

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

    print(banner)
    profile(api_url, user, token)
    menu()
else:
    print(error); sys.exit(1)
