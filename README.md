![alt text](http://leonvoerman.nl/coding/githubapi.png)
# github.py v0.1.1
> Feel free to request more commands! 
> I'll be happy to add them in the future.

***

Interract with the GitHub API. Find info about users and repos.

You'll need to login with your Github username and API token, which you can generate here: https://github.com/settings/tokens

Installation:
```Shell
pip install -r required.txt
```

Note the near bottom of github.py:
```Python
    user = raw_input('Username: ')
    token = getpass.getpass('Token: ')
    # Enter your details below and hash the 2 lines above for static values
    #user = 'USERNAME'
    #token = 'TOKEN'
```

Usage:
```Shell
python github.py
```

Features:
```Shell
Commands:
    Global:
    clone <url>                       | Clone a repo
    clone all <username>              | Clone all user repos
    clear                             | Clear terminal screen
    exit/quit                         | Exit the console

    Users:
    get repos <username>              | Get all users repos
    get starred <username>            | Get all users starred repos
    get followers <username>          | Get all users who are following this user
    get following <username>          | Get all users who this user is following
    search <user>                     | Search for a user
    find <string>                     | Search for repositories by string

    Your account:
    profile                           | Show your profile
    delete <repo>                     | Delete a repo
    create <repo>                     | Create a repo
    edit repo/item/string             | Valid Items: name, description, homepage, private
    donothitenternow                  | Do Not Hit Enter Now -> DELETES ALL REPOS !!
```

Base code:
```Python
login = requests.get('https://api.github.com/', auth=(user, token))
print(login.json()) # Show other links and format from here.

```

Test API:
```Shell
curl -i https://api.github.com/ -u USERNAME:TOKEN
```

GET command template (example):
```Python
import requests, os, sys

def command_name(api_url, user, token, key_in_dict):

    login = requests.get(api_url, auth=(user, token))
    
    output = login.json()
    
    print(output.keys()) # output all keys in dict
    data = output[key_in_dict] # Which will be "html_url" in this case.
    
# Usage:
#command_name(api_url, user, token, "html_url")

# Add on top of github.py
#from commands.command_name import *
```

POST command template (example):
```Python
import requests, json, sys, os

def create_repo(api_url, user, token, repo):
    payload = {'name': repo, 'description': 'Created with Github API', 'auto_init': 'true'}
    login = requests.post(api_url + 'user/repos', auth=(user,token), data=json.dumps(payload))

    if login.status_code == 201:
        print('\033[32m[OK]\033[0m Repo created')
    else:
        print('\033[31m[%s]\033[0m Cannot create repo')

```
