import requests, json, sys, os

def create_repo(api_url, user, token, repo):
    payload = {'name': repo, 'description': 'Created with Github API', 'auto_init': 'true'}
    login = requests.post(api_url + 'user/repos', auth=(user,token), data=json.dumps(payload))

    if login.status_code == 201:
        print('\033[32m[OK]\033[0m Repo created')
    else:
        print('\033[31m[%s]\033[0m Cannot create repo')
