import tweepy
import getTweets
import random
import json
import pdb
from credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# runs the main function from getTweets which sets up the dictionary
##getTweets.main()

with open("dict.json", "r") as read_file:
	dict = json.load(read_file)


def getWordChain(lastWord, dict): ##generate function not producing anyuthing
	## pdb.set_trace()
	result = lastWord

	while lastWord in dict:
		# first find the sum of all the possibilities
		sum = 0
		for word in dict[lastWord]:
			sum += dict[lastWord][word]

		# generate a random number from 1 to that sum
		rand = random.randint(1, sum)

		# subtract the frequency from that random number. If it's < 1 then select it
		for word in dict[lastWord]:
			if rand - dict[lastWord][word] < 1:
				result = result + ' ' + word
				lastWord = word
				break
			else:
				rand = rand - dict[lastWord][word]

	return result


def generateTweet():

	startword = random.choice(list(dict.keys()))
	sentence = getWordChain(startword, dict)
	api.update_status(sentence)


def main():
	generateTweet()


main()
