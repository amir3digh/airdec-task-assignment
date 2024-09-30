from rest_framework import status
from django.utils.translation import gettext_lazy as _


def custom_status(code):
    if type(code) is not int:
        raise TypeError("Status code must be an integer")

    if code == status.HTTP_200_OK:
        return "OK", _("success")
    elif code == status.HTTP_201_CREATED:
        return "CREATED", _("successfully created")
    elif code == status.HTTP_400_BAD_REQUEST:
        return "VALIDATION_ERROR", _("data is not valid")
    elif code == status.HTTP_401_UNAUTHORIZED:
        return "AUTHORIZATION_ERROR", _("access denied")
    elif code == status.HTTP_404_NOT_FOUND:
        return "NOT_FOUND", _("resource not found")
    # --------------------------------------------------
    elif status.is_informational(code):
        return "INFORMATIONAL", _("information provided successfully")
    elif status.is_success(code):
        return "SUCCESS", _("success")
    elif status.is_redirect(code):
        return "REDIRECT", _("redirecting...")
    elif status.is_client_error(code):
        return "CLIENT_ERROR", _("client error")
    elif status.is_server_error(code):
        return "SERVER_ERROR", _("server error")
    # --------------------------------------------------
    else:
        return "UNKNOWN", _("unknown error")
