from allauth.socialaccount.providers.oauth.urls import default_urlpatterns

from .provider import WarwickSSOProvider

urlpatterns = default_urlpatterns(WarwickSSOProvider)
