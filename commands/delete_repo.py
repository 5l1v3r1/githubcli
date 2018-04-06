import requests, sys, os

def delete_repo(api_url, user, token, repo):
    login = requests.delete(api_url + 'repos/' + user + '/' + repo, auth=(user,token))

    if login.status_code == 201:
        print('\033[31m[%s]\033[0m Repo does not exist' % login.status_code)
    else:
        print('\033[32m[OK]\033[0m Repo deleted')
