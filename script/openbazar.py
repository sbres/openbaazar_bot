import requests
from binascii import hexlify

class Openbazaar():
    def __init__(self, user, pwd, host='127.0.0.1', port='18469'):
        self.url = 'http://{0}:{1}'.format(host, port)
        self.s = requests.Session()
        auth = {
            'username': user,
            'password': pwd,
        }
        auth_url = self.url + '/api/v1/login'
        r = self.s.post(auth_url, data=auth)
        res = r.json()
        if res.get('success', False) is False:
            print res.get('reason', "Authentification Error")
        self.guid = 42
        if self.get_profile() == {}:
            self.guid = None
        else:
            self.guid = self.get_profile()['profile']['guid']

    def get_profile(self, guid=None):
        followers_url = self.url + '/api/v1/profile'
        if guid is None or guid == self.guid:
            data = {}
        else:
            data = {'guid': guid}
        r = self.s.get(followers_url, params=data)
        return r.json()

    def get_followers(self, guid=None):
        followers_url = self.url + '/api/v1/get_followers'
        if guid is None or guid == self.guid:
            data = {}
        else:
            data = {'guid': guid}
        r = self.s.get(followers_url, params=data)
        return r.json()

    def set_profile(self, name, location, primary_color, secondary_color, background_color):
        followers_url = self.url + '/api/v1/profile'
        data = {'name': name,
                'location': location,
                'primary_color': primary_color,
                'background_color': background_color,
                'secondary_color': secondary_color
                }
        r = self.s.post(followers_url, params=data)
        return r.json()

    # def set_profile_header(self, file):
    #     followers_url = self.url + '/api/v1/profile'
    #     with open(file, 'rb') as f:
    #         content = f.read()
    #     out = hexlify(content)
    #
    #     files = {'header': ('00001.jpg', out)}
    #     r = self.s.post(followers_url, files=files)
    #     return r.json()

    def follow(self, guid):
        followers_url = self.url + '/api/v1/follow'
        data = {'guid': guid}
        r = self.s.post(followers_url, data=data)
        return r.json()

if __name__ == '__main__':
    user = 'sbres'
    pwd = 'fsdkjbfdskjbfsdfsds'
    host = '178.62.3.86'

    user = 'toto'
    pwd = 'tata'
    host = '46.101.93.158'
    bazaar = Openbazaar(user, pwd, host)


