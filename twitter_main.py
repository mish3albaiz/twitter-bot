import random
import time
import tweepy
import loginfo
import map_imager
import subprocess

consumer_key = loginfo.consumer_key # get api tokens
consumer_secret = loginfo.consumer_secret
access_token = loginfo.access_token
access_token_secret = loginfo.access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) # auth and access
auth.set_access_token(access_token, access_token_secret)

# method to tweet out pdxpolicelog's tweets with location
def pdxpolicelog_tweet():
    api = tweepy.API(auth) # get api instance
    public_tweets = [] # tweets by user's public timeline
    public_tweets = api.user_timeline(screen_name="pdxpolicelog") # get last 20 tweets
    last_tweet_file = open('last_tweet_pdx.txt') # open last self tweet that was saved
    saved_last_tweet = last_tweet_file.read() # read text
    last_tweet_file.close() # close file
    tweet_num = 0 # last tweet index number in current tweets
    last_tweet = "" # set last tweet to empty
    for tweet in public_tweets: # iterate through last 20 tweets
        if(saved_last_tweet == tweet.text): # if tweet matches saved tweet
            if(tweet_num == 0): # if it is the most recent tweet
                last_tweet = public_tweets[tweet_num] # set last tweet
                break # exit loop
            else: # if it is not most recent tweet
                last_tweet = public_tweets[tweet_num-1] # set it to the tweet after that
                break # exit loop
        else: # if it does not match the saved tweet
            if(tweet_num == 19): # save it if it is the 20th tweet
                last_tweet = public_tweets[tweet_num] # set last tweet
                break # exit
            else: # if it is under the 20th tweet
                tweet_num = tweet_num + 1 # add 1 to tweet number

    public_tweets = [] # clear last 20 tweets
    last_tweet_text = last_tweet.text # get last tweet text

    if(last_tweet_text != saved_last_tweet): # if the last tweet is not the saved tweet
        location = last_tweet_text.split(" at ", 1)[1] # get location street
        location = location.split(", PORT", 1)[0] # remove city from string
        location = location.replace(" ", "+") # replace spaces with + for google api
        location = location + ",+PORTLAND,+OR" # add city and state for google api
        try: # try to get map image and tweet
            map_imager.map_image(location) # create map image
            time.sleep(5) # wait 5 seconds
            # tweet out image and text
            last_tweet_text = last_tweet_text.strip("amp;")
            composed_tweet = last_tweet_text + " #portland #pdx #oregon"
            api.update_with_media(filename="/home/meshal/Desktop/twootter/map.png", status=composed_tweet)
        except:
            # failed to tweet
            print("Error while tweeting")
        last_tweet_file_write = open('last_tweet_pdx.txt', 'w') # save last tweeted tweet
        last_tweet_file_write.write(last_tweet_text)
        last_tweet_file_write.close()
    else: # if tweet is same as most recent then do nothing
        time.sleep(1)

def multpolicelog_tweet():
    api = tweepy.API(auth) # get api instance
    public_tweets = [] # tweets by user's public timeline
    public_tweets = api.user_timeline(screen_name="pdxsherrifflog") # get last 20 tweets
    last_tweet_file = open('last_tweet_mult.txt') # open last self tweet that was saved
    saved_last_tweet = last_tweet_file.read() # read text
    last_tweet_file.close() # close file
    tweet_num = 0 # last tweet index number in current tweets
    last_tweet = "" # set last tweet to empty
    for tweet in public_tweets: # iterate through last 20 tweets
        if(saved_last_tweet == tweet.text): # if tweet matches saved tweet
            if(tweet_num == 0): # if it is the most recent tweet
                last_tweet = public_tweets[tweet_num] # set last tweet
                break # exit loop
            else: # if it is not most recent tweet
                last_tweet = public_tweets[tweet_num-1] # set it to the tweet after that
                break # exit loop
        else: # if it does not match the saved tweet
            if(tweet_num == 19): # save it if it is the 20th tweet
                last_tweet = public_tweets[tweet_num] # set last tweet
                break # exit
            else: # if it is under the 20th tweet
                tweet_num = tweet_num + 1 # add 1 to tweet number

    public_tweets = [] # clear public tweets
    last_tweet_text = last_tweet.text # get last tweet text

    if(last_tweet_text != saved_last_tweet): # if the last tweet is not the saved tweet
        location = last_tweet_text.split(" at ", 1)[1] # get location street
        location = location.split(", GRSM", 1)[0] # remove city from string
        location = location.replace(" ", "+") # replace spaces with + for google api
        location = location + ",+GRESHAM,+OR" # add city and state for google api
        try: # try to get map image and tweet
            map_imager.map_image(location) # create map image
            time.sleep(5) # wait 5 seconds
            # tweet out image and text
            last_tweet_text = last_tweet_text.strip("amp;")
            composed_tweet = last_tweet_text + " #gresham #pdx #oregon"
            api.update_with_media(filename="/home/meshal/Desktop/twootter/map.png", status=composed_tweet)
        except:
            # failed to tweet
            print("Error while tweeting")
        last_tweet_file_write = open('last_tweet_mult.txt', 'w') # save last tweeted tweet
        last_tweet_file_write.write(last_tweet_text)
        last_tweet_file_write.close()
    else: # if tweet is same as most recent then do nothing
        time.sleep(1)


pdxpolicelog_tweet()
time.sleep(10)
multpolicelog_tweet()
time.sleep(10)
