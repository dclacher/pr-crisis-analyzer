# Search class handle different kinds of search
import tweepy
from tweepy import OAuthHandler
import pandas
import sys
import json


class SearchATweetAndItsReplies:
    """
    After claim SearchATweetAndItsReplies Class, initialize it will necessary information
    Call the search_latest_tweet_and_its_replies() function to get the latest tweet and its replies
    Using the_latest_tweet() function and self.replies (tuple) attribute to get the data.
    """

    def __init__(self):
        """
        Constructor
        """
        self._api = None  # api to access tweet search engine
        self._tweet_id_str = None  # please use string instead big int to stay safe.(id_str)
        self._target_str = None  # the targeted user.
        # NEEDIMPROVE: default tweets_count is 5, we need to try to make it larger to get more result.
        self._tweets_count = 5  # control the number of tweet we want in search function.
        '''
        Below is data
        '''
        self._the_latest_tweet = None  # the latest tweet.
        # NEEDIMPROVE: private? public? getter? setter? robust?
        self.replies = []  # the set of replies
        """
        in_reply_to_status_id_str: 
        Nullable. If the represented Tweet is a reply, this field will contain the string representation of the original Tweet’s ID.
        """

    def initialize(self, api, target_str, tweets_count=5):
        """
        initialize the search function
        :param tweets_count: The number of replies we want to get
        :param api: The authorization we need to use tweet api
        :param target_str: the user we are targeting
        :return:
        """
        self._get_api(api)
        self._get_target_str(target_str)
        self.tweets_count(tweets_count)

    def _get_api(self, api=None):
        """
        Getter and setter of _api which is used to access Tweet service
        :param api:
        :return:
        """
        if isinstance(api, tweepy.API):
            self._api = api
        return self._api

    def _get_tweet_id_str(self, tweet_id_str=None):
        """
        Getter and setter of _tweet_id_str which is used to access re-tweet
        :param tweet_id_str:
        :return:
        """
        if isinstance(tweet_id_str, str):
            self._tweet_id_str = tweet_id_str
        return self._tweet_id_str

    def _get_target_str(self, target_str=None):
        """
        Getter and setter of _target_str which is used in q
        :param target_str:
        :return:
        """
        # FIXME: Need to find a way to regulate '_target_str' "@noradio"
        if isinstance(target_str, str):
            self._target_str = target_str
        return self._target_str

    def the_latest_tweet(self, the_latest_tweet=None):
        """
        Getter and setter of the latest tweet
        :param the_latest_tweet:
        :return:
        """
        # FIXME: Need to find a way to regulate '_the_latest_tweet'
        if the_latest_tweet is not None:
            self._the_latest_tweet = the_latest_tweet
        return self._the_latest_tweet

    def tweets_count(self, tweets_count=None):
        """
        Getter and setter of the number of tweet we want in search function.
        :param tweets_count:
        :return:
        """
        if isinstance(tweets_count, int):
            self._tweets_count = tweets_count
        return self._tweets_count

    def search_latest_tweet_and_its_replies(self):
        """
        The Search function, search for the latest tweet first, and then search its replies
        :return:
        """
        self._search_the_latest_tweet()
        self._search_replies_of_the_tweet()

    def _search_the_latest_tweet(self):  # search the latest tweet of our target user. (private)
        if (self._get_api() is not None) & (
                self._get_target_str() is not None):  # we need api to access search, target_str to target user.
            # FIXME: Consider the retweet situation!
            # FIXME: Consider the reply situation!
            # FIXME: Some Serious Error Happened About RETWEET!!
            # FIXME: EXCEPTION HANDLING
            tweets = self._get_api().user_timeline(id=self._get_target_str(),
                                                   count=1)  # Search for the latest tweet of the target user from his/her user timeline.
            if tweets:
                for the_tweet in tweets:
                    self.the_latest_tweet(the_tweet)  # set the tweet
                    self._get_tweet_id_str(the_tweet.id_str)  # set tweet_id_str
                    # NEEDIMPROVE: more potential operation related to the tweet.
            return tweets
        return None

    def _search_replies_of_the_tweet(self):  # search the replies of the latest tweet of our target user. (private)
        if (self._get_api() is not None) & (self._get_tweet_id_str() is not None) & (
                self._get_target_str() is not None) & (
                self.tweets_count() is not None):  # check the information we need to search.
            # FIXME: EXCEPTION HANDLING
            tweets = self._get_api().search(q=f'to:{self._get_target_str()}', since_id=self._get_tweet_id_str(),
                                            result_type='popular',
                                            count=self.tweets_count())  # search tweets that to the target user, id bigger than the tweet's id, and the result is recent.
            for tweet in tweets:
                if not hasattr(tweet, 'in_reply_to_status_id_str'):  # skip those are non replies
                    continue
                if tweet.in_reply_to_status_id_str == self._get_tweet_id_str():  # check if it is the specific tweet's replies.
                    self.replies.append(tweet)  # put the replies in to a tuple


consumer_key = 'pCQZGN989DvXFuzECpj0XPnBM'
consumer_secret = 'R0O6UP86HyiJ36pqD8WpLjXKH0b0ChKa4Y4b4fOuPjeNpAON5z'
access_token = '1217182018339057664-pPTx8umK3LIWzMEmqsQJotldstsj1S'
access_secret = 'JCMAD6ubDQXfAezlXlaQzNDCIHxPZU0DoZzod2xo8D4Ln'


# TEST: for test. SUCCESS
def main():
    s = SearchATweetAndItsReplies()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    # TEST: test start. SUCCESS
    s.initialize(api, '@realDonaldTrump')
    s.search_latest_tweet_and_its_replies()
    print('Original Tweet: ')
    print(s.the_latest_tweet())
    print('The Replies: ')
    # print(s.replies)
    for t in s.replies:
        print(t)


if __name__ == '__main__':
    main()
