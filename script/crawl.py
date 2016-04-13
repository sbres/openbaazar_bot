from openbazar import Openbazaar
from user import Generate_Data
import random
user = 'toto'
pwd = 'tata'
host = '46.101.93.158'

def extract_guids(data, already=[]):
    for user in data.get('followers', []):
        guid = user['guid']
        if guid not in already:
            already.append(guid)
    return already

def get_guid(root, bazaar, to_find=100):
    root_followers = bazaar.get_followers(root)
    print root_followers
    nodes = extract_guids(root_followers)
    if nodes == 0:
        return []
    while len(nodes) < to_find:
        user = random.choice(nodes)
        print 'LOOP {0}'.format(len(nodes))
        print 'Checking {0}'.format(user)
        user_followers = bazaar.get_followers(user)
        nodes = extract_guids(user_followers, nodes)
    return nodes

if __name__ == '__main__':
    root = '7a94af9cf4d784a974a17e18089ce62f529ce41f'
    bazaar = Openbazaar(user, pwd, host)
    get_guid(root, bazaar, 5000)