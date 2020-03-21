from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

def extract_retweeters(file):
  lst = []
  with open(file, 'r') as inptr:
    for line in inptr:
      lst.append(line.rstrip())
  return lst

def init_browser():
  login_url = "https://www.twitter.com/login"
  driver = webdriver.Firefox()
  driver.get(login_url)

  driver = authenticate(driver)
  time.sleep(1)
  return driver

def authenticate(driver):
  input("Press any key after logging in.")
  return driver

def tweet_at(driver, message):
  driver.get('https://twitter.com/compose/tweet')

  autotw1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'DraftEditor-root')))
  autotw1.click()

  element = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CLASS_NAME, 'public-DraftEditorPlaceholder-root')))
  ActionChains(driver).move_to_element(element).send_keys(message).perform()

  time.sleep(1)
  tweet = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='css-901oao css-16my406 css-bfa6kz r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0']//span[@class='css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0'][contains(text(),'Tweet')]")))
  # tweet.click()

def main():
  driver = init_browser()

  retweeter_file = 'test.txt'
  message_content = 'Testing out my new Twitter agent.'
  retweet_at_list = extract_retweeters(retweeter_file)

  for (i, to_tweet) in enumerate(retweet_at_list):
    print("At = ", to_tweet)
    tweet_at(driver, '@' + to_tweet + ' ' + message_content)
    
    if(i % 10 == 0):
      ans = input("Keeping tweeting? (Y/N)")
      if (ans == 'y' or ans == 'Y'):
        continue
      else:
        break
        
	driver.quit()

if __name__ == '__main__':
	main()