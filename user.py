import requests
import random

class Generate_Data():
    def __init__(self):
        self.url = 'http://uinames.com/api/'

    def create(self, nb=1):
        data = {'amount': nb,
                'region': 'United States',
                'gender': 'male'}
        res = requests.get(self.url, params=data)
        tmp = res.json()
        if nb == 1:
            tmp = [tmp]
        tmp = self.format_countries(tmp)
        return tmp

    def format_countries(self, data):
        for bot in data:
            tmp = bot['region']
            tmp = tmp.upper()
            bot['region'] = tmp.replace(' ', '_')
            bot['name'] = bot['name'].encode('utf-8')
            bot['surname'] = bot['surname'].encode('utf-8')
            bot['primary_color'] = self.random_colors()
            bot['background_color'] = self.random_colors()
            bot['secondary_color'] = self.random_colors()
        return data

    def random_colors(self):
        r = (random.randrange(0, 255) + 255) / 2
        g = (random.randrange(0, 255) + 255) / 2
        b = (random.randrange(0, 255) + 255) / 2
        return int("{0:02x}{1:02x}{2:02x}".format(r, g, b), 16)


if __name__ == '__main__':
    tmp = Generate_Data()
    print tmp.random_colors()