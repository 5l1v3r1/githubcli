import requests, sys, os
# Blocking users is broken?
# Blocking users return this message:
# If you would like to help us test the User blocking api during its preview period,
# you must specify a custom media type in the 'Accept' header."
#

def block(api_url, user, token, username):
    login = requests.put(api_url + 'user/blocks/' + username, auth=(user,token))

    if login.status_code == 204:
        print('\033[32m[OK]\033[0m blocked %s' % username)
    else:
        print('\033[31m[%s]\033[0m Cannot block user' % login.status_code)

def unblock(api_url, user, token, username):
    login = requests.delete(api_url + 'user/blocks/' + username, auth=(user,token))

    if login.status_code == 204:
        print('\033[32m[OK]\033[0m unblocked %s' % username)
    else:
        print('\033[31m[%s]\033[0m Cannot unblock' % login.status_code)

def blocks(api_url, user, token):
    login = requests.get(api_url + 'user/blocks', auth=(user,token))

    c = 0

    header = "Username".ljust(25), "Profile".ljust(35), "Site Admin"
    print('\033[34m{0[0]} {0[1]} {0[2]}\033[0m'.format(header))

    for blocked in login.json():
        print('%s %s %s' % (blocked["login"].ljust(22), blocked["html_url"].ljust(38), blocked["site_admin"]))
        c+=1
    print('\033[32mFound %i blocked users\033[0m' % int(c))
