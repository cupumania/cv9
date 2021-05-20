import tweepy
import csv

consumer_key = 'xxxx'
consumer_secret = 'xxxx'
access_token = 'xxxx-xxxx'
access_token_secret = 'xxxx'
#------------------------------------
##end editing

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)


csvFile = open('contoh.csv', 'a')
csvWriter = csv.writer(csvFile, delimiter=',')

for tweet in tweepy.Cursor(api.search,
                           q = "tokopedia",
                           since = "2020-06-14",
                           until = "2020-06-15",
                           lang = "id").items():

    # Write a row to the CSV file. I use encode UTF-8
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    print tweet.created_at, tweet.text

csvFile.close()
