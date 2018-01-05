"""
Name: Aditya Krishna Yerraguntla Kumar

Date: 01/05/17

Description: a twitter bot that uses the reddit api to get the
             top jokes from /r/dadjokes and then tweets one out
             every single day
"""
#Dependencies

#used for talking to twitter
import tweepy

#used for talking to reddit
import praw

#local module that holds all of the keys for the apis
import keys

#used for making the code sleep
import time



def getJokes ():
    #accesses the bot
    redditBot = praw.Reddit(client_id = keys.redditID, client_secret = keys.redditsecret,
                        password = keys.password, user_agent = "test script",
                        username = keys.userName)

    twoDList = []

    subreddit = redditBot.subreddit('dadjokes')

    for submission in subreddit.hot(limit = 10):

        title = submission.title
        post = submission.selftext

        twoDList.append([title, post])

    return twoDList


def tweetJoke():
    jokes = getJokes()

    auth = tweepy.OAuthHandler(keys.twitterKey, keys.twitterSecret)
    auth.set_access_token(keys.twitterAccess,keys.twitterAccessSecret)
    bot = tweepy.API(auth)
    title = jokes[0][0]
    joke = jokes[0][1]


    bot.update_status(title +"\n"+ joke)
    time.sleep(86400)



def main():
    while True:
        tweetJoke()

main()