import sendsms
import sendemail
import logging

def sendAlerts(users, subs, tweet_text, tweet_user):
    '''Send subscribed alerts when a matching tweet is streamed'''
    subs_to_send = []
    valid_accounts = []
    for sub in subs:
        if any(keyword.lower() in tweet_text.lower() for keyword in sub.keywords[0]):
            subs_to_send.append(sub.name)
            accounts = [name for name in sub.twitter_names[0] if name not in valid_accounts]
            #print(f'accounts: {accounts}')
            for name in accounts:
                valid_accounts.append(name)
            #break
    #print(f'valid accounts: {valid_accounts}')
    for sub in subs_to_send:
        if tweet_user.replace('@', '') in valid_accounts:
            for user in users:
                if sub in user.subscriptions[0]:
                    if any(vendor.lower() in tweet_text.lower() for vendor in user.vendors[0]):
                        if user.phone[0] != 'None':
                            logging.info(f'Sending SMS to {user.name}')
                            sendsms.send(user.phone[0], user.phone[1], tweet_text)
                        if user.email != 'None':
                            logging.info(f'Sending email to {user.name}')
                            sendemail.send(user.email, f'{sub} ALERT', tweet_text)
        