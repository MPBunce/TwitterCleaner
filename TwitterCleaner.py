import tweepy
import os
import math

#Enviormental Variables Set up in .env file 
from dotenv import load_dotenv
load_dotenv()

#Importing from .env file
API_KEY = os.getenv("API_KEY")
API_KEY_SECRET = os.getenv("API_KEY_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
BEARBER_TOKEN = os.getenv("BEARBER_TOKEN")


print('\n')
print('Welcome to the twitter scrubber!')
print('\n')
print('API_KEY =', API_KEY)
print('API_KEY_SECRET =', API_KEY_SECRET)
print('ACCESS_TOKEN =', ACCESS_TOKEN)
print('ACCESS_TOKEN_SECRET =', ACCESS_TOKEN_SECRET)
print('\n')

auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)


#Checking these are the right keys



char = input('Please confirm these are your API keys and access tokens (y/n):')
if char == 'y':


    #Checking the keys are correct and that the user wants to scrub their twitter account
    charTwo = input('Are you sure you want to scrub your twitter account clean? (y/n):')
    if charTwo == 'y':

        #User confirmed they want to scrub their twitter account, lets start!
        print('\nOkay here we go!\n')

        timeline = tweepy.Cursor(api.user_timeline).items()
        favorites = tweepy.Cursor(api.get_favorites).items()

        if api.verify_credentials() == False:
            print("The user credentials are invalid!\n")
        else:
            print("The user credentials are valid!\n") 


        #call delete function

        print("Fetching Tweets")

        for tweet in timeline:
            api.destroy_status(tweet.id)
            if timeline == None:
                break


        print("Deleted Tweets")

        #call delete likes

        print("Fetching Favourites")
        for tweet in favorites:
            api.destroy_favorite(tweet.id)      
            if favorites == None:
                break

        print("Deleted Likes")


    else:
        print('\nEither you have entered something incorrently or selected no\nGoodbye!\n')
        quit

else:
    print('\nEither you have entered something incorrently or your API keys and Bearber Token are wrong. Edit your .env file and restart the program :)')
    print('Goodbye!')
    print('\n')

