import requests, sys, os

def delete_repo(api_url, user, token, repo):
    login = requests.delete(api_url + 'repos/' + user + '/' + repo, auth=(user,token))

    print(login.status_code)

    if login.status_code == 204:
        print('\033[32m[OK]\033[0m Repo deleted')
    else:
        print('\033[31m[%s]\033[0m Cannot delete repo' % login.status_code)
