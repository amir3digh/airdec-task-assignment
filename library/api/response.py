from rest_framework.response import Response
from library.api.status import custom_status
from rest_framework import status as rest_status

"""
    Making more informational responses for better front-end development
"""


def json_response(instance: Response, message: str = None):
    status = instance.status_code
    status_code, default_message = custom_status(status)

    structured_data = {"status": status_code}

    if rest_status.is_client_error(status):
        structured_data["errors"] = instance.data
    else:
        structured_data["data"] = instance.data

    if not message:
        message = default_message

    structured_data["message"] = message
    instance.data = structured_data
    return instance


class TemplateResponse(Response):
    def __init__(
            self, data=None,
            status=None,
            template_name=None,
            headers=None,
            exception=False,
            content_type=None,
            message=None,
            **kwargs
    ):
        if not status:
            status = rest_status.HTTP_200_OK

        status_code, default_message = custom_status(status)

        structured_data = {"status": status_code}

        if not message:
            message = default_message

        structured_data["message"] = message

        if rest_status.is_client_error(status):
            structured_data["errors"] = data
        else:
            structured_data["data"] = data

        super().__init__(
            data=structured_data, status=status, template_name=template_name,
            headers=headers, exception=exception, content_type=content_type,
        )
