import requests, sys

def get_following(api_url, user, token, username):
    login = requests.get(api_url + 'users/' + username + '/following', auth=(user,token))

    c = 1

    header = "Username".ljust(25), "Profile"
    print('\033[34m{0[0]} {0[1]}\033[0m'.format(header))

    for follower in login.json():
        print('%i) %s %s' % (int(c), follower["login"].ljust(20), follower["html_url"]))
        c+=1
