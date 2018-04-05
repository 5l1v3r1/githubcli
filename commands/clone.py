import os, sys

def clone(url):
    if os.path.isdir(('./repos')):
        os.system('git clone %s ./repos' % url)
    else:
        os.makedirs('./repos')
        os.system('git clone %s ./repos' % url)
