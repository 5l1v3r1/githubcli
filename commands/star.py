import requests

def star(api_url, user, token, username, repo):
    login = requests.put(api_url + 'user/starred/' + username + '/' + repo, auth=(user,token))

    if login.status_code == 204:
        print('\033[32m[OK]\033[0m You starred %s' % repo)
    else:
        print('\033[31m[%i]\033[0m Failed to star repo' % login.status_code)

def unstar(api_url, user, token, username, repo):
    login = requests.delete(api_url + 'user/starred/' + username + '/' + repo, auth=(user,token))

    if login.status_code == 204:
        print('\033[32m[OK]\033[0m Removed star from %s' % repo)
    else:
        print('\033[31m[%i]\033[0m Failed to unstar repo' % login.status_code)
