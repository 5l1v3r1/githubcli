import requests

def get_commits(api_url, token, username, repo):
    headers = {"Authorization": "token %s" % token}
    login = requests.get(api_url + 'repos/' + username + '/' + repo + '/commits', headers=headers)

    data = login.json()

    #print(data[0]["commit"]["author"]["name"])
    #print(data[0]["commit"]["committer"]["name"])
    #print(data[0]["commit"]["committer"]["date"])
    #print(data[0]["commit"]["message"])

    header = "Date".ljust(30), "Author".ljust(30), "Committer".ljust(20), "Message"
    print('\033[37m{0[0]} {0[1]} {0[2]} {0[3]}\033[0m'.format(header))

    for i in range(len(data)):
        date = data[i]["commit"]["committer"]["date"].strip('TZ')
        author = data[i]["commit"]["author"]["name"]
        commiter = data[i]["commit"]["committer"]["name"]
        message = data[i]["commit"]["message"]

        # Grab title only
        if "\n" in message:
            message = message.split('\n')[0]

        print('%s %s %s %s' % (date.ljust(30), author.ljust(30), commiter.ljust(20), message))
