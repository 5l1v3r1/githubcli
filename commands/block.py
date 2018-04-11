import requests, sys, os

def block(api_url, user, token, username):
    headers = {"Accept": "application/vnd.github.giant-sentry-fist-preview+json"}
    login = requests.put(api_url + 'user/blocks/' + username, auth=(user,token), headers=headers)

    if login.status_code == 204:
        print('\033[32m[OK]\033[0m blocked %s' % username)
    else:
        print('\033[31m[%s]\033[0m Cannot block user' % login.status_code)

def unblock(api_url, user, token, username):
    headers = {"Accept": "application/vnd.github.giant-sentry-fist-preview+json"}
    login = requests.delete(api_url + 'user/blocks/' + username, auth=(user,token), headers=headers)

    if login.status_code == 204:
        print('\033[32m[OK]\033[0m unblocked %s' % username)
    else:
        print('\033[31m[%s]\033[0m Cannot unblock' % login.status_code)

def blocks(api_url, user, token):
    headers = {"Accept": "application/vnd.github.giant-sentry-fist-preview+json"}
    login = requests.get(api_url + 'user/blocks', auth=(user,token), headers=headers)

    data = login.json()
    c = 0

    header = "Username".ljust(25), "Profile".ljust(35), "Site Admin"
    print('\033[34m{0[0]} {0[1]} {0[2]}\033[0m'.format(header))

    for i in range(len(data)):
        print('%s %s %s' % (data[i]["login"].ljust(22), data[i]["html_url"].ljust(38), data[i]["site_admin"]))
        c+=1
    print('\033[32mFound %i blocked users\033[0m' % int(c))

    #for blocked in login.json():
    #    print('%s %s %s' % (blocked["login"].ljust(22), blocked["html_url"].ljust(38), blocked["site_admin"]))
    #    c+=1
