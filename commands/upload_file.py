import requests, hashlib, os, getpass

def upload_file(api_url, user, token, username, repo):
    # Local paths
    local_filepath = raw_input("Local filepath (/home/%s/): " % getpass.getuser())
    if os.path.isfile(local_filepath):
        pass
    else:
        print('File does not exist, try again...')
        return upload_file(api_url, user, token, username, repo)

    git_filepath = raw_input("Git filepath: " )
    message = raw_input("Commit message: ")

    # Encoding
    with open(local_filepath, 'rb') as f:
        base64_encoding = f.read()
        base64_encoding = base64_encoding.encode('base64')

    BLOCKSIZE = 65536
    hasher = hashlib.sha1()
    with open(local_filepath, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
    sha = hasher.hexdigest() # Get shasum

    print('Uploading: %s' % local_filepath)
    print('To: %s ' % git_filepath)
    print('With sha: %s' % sha)
    print('With message: %s' % message)
    print('--------BASE64--------\n%s\n--------END OF BASE64--------' % base64_encoding)


    # Upload file
    headers = {"path": git_filepath, "message": message, "content": base64_encoding}
    login = requests.put(api_url + 'repos/' + username + '/' + repo + '/contents/' + git_filepath, auth=(user, token), headers=headers)

    if login.status_code == 201:
        print('\033[32m[OK]\033[0m File created')
    else:
        print("\033[31m[%s]\033[0m Mission failed, we'll get 'em next time...'" % login.status_code)
        print(login.json())
