import tweepy
import user
import subs
from sendalerts import sendAlerts
from twitconfig import create_api

class MyStreamListener(tweepy.StreamListener):
    '''Listener for subscribed tweets.  On status events send notifications to subscribed users'''

    def __init__(self, api, users, subs):
        self.api = api
        self.users = users
        self.subs = subs

    def on_status(self, tweet):
        #print(f"{tweet.user.name}:{tweet.text}")
        sendAlerts(self.users, self.subs, tweet.text, tweet.user.name)

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return False

def loadUser():
    '''Loads user class'''
    return user.getUserConfig()

def loadSubs(api):
    '''Loads subscriptions class and translates twitternames to IDs'''
    my_subs = subs.getSubsConfig()
    for sub in my_subs:
        for name in sub.twitter_names[0]:
            user = api.get_user(name)
            sub.twitterIDs.append(user.id_str)
    return my_subs

def main():
    '''Loads everything and establishes listener'''
    api = create_api()
    my_users = loadUser()
    my_subs = loadSubs(api)
    myStreamListener = MyStreamListener(api, my_users, my_subs)
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
    listen_IDs = []
    for sub in my_subs:
        for ID in sub.twitterIDs:
            listen_IDs.append(ID)
    myStream.filter(follow=listen_IDs, is_async=True)


if __name__ == '__main__':
    main()

        