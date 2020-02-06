import tweepy 

# # personal details 
# consumer_key ="xxxxxxxxxxxxxxxx"
# consumer_secret ="xxxxxxxxxxxxxxxx"
# access_token ="xxxxxxxxxxxxxxxx"
# access_token_secret ="xxxxxxxxxxxxxxxx"
  
def extract_retweeters(file):
  lst = []
  with open(file, 'r') as inptr:
    for line in inptr:
      lst.append(line.rstrip())
  return lst

def tweet_at(api, user, message):
  # update the status 
  api.update_status(status = "@" + str(user) + " " + message) 

def authenticate():
  # authentication of consumer key and secret 
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
    
  # authentication of access token and secret 
  auth.set_access_token(access_key, access_secret) 
  return tweepy.API(auth) 

def main():
  retweeter_file = 'test.txt'
  message_content = 'Testing out my new Twitter agent.'
  retweet_at_list = extract_retweeters(retweeter_file)

  api = authenticate()
  for user in retweet_at_list:
    tweet_at(api, user, message_content)

if __name__ == '__main__':
	main()