import requests, json

def edit_repo(api_url, user, token, item, value, repo):
    payload = {"name": repo, item: value}
    login = requests.post(api_url + 'repos/' + user + '/' + repo, auth=(user,token), data=json.dumps(payload))

    print(login.status_code)
    print(login.content)
