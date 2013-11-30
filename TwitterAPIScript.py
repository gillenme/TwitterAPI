from twython import Twython
import csv, json

#The following are the keys that are created when you register your app through Twitter.

APP_KEY = 'sYKvYkH7Em9XGQyoT0LCw'
APP_SECRET = 'BEPRFgO3jKqIJ7CcFki9mCZbS8eXfoJJvpHkg8t3Uk'
OAUTH_TOKEN = '16723356-J8Xw0S4DrbntPgAEOvJ5E3m5AKzColMNAO6OLl3Uh'
OAUTH_TOKEN_SECRET = 'Hz2GOihqgJ6Hq9QliIMAUdw6Cak98fTEbdeBAAOIFUYtZ'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter = Twython(access_token=ACCESS_TOKEN)

results = twitter.search(q='sondheim')
if results.get('statuses'):
   for result in results['statuses']:
     print result['text']
