#!/usr/bin/python
# This is most likely the stupidest thing I ever coded.

import requests

def delete_all(api_url, user, token):
    login = requests.get(api_url + 'user/repos', auth=(user, token))

    repos = login.json()

    for url in repos:
        url = url["html_url"]
        repo = url.split('/')[-1]
        delete = requests.delete(api_url + 'repos/' + user + '/' + repo, auth=(user,token))
