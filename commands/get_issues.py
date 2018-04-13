import requests
from prettytable import PrettyTable

def get_issues(api_url, user, token, owner, repo):
    login = requests.get(api_url + 'repos/' + owner + '/' + repo + '/issues', auth=(user, token))

    c = 0

    table = PrettyTable(['From', 'State', 'Title', 'Link']) # Header
    table.align = "l" # Text Align left

    data = login.json()

    for i in range(len(data)):
        # Grab data for each issue
        uname = data[i]["user"]["login"]
        state = data[i]["state"]
        title = data[i]["title"]
        url = data[i]["html_url"]

        # Max title length is 70 characters
        if len(title) >= 35:
            title = title[:35] + '...'

        result = uname, state, title, url
        table.add_row([result[0], result[1], result[2], result[3]])

        c+=1

    print(table)
    print('\033[32mDisplaying %i issues\033[0m' % int(c))
