
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

starttime = time.time()

while True:
        
        response = requests.get('https://www.hackensackmeridianhealth.org/covid19/')
        doc = html.fromstring(response.content)
        first_dose = doc.xpath('//*[@id="pagealertVaccineStats"]/text()[1]')[0]
        fully_vaxxed = doc.xpath('//*[@id="pagealertVaccineStats"]/text()[2]')[0]
        total_vax = doc.xpath('//*[@id="pagealertVaccineStats"]/text()[3]')[0]
        last_updated = doc.xpath('//*[@id="pagealertVaccineStats"]/small')[0].text
        
        tweet = f'''Total Vaccines Administered at HMH:\n%s%s%s\n%s\n\n\n#COVID #NewJersey #CoronavirusUpdates #NJ #MonmouthCounty''' %(first_dose,fully_vaxxed,total_vax,last_updated)
        the_twitter_api.update_status(status=tweet)
        
        
        time.sleep(86400 - ((time.time() - starttime) % 60.0))