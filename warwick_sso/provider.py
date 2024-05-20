from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth.provider import OAuthProvider


class WarwickSSOAccount(ProviderAccount):
    def to_str(self):
        dflt = super().to_str()
        name = self.account.extra_data.get("name", dflt)
        return name


class WarwickSSOProvider(OAuthProvider):
    id = "warwick_sso"
    name = "Warwick SSO"
    account_class = WarwickSSOAccount

    def get_default_scope(self):
        return ["urn:websignon.warwick.ac.uk:sso:service"]

    def extract_uid(self, data):
        return str(data["id"])

    def extract_common_fields(self, data):
        return dict(
            username=data.get("user"),
            email=data.get("email"),
            first_name=data.get("firstname"),
            last_name=data.get("lastname"),
            email_verified=True,
        )


provider_classes = [WarwickSSOProvider]
