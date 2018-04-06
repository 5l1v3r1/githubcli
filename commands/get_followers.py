import requests, sys

def get_followers(api_url, user, token, username):
    login = requests.get(api_url + 'users/' + username + '/followers', auth=(user,token))

    c = 1

    header = "Username".ljust(25), "Profile"
    print('\033[34m{0[0]} {0[1]}\033[0m'.format(header))

    for follower in login.json():
        print('%i) %s %s' % (int(c), follower["login"].ljust(22), follower["html_url"]))
        c+=1
