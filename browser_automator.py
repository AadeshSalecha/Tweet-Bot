from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

twitter_username = Enter Username
twitter_password = Enter Password 

def main():
  login_url = "https://www.twitter.com/login"
  driver = webdriver.Firefox()
  driver.get(login_url)

  driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input').send_keys(twitter_username)
  driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input').send_keys(twitter_password)
  driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[3]/div/div').click()

  time.sleep(10)


  body = driver.find_element_by_tag_name("body")
  body.send_keys(Keys.CONTROL + 't')
  driver.get("http://stackoverflow.com/")

	# driver.quit()

if __name__ == '__main__':
	main()