import yaml

class Sub:
    '''Subscriptions schema'''
    def __init__(self, name) -> None:
        self.name = name
        self._enable = False
        self._keywords = []
        self._twitter_names = []
        self._twitterIDs = []

    @property
    def enable(self):
        '''Enable getter''' 
        return self._enable

    @enable.setter
    def enable(self, e):
        '''Enable setter'''
        self._enable = e
    
    @property
    def keywords(self):
        '''Keywords getter''' 
        return self._keywords

    @keywords.setter
    def keywords(self,k):
        '''Keywords setter'''
        self._keywords.append(k)

    @property
    def twitter_names(self):
        '''Twitter_names getter''' 
        return self._twitter_names

    @twitter_names.setter
    def twitter_names(self,t):
        '''Twitter_names setter'''
        self._twitter_names.append(t)

    @property
    def twitterIDs(self):
        '''TwitterIDs getter''' 
        return self._twitterIDs

    @twitterIDs.setter
    def twitterIDs(self,t):
        '''TwitterIDs setter'''
        self._twitterIDs.append(t)

def getSubsConfig():
    '''Get subscriptions config from YAML'''
    subs = []
    with open('config.yaml', 'r') as stream:
        configdict = yaml.load(stream, Loader=yaml.FullLoader)
        for k,v in configdict['Subscriptions'].items():
            sub = Sub(v['name'])
            if v['enable'] == False:
                pass
            else:
                sub.keywords = v['keywords']
                sub.twitter_names = v['twitter_names']
                subs.append(sub)
    return subs

if __name__ == '__main__':
    subs = getSubsConfig()
    print(subs)
    print(subs[0].keywords)