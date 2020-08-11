# NEEDIMPROVE: rearrange the imports
from ibm_cloud_sdk_core.authenticators import *
from ibm_watson.tone_analyzer_v3 import *

from src.watson.authentication.tone_analysis_authentication import ToneAnalysisAuthentication


class ToneAnalysis:
    # FIXME: Need to find a way to use json or other type of data as data source
    """
    After claim the class, authentication is given automatically(Only for prototype, time limit)
    Call tone_analysis_by_str(str) function to analysis the string or multi-line string
    Right now, only achieved using string as input data source to analysis.
    """

    def __init__(self):
        """
        Constructor
        """
        # FIXME: Need to find a better way to give authentication!
        self._authentication = ToneAnalysisAuthentication()  # Get authentication to access API
        self._tone_analysis_result = None  # result object

    def get_authentication(self, authentication=None):
        """
        Getter and Setter of _authentication
        :param authentication: new authentication
        :return:
        """
        if isinstance(authentication, ToneAnalysisAuthentication):
            self._authentication = authentication
        return self._authentication

    def tone_analysis_by_str(self, str):
        """
        Use tone() function to analysis tone.
        :param str: use a string that contain multi-line as data source (temporary)
        :return:
        """
        self.get_tone_analysis_result(self.get_authentication().get_tone_analyzer().tone({'text': str},
                                                                                         content_type='application/json').get_result())

    def get_tone_analysis_result(self, tone_analysis_result=None):
        """
        Getter and Setter of _tone_analysis_result
        :param tone_analysis_result:
        :return:
        """
        # FIXME: Need a way to regulate _tone_analysis_result
        if tone_analysis_result:
            self._tone_analysis_result = tone_analysis_result
        return self._tone_analysis_result


def main():
    # TEST test data SUCCESS
    text = 'Team, I know that times are tough! Product ' \
           'sales have been disappointing for the past three ' \
           'quarters. We have a competitive product, but we ' \
           'need to do a better job of selling it!'
    Ta = ToneAnalysis()
    Ta.tone_analysis_by_str(text)
    result = Ta.get_tone_analysis_result()
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
