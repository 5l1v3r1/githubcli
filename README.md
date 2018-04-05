![alt text](http://leonvoerman.nl/coding/githubapi.png)
# github.py v0.0.1
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
    # Enter your details below and has the 2 lines above for static values
    #user = 'USERNAME'
    #token = 'TOKEN'
```

Usage:
```Shell
python github.py
```
