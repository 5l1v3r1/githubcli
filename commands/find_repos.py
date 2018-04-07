import requests, sys

def find_repos(api_url, user, token, string):
    login = requests.get(api_url + 'search/repositories?q=' + string, auth=(user,token))

    c = 0

    result = login.json()

    header = "Url".ljust(50), "Description"
    print('\033[37m{0[0]} {0[1]}\033[0m'.format(header))

    for i in range(len(result["items"])):
        #print(result["items"][i]["full_name"]) # Full name
        #print(result["items"][i]["owner"]["login"]) # owner name
        #print(result["items"][i]["html_url"]) # Url to repo
        #print(result["items"][i]["description"]) # description of repo

        print('%s %s ' % (result["items"][i]["html_url"].ljust(50), result["items"][i]["description"]))
        c+=1



    #for found in login.json():
    #    print('%s %s %s' % (found["name"].ljust(25), found["login"], found["html_url"]))
    #    c+=1

    print('\033[32mDisplaying %i results out of %i\033[0m' % (int(c), result["total_count"]))
