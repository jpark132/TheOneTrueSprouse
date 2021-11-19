import tweepy
import re
import json
import os

# Import our Twitter credentials from credentials.py
from credentials import *

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

names = ['colesprouse', 'dylansprouse']
alltweets = []
dict = {}

def create_dict(alltweets):
	for tweet in alltweets:
		for i in range(0, len(tweet) - 1):
			if '@' in tweet[i] or 'http' in tweet[i]:
				continue

			if '@' in tweet[i+1] or 'http' in tweet[i+1]:
				continue
				
			curr = tweet[i]
			next = tweet[i+1]

			# if not in the dictionary at all
			if curr not in dict:
				dict[curr] = {next: 1}
			else:

				# if the root word is in but there is a new next word
				if next not in dict[curr]:
					dict[curr][next] = 1

				else:
					# if there is already that combination just increment
					dict[curr][next] = dict[curr][next] + 1


# get the tweets and add to alltweet list
def get_tweets(name):
	for tweet in tweepy.Cursor(api.user_timeline, id=name).items():
		data = str(tweet.text)
		data = data.split(" ")
		alltweets.append(data)


def updateJSON(filename, dict):
	file = open(filename, "w")
	json.dump(dict, file)
	file.close()


def main():
	# deleting old dict to get up to date tweets
	if os.path.exists("dict.json"):
		os.remove("dict.json")

	# getting tweets for both dylan and cole sprouse
	print("getting tweets")
	get_tweets('dylansprouse')
	get_tweets('colesprouse')

	# creating the dictionary and then updating the json file
	create_dict(alltweets)
	updateJSON("dict.json", dict)

main()