import tweepy
from tweepy import OAuthHandler, TweepError


# FIXME: Rename the getter and setter function
# FIXME: ADD Exception Handling
class TwitterAPIAuthentication:

    def __init__(self):
        """
        Constructor
        """
        self._consumer_key = 'pCQZGN989DvXFuzECpj0XPnBM'
        self._consumer_secret = 'R0O6UP86HyiJ36pqD8WpLjXKH0b0ChKa4Y4b4fOuPjeNpAON5z'
        self._access_token = '1217182018339057664-pPTx8umK3LIWzMEmqsQJotldstsj1S'
        self._access_secret = 'JCMAD6ubDQXfAezlXlaQzNDCIHxPZU0DoZzod2xo8D4Ln'
        self._auth = None
        self._api = None

    def get_authentication(self):
        """Get Tweepy API to access Twitter"""
        try:
            # NEEDIMPROVE: need to improve the way of setting auth.
            self._auth = OAuthHandler(self._consumer_key, self._consumer_secret)
            self._auth.set_access_token(self._access_token, self._access_secret)
            self.get_api(tweepy.API(self.get_auth(), wait_on_rate_limit=True))
        except TweepError as e:
            print(e.__str__())
            pass
        return self.get_api()

    def consumer_key(self, consumer_key=None):
        """
        Getter and Setter of _consumer_key
        :param consumer_key:
        :return:
        """
        # FIXME: Need a way to regulate _consumer_key
        if consumer_key:
            self._consumer_key = consumer_key
        try:
            return self._consumer_key
        except AttributeError:
            return None

    def consumer_secret(self, consumer_secret=None):
        """
        Getter and Setter of _consumer_secret
        :param consumer_secret:
        :return:
        """
        # FIXME: Need a way to regulate _consumer_secret
        if consumer_secret:
            self._consumer_secret = consumer_secret
        try:
            return self._consumer_secret
        except AttributeError:
            return None

    def access_token(self, access_token=None):
        """
        Getter and Setter of _access_token
        :param access_token:
        :return:
        """
        # FIXME: Need a way to regulate _access_token
        if access_token:
            self._access_token = access_token
        try:
            return self._access_token
        except AttributeError:
            return None

    def access_secret(self, access_secret=None):
        """
        Getter and Setter of _access_secret
        :param access_secret:
        :return:
        """
        # FIXME: Need a way to regulate _access_secret
        if access_secret:
            self._access_secret = access_secret
        try:
            return self._access_secret
        except AttributeError:
            return None

# DEBUG: delete this comment after success
    def get_auth(self, auth=None):
        """
        Getter and Setter of _auth
        :param auth:
        :return:
        """
        # FIXME: Find a way to regulate auth(OAuthHandler)
        if auth:
            self._auth = auth
        try:
            return self._auth
        except AttributeError:
            return None

    def get_api(self, api=None):
        """
        Getter and setter of _api which is used to access Tweet service
        :param api:
        :return:
        """
        if isinstance(api, tweepy.API):
            self._api = api
        return self._api


def main():
    a = TwitterAPIAuthentication()


if __name__ == '__main__':
    main()
