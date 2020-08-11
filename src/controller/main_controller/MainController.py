# NEEDIMPROVE: need to rearrange the imports
import json

from src.twitter.authentication.TwitterAPIAuthentication import TwitterAPIAuthentication
from src.twitter.search.search import Search
# FIXME: Same name as .py file in watson API!
from src.watson.tone_analysis.tone_analysis import ToneAnalysis


class MainController:
    def __init__(self):
        self._screen_name = ''
        self._tone_analysis_result = None

    def get_screen_name(self, screen_name=None):
        """
        Getter and Setter of _screen_name
        :param screen_name:
        :return:
        """
        # FIXME: Need a way to regulate _consumer_key
        if screen_name:
            self._screen_name = screen_name
        try:
            return self._screen_name
        except AttributeError:
            return None

    def _set_tone_analysis_result(self, tone_analysis_result=None):
        """
        Getter and Setter of _tone_analysis_result
        :param tone_analysis_result:
        :return:
        """
        # FIXME: Need a way to regulate _tone_analysis_result
        if tone_analysis_result:
            self._tone_analysis_result = tone_analysis_result
        try:
            return self._tone_analysis_result
        except AttributeError:
            return None

    def get_tone_analysis_result(self):
        # Get Data from twitter part.
        # initialize Twitter API Authenticator
        twitterAPIAuthentication = TwitterAPIAuthentication()
        # get twitter API Handle
        twitterAPIHandle = twitterAPIAuthentication.get_authentication()
        # claim and initialize Search class with twitterAPIHandle and screen name(target)
        search = Search()
        search.initialize(twitterAPIHandle, self.get_screen_name())
        # get results
        results = search.search_a_tweet_and_its_replies()
        # TEST: Print original tweet and it's replies
        # print(results[0])
        # print(results[1])
        # for t in results[1]:
        #     print(t.text)
        # print('-----Twitter API Done-----')

        # Twitter part done.
        # Process the data(Very Sample)
        text = ''
        for t in results[1]:
            text += (t.text + '\n')

        # Throw an exception if there is no replies(no data to analysis).
        if text == '':
            raise Exception('There is no replies got.')

        # Process the data done
        # Tone Analysis
        # initialize Tone Analysis Authenticator
        toneAnalysis = ToneAnalysis()
        # analysis text
        toneAnalysis.tone_analysis_by_str(text)
        # get result
        result = toneAnalysis.get_tone_analysis_result()
        # set result(private)
        self._set_tone_analysis_result(result)
        # try to return result(not null)
        if result:
            self._tone_analysis_result = result
        try:
            return self._tone_analysis_result
        except AttributeError:
            return None


def controller():
    """
    Demonstrate the process of data flow.
    :return:
    """
    # Get Data from twitter part.
    a = TwitterAPIAuthentication()
    api = a.get_authentication()
    s = Search()
    s.initialize(api, '@realDonaldTrump')
    r = s.search_a_tweet_and_its_replies()
    print(r[0])
    print(r[1])
    for t in r[1]:
        print(t.text)
    print('-----Twitter API Done-----')
    # Twitter part done.
    # Process the data(Very Sample)
    text = ''
    for t in r[1]:
        text += (t.text + '\n')
    # Throw an exception if there is no replies(no data to analysis).
    if text == '':
        raise Exception('There is no replies got.')
    # Process the data done
    # Tone Analysis
    Ta = ToneAnalysis()
    Ta.tone_analysis_by_str(text)
    result = Ta.get_tone_analysis_result()
    # Tone Analysis Done
    # Display result
    json_result = json.dumps(result, indent=2)
    #print(json.dumps(result, indent=2))
    print(result)
    for r in result["sentences_tone"]:
        print(r["text"])
        for r2 in r["tones"]:
            print(r2["tone_name"])
        print("123123123123")



if __name__ == '__main__':
    controller()
