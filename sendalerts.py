import sendsms
import sendemail

def sendAlerts(users, subs, tweet_text):
    '''Send subscribed alerts when a matching tweet is streamed'''
    subs_to_send = []
    for sub in subs:
        if any(keyword.lower() in tweet_text.lower() for keyword in sub.keywords[0]):
            subs_to_send.append(sub.name)
            break
    for sub in subs_to_send:
        for user in users:
            if sub in user.subscriptions[0]:
                if any(vendor.lower() in tweet_text.lower() for vendor in user.vendors[0]):
                    if user.phone != None:
                        sendsms.send(user.phone[0], user.phone[1], tweet_text)
                    if user.email != None:
                        sendemail.send(user.email, f'{sub} ALERT', tweet_text)
        