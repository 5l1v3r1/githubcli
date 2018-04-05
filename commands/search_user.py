import requests, sys

def search_user(api_url, user, token, username):
    #login = requests.get(api_url + 'users/' + username + '/repos', auth=(user, token))
    login = requests.get(api_url + 'users/' + username, auth=(user, token))

    if login.status_code == 200:
        # Get Data
        info = login.json()
        name = info["name"]
        location = info["location"]
        company = info["company"]
        bio = info["bio"]
        email = info["email"]
        url = info["html_url"]
        utype = info["type"]
        admin = info["site_admin"]
        created = info["created_at"]

        # Find followers and repos
        repos = []
        followers = []

        login = requests.get(api_url + 'users/' + username + '/followers', auth=(user, token))

        for follower in login.json():
            followers.append(follower)

        login = requests.get(api_url + 'users/' + username + '/repos', auth=(user, token))
        for repo in login.json():
            repos.append(repo)


        print('''
    Result:
        Username:      %s
        Name:          %s
        Location:      %s
        Company:       %s
        Email:         %s
        Profile URL    %s
        Type:          %s
        is Admin:      %s
        Created:       %s

        Bio:           %s

        Followers:     %i
        Repos:         %i

        ''' % (username, name, location, company, email, url, utype, admin, created, bio, len(followers), len(repos)))

    else:
        print('\033[31m[ERROR]\033[0m User does not exist')
