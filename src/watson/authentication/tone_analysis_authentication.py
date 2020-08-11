# NEEDIMPROVE: adjust those import in the future
from ibm_cloud_sdk_core import ApiException
from ibm_cloud_sdk_core.authenticators import *
from ibm_watson.tone_analyzer_v3 import *


class ToneAnalysisAuthentication:
    """
    After claimed, need to call get_tone_analyzer() to get tone analyzer authentication.
    ATTENTION: be careful of the different of _authenticator(attribute), _get_authenticator()(getter setter), _get_authentication()(private function), and get_tone_analyzer()(critical function)
    """

    def __init__(self):
        """
        Constructor
        """
        self._apikey = 'DAFlrX2dJR9I81LLxeCmxRqGBtu69cmbEKMCggULoYnF'
        self._version = '2020-2-13'
        self._url = 'https://api.us-east.tone-analyzer.watson.cloud.ibm.com/instances/4ea25116-c988-47d0-8afc-1b32407b29b3'
        self._authenticator = None  # IAMAuthenticator authentication
        self._tone_analyzer = None  # tone analyzer authentication

    def _get_authentication(self):
        """Get Watson Tone Analysis Authenticator to access Tone Analysis"""
        try:
            _authenticator = IAMAuthenticator(f'{self.get_apikey()}')
            self._get_authenticator(_authenticator)
        except ApiException as ex:
            print
            "Method failed with status code " + str(ex.code) + ": " + ex.message

    def get_tone_analyzer(self):
        """
        get ToneAnalyzerV3 object, and set service.
        :return: usable tone_analyzer
        """
        self._get_authentication()  # get IAMAuthenticator authentication
        try:
            tone_analyzer = ToneAnalyzerV3(version=f'{self.get_version()}', authenticator=self._get_authenticator())
            tone_analyzer.set_service_url(f'{self.get_url()}')
        except ApiException as ex:
            print
            "Method failed with status code " + str(ex.code) + ": " + ex.message
        return tone_analyzer

    def get_apikey(self, apikey=None):
        """
        Getter and Setter of _apikey
        :param apikey:
        :return:
        """
        if isinstance(apikey, str):
            self._apikey = apikey
        return self._apikey

    def get_version(self, version=None):
        """
        Getter and Setter of _version
        :param version:
        :return:
        """
        if isinstance(version, str):
            self._version = version
        return self._version

    def get_url(self, url=None):
        """
        Getter and Setter of _url
        :param url:
        :return:
        """
        if isinstance(url, str):
            self._url = url
        return self._url

    def _get_authenticator(self, authenticator=None):
        """
        Getter and setter of _authenticator
        :param authenticator:
        :return:
        """
        # FIXME: Find a way to regulate authenticator
        if authenticator:
            self._authenticator = authenticator
        return self._authenticator


def main():
    # TEST: for test SUCCESS
    t = ToneAnalysisAuthentication()
    ta = t.get_tone_analyzer()
    text = 'Team, I know that times are tough! Product ' \
           'sales have been disappointing for the past three ' \
           'quarters. We have a competitive product, but we ' \
           'need to do a better job of selling it!'

    tone_analysis = ta.tone(
        {'text': text},
        content_type='application/json'
    ).get_result()
    print(json.dumps(tone_analysis, indent=2))


if __name__ == '__main__':
    main()
