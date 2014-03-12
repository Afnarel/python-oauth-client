python-oauth-client
===================

Simple OAuthClient class in Python which simplifies the retrieval of oauth access tokens in a web app

It makes [requests-oauthlib](http://requests-oauthlib.readthedocs.org/en/latest/) even simpler.

How to use it:

  * Create a OAuthClient object. It needs
    * the base URL used for oauth
    * the API key
    * the API secret
  * Call `client.ask_permission()`: it returns the URL the user needs to visit
    to accept the permissions asked by your web app
  * When the client has accepted to allow your app, he is redirected to the
    callback URL (with a 'verifier' token). Call `client.verify(callback)` and
    it will return a (user_key, user_secret) tuple. You can now use these to
    access the resources exposed by the provider's API.
