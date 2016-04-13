from openbazar import Openbazaar
from user import Generate_Data
import sys
import time

def follow(user, pwd, to_follow, host='127.0.01'):
    if len(to_follow) != 40:
        print 'To follow number guid is wrong'
        exit(-1)
    print 'Following {0}'.format(to_follow)
    connected = False
    while not connected:
        try:
            bazaar = Openbazaar(user, pwd, host)
            connected = True
        except Exception:
            print 'Trying again'
            time.sleep(1)
            pass
    generator = Generate_Data()
    data = generator.create()
    bot = data[0]
    name = "{0} {1}".format(bot['name'], bot['surname'])
    print bazaar.set_profile(name,
                         bot['region'],
                         bot['primary_color'],
                         bot['secondary_color'],
                         bot['background_color'])
    for x in xrange(5):
        res = bazaar.follow(to_follow)
        if res.get('success') == True:
            break
        time.sleep(1)
    if res.get('success') == False:
        print 'Check the node to follow is on'
    else:
        print 'success'
    exit(1)

if __name__ == '__main__':
    user = 'get_followers'
    pwd = 'get_followers69'
    host = '127.0.0.1'
    if len(sys.argv) != 2:
        print 'Put the guid to follow'
        print 'Ex:'
        print "python script/run.py 187ecbdb6ac2d264330e77b85dab984ac50bc49e"
    to_follow = sys.argv[1]
    follow(user, pwd, to_follow, host)

