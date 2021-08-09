import yaml

class User:
    def __init__(self, name) -> None:
        self.name = name
        self._enable = False
        self._phone = None
        self._carrier = None
        self._email = None
        self._subscriptions = []
        self._vendors = []

    @property
    def enable(self):
        '''Enable getter''' 
        return self._enable

    @enable.setter
    def enable(self, e):
        '''Enable setter'''
        self._enable = e

    @property
    def phone(self):
        '''Phone getter''' 
        return self._phone, self._carrier

    @phone.setter
    def phone(self, p):
        '''Phone setter'''
        self._phone = p[0]
        self._carrier = p[1]

    @property
    def email(self):
        '''Email getter''' 
        return self._email

    @email.setter
    def email(self,e):
        '''Email setter'''
        self._email = e
    
    @property
    def subscriptions(self):
        '''Subscription getter''' 
        return self._subscriptions

    @subscriptions.setter
    def subscriptions(self,s):
        '''Subscription setter'''
        self._subscriptions.append(s)

    @property
    def vendors(self):
        '''Vendors getter''' 
        return self._vendors

    @vendors.setter
    def vendors(self,v):
        '''Vendors setter'''
        self._vendors.append(v)

def getUserConfig():
    users = []
    with open('config.yaml', 'r') as stream:
        configdict = yaml.load(stream, Loader=yaml.FullLoader)
        for k,v in configdict['Users'].items():
            user = User(v['name'])
            if v['enable'] == False:
                pass
            else:
                if v['phone'] != None:
                    user.phone = (v['phone'], v['carrier'])
                if v['email'] != None:
                    user.email = v['email']
                user.subscriptions = v['subscriptions']
                user.vendors = v['vendors']
                users.append(user)
    return users
