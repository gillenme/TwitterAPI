from twython import Twython
import csv

# Here we are importing the Twython library we previously installed. We are also importing the csv module so we can later save the data we're gathering from Twitter into an easy-to-read and use Excel file.

APP_KEY = '1234567890'
APP_SECRET = '1234567890'
OAUTH_TOKEN = '1234567890'
OAUTH_TOKEN_SECRET = '1234567890'

#Now obviously '1234567890' isn't the actual code you need for the script to work, it's simply a placeholder. Refer back to your My Applications page on the Twitter Developer page. The naming Twitter uses for these authorization codes is a little confusing, but to make it easier:

#APP_KEY = Consumer Key
#APP_SECRET = Consumer Secret
#OAUTH_TOKEN = Access Token
#OAUTH_TOKEN_SECRET = Access Token Secret

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter = Twython(access_token=ACCESS_TOKEN)

searchterm = 'Python'
results = twitter.search(q=searchterm)

# Here, we are defining results as tweets containing the search term 'python'. Feel free to change this term to whatever you would like! 

if results.get('statuses'):
   for result in results['statuses']:
     print result['text']
    
# Here, we are telling our script to return the results to the terminal so that we can read them. Later, we will print them to a CSV file. 

with open ('data.csv', 'w') as fp:
    a = csv.writer(fp)
    
#Open the CSV file. 'data.csv' can be renamed to whatever you would like. This is the filename it will save under.

    a.writerow(('Search Term', 'Tweet Text'))

#At the top of the CSV file, we want to add in a row with columns labeled 'Search Term' and 'Tweet Text'.

    for result in results['statuses']:
        text=[[searchterm, result['text'].encode('utf-8')]]
        a.writerows((text))
        
#For every result we pulled earlier, we want to print the search term attached to it as well as the text, making sure that it is in UTF-8 encoding so special characters will print and not return an error.
