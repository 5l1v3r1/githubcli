import requests, sys

def get_following(api_url, user, token, username):
    login = requests.get(api_url + 'users/' + username + '/following' + '?per_page=100', auth=(user,token))

    c = 0

    header = "Username".ljust(25), "Profile".ljust(35), "Site Admin"
    print('\033[34m{0[0]} {0[1]} {0[2]}\033[0m'.format(header))

    for follower in login.json():
        print('%s %s %s' % (follower["login"].ljust(22), follower["html_url"].ljust(38), follower["site_admin"]))
        c+=1
    print('\033[32mFound %i results\033[0m' % int(c))
