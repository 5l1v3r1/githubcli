import requests, sys
from prettytable import PrettyTable

def get_starred(api_url, user, token, username):
    login = requests.get(api_url + 'users/' + username + '/starred', auth=(user, token))

    c = 0

    print('Starred repos by user %s\n' % username)

    table = PrettyTable(['Name', 'Link', 'Description']) # Header
    table.align = "l" # Text Align left

    if login.status_code == 200:
        for repo in login.json():
            name = repo["html_url"].split('/')[-1]
            if not repo["description"] == None:
                description = repo["description"]
                # Max characters for description
                if len(description) >= 80:
                    description = description[:80] + '...'
            else:
                description = None

            result = name, repo["html_url"], description
            table.add_row([result[0], result[1], result[2]])

            c+=1

        print(table)
        print('\033[32mFound %i results\033[0m' % int(c))

    else:
        print('\033[31m[ERROR]\033[0m Cannot find any repos for this user')
