import requests
from prettytable import PrettyTable

def get_commits(api_url, token, username, repo):
    headers = {"Authorization": "token %s" % token}
    login = requests.get(api_url + 'repos/' + username + '/' + repo + '/commits', headers=headers)

    data = login.json()

    table = PrettyTable(['Date', 'Author', 'Committer', 'Message']) # Header
    table.align = "l" # Text Align left

    for i in range(len(data)):
        date = data[i]["commit"]["committer"]["date"].strip('TZ')
        author = data[i]["commit"]["author"]["name"]
        committer = data[i]["commit"]["committer"]["name"]
        message = data[i]["commit"]["message"]

        # Grab title only
        if "\n" in message:
            message = message.split('\n')[0]

        result = date, author, committer, message
        table.add_row([result[0], result[1], result[2], result[3]])

    # Print table
    print(table)
