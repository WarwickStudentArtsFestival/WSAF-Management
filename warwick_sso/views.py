from allauth.socialaccount.providers.oauth.client import OAuth
from allauth.socialaccount.providers.oauth.views import (
    OAuthAdapter,
    OAuthCallbackView,
    OAuthLoginView,
)

from .provider import WarwickSSOProvider

API_BASE = "https://websignon.warwick.ac.uk"


class WarwickSSOAPI(OAuth):
    """Verifying Warwick SSO attributes."""

    url = API_BASE + "/oauth/authenticate/attributes"

    def get_user_info(self):
        query = self.query(self.url, method="POST")
        content = query.strip()
        data = {}
        for item in content.split("\n"):
            if "=" not in item:
                continue
            key, value = item.split("=", 1)
            data[key] = value
        return data


class WarwickSSOOAuthAdapter(OAuthAdapter):
    provider_id = WarwickSSOProvider.id
    request_token_url = API_BASE + "/oauth/requestToken"
    access_token_url = API_BASE + "/oauth/accessToken"
    authorize_url = API_BASE + "/oauth/authorise"

    def complete_login(self, request, app, token, response):
        client = WarwickSSOAPI(request, app.client_id, app.secret, self.request_token_url)
        extra_data = client.get_user_info()
        return self.get_provider().sociallogin_from_response(request, extra_data)


oauth_login = OAuthLoginView.adapter_view(WarwickSSOOAuthAdapter)
oauth_callback = OAuthCallbackView.adapter_view(WarwickSSOOAuthAdapter)
