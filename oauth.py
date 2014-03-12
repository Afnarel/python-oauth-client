from requests_oauthlib import OAuth1Session


class OAuthClient(object):
    def __init__(self, base_url, api_key, api_secret):
        self.base_url = base_url
        self.oauth = OAuth1Session(api_key, client_secret=api_secret)

    def get_request_token(self, url_path):
        fetch_response = self.oauth.fetch_request_token(self.url(url_path))
        self.resource_owner_key = fetch_response.get('oauth_token')
        self.resource_owner_secret = fetch_response.get('oauth_token_secret')

    def get_authorization_url(self, url_path):
        return self.oauth.authorization_url(self.url(url_path))

    def ask_permission(self, request_token_path='request_token',
                       authorization_path='authorize'):
        self.get_request_token(request_token_path)
        return self.get_authorization_url(authorization_path)

    def verify(self, callback_url, verify_path='access_token'):
        response = self.oauth.parse_authorization_response(callback_url)
        verifier = response.get('oauth_verifier')

        self.oauth.resource_owner_key = self.resource_owner_key
        self.oauth.resource_owner_secret = self.resource_owner_secret
        self.verifier = verifier

        tokens = self.oauth.fetch_access_token(self.url(verify_path))
        token = tokens.get('oauth_token')
        token_secret = tokens.get('oauth_token_secret')
        return (token, token_secret)

    def url(self, url_path):
        return self.base_url + url_path


if __name__ == '__main__':
    CONSUMER_KEY = ''  # Use you API key
    CONSUMER_SECRET = ''  # Use your API secret
    client = OAuthClient(
        'https://oauth.withings.com/account/',
        CONSUMER_KEY,
        CONSUMER_SECRET)
    print client.ask_permission()
    callback = raw_input('URL: ')
    print client.verify(callback)
