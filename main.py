import tweepy
from other import keys


def api():
    auth = tweepy.OAuthHandler(keys.api_key, keys.api_key_secret)
    auth.set_access_token(keys.access_token, keys.access_token_secret)

    return tweepy.API(auth)


def tweet(api: tweepy.API, message: str, image_path=None):
    if image_path:
        api.update_status_with_media(message, image_path)
    else:
        api.update_status(message)

    print('Tweeted successfully!')


if __name__ == 'main':
    api = api()
    tweet(api, 'This was tweeted from Python')