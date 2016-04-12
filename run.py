from openbazar import Openbazaar
from user import Generate_Data



if __name__ == '__main__':
    nb = 1
    user = 'toto'
    pwd = 'tata'
    host = '46.101.93.158'
    to_follow = 'ob://798b7243a876916b3115918a7216ccb4b06b7c2a/followers'
    bazaar = Openbazaar(user, pwd, host)
    generator = Generate_Data()
    data = generator.create(nb)
    bot = data[0]
    name = "{0} {1}".format(bot['name'], bot['surname'])
    print bazaar.set_profile(name,
                                 bot['region'],
                                 bot['primary_color'],
                                 bot['secondary_color'],
                                 bot['background_color'])
    bazaar.follow(to_follow)

