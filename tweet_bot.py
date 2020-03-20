import tweepy 

#bhavtosh_app_5:
consumer_key="cUG1EhS3j1A90sNXH5kgAQMS8"
consumer_secret="1Z8YZliuYxSZekkX1S1gptLgNo4YMwNqjfBlz555ekb08UEsG2"
access_key="2878920982-nFblRgI8msBrOKcr1rDL8uzrCwKaTkHBCbM3OBV"
access_secret="a2gp3sI5zMvshmwVQR25cmiY13NUP8rH0tqOfTbSuzEW0"

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

# import tweepy 

# def extract_retweeters(file):
#   lst = []
#   with open(file, 'r') as inptr:
#     for line in inptr:
#       lst.append(line.rstrip())
#   return lst

# def tweet_at(api, user, message):
#   # update the status 
#   api.update_status(status = "@" + str(user) + " " + message) 

# def authenticate(consumer_key, consumer_secret, access_key, access_secret):
#   # authentication of consumer key and secret 
#   auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
    
#   # authentication of access token and secret 
#   auth.set_access_token(access_key, access_secret) 
#   return tweepy.API(auth) 

# def read_api_keys(file_name):
#   keys = []
#   with open(file_name, 'r') as inptr:
#     while True:
#       comment = inptr.readline()
#       consumer_key = inptr.readline().lstrip('consumer_key=').rstrip('\n')
#       consumer_secret = inptr.readline().lstrip('consumer_secret=').rstrip('\n')
#       access_key = inptr.readline().lstrip('access_key=').rstrip('\n')
#       access_secret = inptr.readline().lstrip('access_secret=').rstrip('\n')
#       blank_line = inptr.readline()

#       if (not comment): ### EOF
#         break

#       keys.append([consumer_key, consumer_secret, access_key, access_secret])
#   return keys

# def set_up_keys():
#   keys = read_api_keys("api_keys")
#   for i in range(len(keys)):
#     keys[i] = authenticate(keys[i][0], keys[i][1], keys[i][2], keys[i][3])
#   return keys

# def main():
#   retweeter_file = 'test.txt'
#   message_content = 'You have been flagged as a bot by our newT witter agent.'
#   retweet_at_list = extract_retweeters(retweeter_file)

#   apis = set_up_keys()
#   count = 0
#   api_counter = 0
#   for user in retweet_at_list[:2]:
#     print("Tweet counter = ", count)
#     count += 1
#     tweet_at(apis[api_counter], user, message_content)
#     api_counter = (api_counter + 1) % len(apis)

# if __name__ == '__main__':
# 	main()