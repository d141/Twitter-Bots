# Import the python libraries we need to 
import sys
import tweepy
import time
import requests
from lxml import html


## Authentication Boilerplate

# Be sure to paste your keys and tokens in here because it won't work otherwise!
CONSUMER_KEY="uxfFn89c4FHD8Vu6T0CX6fVA4"
CONSUMER_SECRET= "DxKxcfQbacm5OuFiXD7UD6QKrMS2BDLV9YMNb4MqaovZSfjCBE"
ACCESS_KEY = "1355940286413893634-dQP4MF4ChA2d6XBX0ASpXErI5vfwcT"
ACCESS_SECRET = "gaaHLCRQZ8c6T959PpdD2bxB5rraeW8vNIj3HEgy9gTla"


# Send our keys and tokens to Twitter
credentials = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
credentials.set_access_token(ACCESS_KEY, ACCESS_SECRET)

# Authenticate with Twitter to get access
the_twitter_api = tweepy.API(credentials)


def get_current_hack():
    response = requests.get('https://www.hackensackmeridianhealth.org/covid19/')
    doc = html.fromstring(response.content)
    current_hack = doc.xpath('//*[@id="main"]/section[2]/div/div[1]/div[1]/h3')[0].text
    return current_hack

def get_current_ohi():
    response = requests.get('https://ohinj.org/vaccine-consent-landing/')
    doc = html.fromstring(response.content)
    current_ohi = doc.xpath('//*[@id="fl-post-2362"]/div/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div/div/p[14]/span/text()')[0]
    return current_ohi
    
def create_tweet_hack():
    tweet = f'''Hackensack Meridian has updated their website.
    Please visit https://www.hackensackmeridianhealth.org/covid19/'''
    the_twitter_api.update_status(status=tweet)
    print("I tweeted about HM")

def create_tweet_hack():
    tweet = f'''Ocean Health Initiative has updated their website.
    Please visit https://ohinj.org/vaccine-consent-landing/'''
    the_twitter_api.update_status(status=tweet)
    print("I tweeted about OHI")

current_hack=get_current_hack()
current_ohi=get_current_ohi()
starttime = time.time()

while True:
    
    response = requests.get('https://www.hackensackmeridianhealth.org/covid19/')
    doc = html.fromstring(response.content)
    now_current_hack = doc.xpath('//*[@id="main"]/section[2]/div/div[1]/div[1]/h3')[0].text
    if now_current_hack != current_hack:
        create_tweet_hack()
        current_hack=now_current_hack
        
    response = requests.get('https://ohinj.org/vaccine-consent-landing/')
    doc = html.fromstring(response.content)
    now_current_ohi = doc.xpath('//*[@id="fl-post-2362"]/div/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div/div/p[14]/span/text()')[0]
    if now_current_ohi != current_ohi:
        create_tweet_ohi()
        current_ohi=now_current_ohi
    
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))

