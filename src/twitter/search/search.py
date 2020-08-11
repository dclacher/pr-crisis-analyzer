# Search class handle different kinds of search
import tweepy

# NEEDIMPROVE: Need to adjust structure in the future.
from tweepy import OAuthHandler

from src.twitter.authentication.TwitterAPIAuthentication import TwitterAPIAuthentication
from src.twitter.search import search_a_tweet_and_its_replies

from src.twitter.search.search_a_tweet_and_its_replies import SearchATweetAndItsReplies


# FIXME & NEEDIMPROVE: Restructure the class, it doesn't feel right
class Search:
    """
    After claim the class, initialize it with the necessary information
    Call the search_a_tweet_and_its_replies function to get result and return it.
    The result will be store as tuple.
    """

    def __init__(self):
        """
        Constructor
        """
        self._api = None  # api to access tweet search engine
        self._target_user_str = None  # the targeted user.
        self.results_tuple = []  # the results
        '''
        Below is Specific Search Objects
        '''
        self._search_a_tweet_and_its_replies = None  # the class that handle search one tweet and its replies

    def initialize(self, api, target_str):
        self.get_api(api)
        self.get_target_str(target_str)

    def get_api(self, api=None):
        """
        Getter and setter of _api which is used to access Tweet service
        :param api:
        :return:
        """
        if isinstance(api, tweepy.API):
            self._api = api
        return self._api

    def get_target_str(self, target_user_str=None):
        """
        Getter and setter of _target_user_str which is used in search
        :param target_user_str:
        :return:
        """
        # FIXME: Need to find a way to regulate '_target_str' "@noradio"
        if isinstance(target_user_str, str):
            self._target_user_str = target_user_str
        return self._target_user_str

    def get_search_a_tweet_and_its_replies(self, the_search_a_tweet_and_its_replies=None):
        """
        Getter and setter of search_a_tweet_and_its_replies which is used to access Tweet service
        :param the_search_a_tweet_and_its_replies:
        :return:
        """
        if isinstance(the_search_a_tweet_and_its_replies, SearchATweetAndItsReplies):
            self._search_a_tweet_and_its_replies = the_search_a_tweet_and_its_replies
        return self._search_a_tweet_and_its_replies

    def search_a_tweet_and_its_replies(self):
        """
        Search a tweet and its replies function
        :return:
        """
        # Initialize the specific search object
        self.get_search_a_tweet_and_its_replies(SearchATweetAndItsReplies())
        self.get_search_a_tweet_and_its_replies().initialize(self.get_api(), self.get_target_str())
        # Start a specific search
        self.get_search_a_tweet_and_its_replies().search_latest_tweet_and_its_replies()
        the_tweet = self.get_search_a_tweet_and_its_replies().the_latest_tweet()
        replies = self.get_search_a_tweet_and_its_replies().replies
        # Form the result set
        self.results_tuple.append(the_tweet)
        self.results_tuple.append(replies)
        return self.results_tuple


consumer_key = 'pCQZGN989DvXFuzECpj0XPnBM'
consumer_secret = 'R0O6UP86HyiJ36pqD8WpLjXKH0b0ChKa4Y4b4fOuPjeNpAON5z'
access_token = '1217182018339057664-pPTx8umK3LIWzMEmqsQJotldstsj1S'
access_secret = 'JCMAD6ubDQXfAezlXlaQzNDCIHxPZU0DoZzod2xo8D4Ln'


# TEST: for test SUCCESS
def main():
    a = TwitterAPIAuthentication()
    api = a.get_authentication()
    s = Search()
    # TEST: test start SUCCESS
    s.initialize(api, '@realDonaldTrump')
    r = s.search_a_tweet_and_its_replies()
    print('Original Tweet')
    print(r[0])
    print('Collection of replies')
    print(r[1])
    print('Each reply text')
    for t in r[1]:
        print(t.text)
    print('--------------------------------------------------')
    x = 0
    for i in range(10000000):
        x = x + 2
    ss = Search()
    ss.initialize(api, '@youtubemusic')
    rr = ss.search_a_tweet_and_its_replies()
    print('Original Tweet')
    print(rr[0])
    print('Collection of replies')
    print(rr[1])
    print('Each reply text')
    for t in rr[1]:
        print(t.text)


if __name__ == '__main__':
    main()
