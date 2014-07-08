from twython import Twython

APP_KEY,APP_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET='xxxx','xxxx','xxxx','xxxx'

twitter=Twython(APP_KEY,APP_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
twitter.get_home_timeline()
photo = open(PATH_TO_MEDIA, 'rb')
twitter.update_status_with_media(status=" ...... ", media=photo)
