import requests, sys

def get_repos(api_url, user, token, username):
    login = requests.get(api_url + 'users/' + username + '/repos', auth=(user, token))

    c = 0

    if login.status_code == 200:
        for repo in login.json():
            print('\t%i) %s' % (int(c), repo["html_url"]))
            c+=1
    else:
        print('\033[31m[ERROR]\033[0m Cannot find any repos for this user')
