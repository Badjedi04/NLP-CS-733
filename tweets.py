import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "#gotagohome OR #gotagoranil OR #srilankaeconomiccrisis OR #gohomegota OR #gohomemahinda OR #gohomerajapaksas OR #srilankacrisis OR # fuelcrisislk OR #srilankaprotests) lang:en until:2022-08-16 since:2022-07-16 -filter:links -filter:replies"
tweets = []
limit = 50000

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        
        #print(vars(tweet))
        #break
        if len(tweets) == limit:
                break
        else:
                tweets.append([tweet.date, tweet.user.username, tweet.content])
df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
print(df)

df.to_csv('tweets_post.csv')