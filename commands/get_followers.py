import requests, sys
from prettytable import PrettyTable

def get_followers(api_url, user, token, username):
    login = requests.get(api_url + 'users/' + username + '/followers' + '?per_page=100', auth=(user,token))

    c = 0

    table = PrettyTable(['Username', 'Profile', 'Site Admin']) # Header
    table.align = "l" # Text Align left

    for follower in login.json():
        result = follower["login"], follower["html_url"], follower["site_admin"]
        table.add_row([result[0], result[1], result[2]])
        c+=1
        
    print(table)
    print('\033[32mFound %i results\033[0m' % int(c))
