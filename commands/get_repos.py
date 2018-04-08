import requests, sys

def get_repos(api_url, user, token, username):
    login = requests.get(api_url + 'users/' + username + '/repos', auth=(user, token))

    c = 1

    header = "Name".ljust(35), "link".ljust(50), "Description"
    print('\033[37m{0[0]} {0[1]} {0[2]}\033[0m'.format(header))

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

            print('%i) %s %s %s' % (int(c), name.ljust(32), repo["html_url"].ljust(50), description))

            c+=1
    else:
        print('\033[31m[ERROR]\033[0m Cannot find any repos for this user')
