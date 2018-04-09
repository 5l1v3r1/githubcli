import requests

def get_issues(api_url, user, token, owner, repo):
    login = requests.get(api_url + 'repos/' + owner + '/' + repo + '/issues', auth=(user, token))

    c = 0

    header = "From".ljust(25), "State".ljust(15), "Title".ljust(40), "Link"
    print('\033[37m{0[0]} {0[1]} {0[2]} {0[3]}\033[0m'.format(header))

    result = login.json()

    for i in range(len(result)):
        # Grab data for each issue
        uname = result[i]["user"]["login"]
        state = result[i]["state"]
        title = result[i]["title"]
        url = result[i]["html_url"]

        # Max title length is 70 characters
        if len(title) >= 35:
            title = title[:35] + '...'

        print('%s %s %s %s ' % (uname.ljust(25), state.ljust(15), title.ljust(40), url))
        c+=1
    print('\033[32mDisplaying %i issues\033[0m' % int(c))
