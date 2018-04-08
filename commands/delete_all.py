#!/usr/bin/python
# This is most likely the stupidest thing I ever coded.

import requests

def delete_all(api_url, user, token):
    login = requests.get(api_url + 'user/repos', auth=(user, token))

    repos = login.json()
    c = 0

    for url in repos:
        repo = url["html_url"].split('/')[-1]
        delete = requests.delete(api_url + 'repos/' + user + '/' + repo, auth=(user,token))
        c+=1
        print('\033[31mDeleted %s [%i/%i]\033[0m' % (repo, int(c), len(repos)))
