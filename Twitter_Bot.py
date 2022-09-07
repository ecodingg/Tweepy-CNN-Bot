#Made by Ethan Doss-Fillmore for educational and personal purposes
from Tweepy import tweet
from selenium import webdriver

print("Tweeting...")


url = "https://www.cnn.com/europe/live-news/russia-ukraine-war-news-05-04-22/index.html"
browser = webdriver.Firefox()
newUrl = browser.get(browser.refresh(url))

text = "The current situation according to CNN: {url}".format(url=newUrl)

tweet(text)

print("Done!")
