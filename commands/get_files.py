import requests

def get_files(api_url, user, token, username, repo):
    login = requests.get(api_url + 'repos/' + username + '/' + repo + '/contents', auth=(user, token))

    data = login.json()
    header = "Path".ljust(30), "Type".ljust(20), "Size"
    print('\033[37m{0[0]} {0[1]} {0[2]}\033[0m'.format(header))

    for i in range(len(data)):
        path = data[i]["path"]
        size = data[i]["size"]
        _type = data[i]["type"]
        print('%s %s %s' % (path.ljust(30), _type.ljust(20), size))

        if _type == 'dir':
            get_dir_files(api_url, user, token, username, repo, path)

def get_dir_files(api_url, user, token, username, repo, path):
    login = requests.get(api_url + 'repos/' + username + '/' + repo + '/contents/' + path, auth=(user, token))
    data = login.json()
    for i in range(len(data)):
        path = data[i]["path"]
        size = data[i]["size"]
        _type = data[i]["type"]
        print('%s %s %s' % (path.ljust(30), _type.ljust(20), size))
        if _type == "dir":
            return get_dir_files(api_url, user, token, username, repo, path) # Search all levels
