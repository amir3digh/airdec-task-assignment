from dj_rest_auth.serializers import PasswordResetSerializer
from allauth.utils import build_absolute_uri
from allauth.account.utils import user_pk_to_url_str


class CustomPasswordResetSerializer(PasswordResetSerializer):
    @staticmethod
    def url_generator(request, user, temp_key):
        path = ("/auth/password-reset/confirm/{uid}/{token}/"
                .format(uid=user_pk_to_url_str(user), token=temp_key))

        url = build_absolute_uri(None, path)

        url = url.replace('%3F', '?')

        return url

    def get_email_options(self):
        return {
            'url_generator': self.url_generator
        }

