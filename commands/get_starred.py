import requests, sys

def get_starred(api_url, user, token, username):
    login = requests.get(api_url + 'users/' + username + '/starred', auth=(user, token))

    c = 0

    if login.status_code == 200:
        print('Starred repos by user %s' % username)
        for repo in login.json():
            print('\t%i) %s' % (int(c), repo["html_url"]))
            print('\t%s\n' % repo["description"])
            c+=1
    else:
        print('\033[31m[ERROR]\033[0m Cannot find any repos for this user')
