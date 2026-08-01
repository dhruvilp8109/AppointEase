from rest_framework import status
from django.http import JsonResponse


class GenericSuccessResponse(JsonResponse):

    def __init__(self, data=[], message="Success", code=status.HTTP_200_OK, *args, **kwargs):

        self.data = {
            "data": data,
            "status": {
                "code": code,
                "message": message
            }
        }

        super().__init__(data=self.data, status=code, *args, **kwargs)


class GenericException(JsonResponse):

    def __init__(self, message="There is some internal issue, please try again later.", code=status.HTTP_500_INTERNAL_SERVER_ERROR, *args, **kwargs):

        self.message = message

        self.code = code

        self.data = {
            "data": [],
            "status": {
                "code": self.code,
                "message": self.message
            }
        }

        super().__init__(data=self.data, status=self.code, *args, **kwargs)


class CustomAuthenticationFailed(GenericException):

    def __init__(self, message="Unauthorized User", code=status.HTTP_401_UNAUTHORIZED, *args, **kwargs):

        super().__init__(message=message, code=code, *args, **kwargs)


class CustomPermissionDenied(GenericException):

    def __init__(self, message="User is not allowed to perform this action", code=status.HTTP_403_FORBIDDEN, *args, **kwargs):

        super().__init__(message=message, code=code, *args, **kwargs)


class CustomMethodNotAllowed(GenericException):

    def __init__(self, message="Method Not Allowed", code=status.HTTP_405_METHOD_NOT_ALLOWED, *args, **kwargs):

        super().__init__(message=message, code=code, *args, **kwargs)


class CustomNotAcceptable(GenericException):

    def __init__(self, message="Not Acceptable ", code=status.HTTP_406_NOT_ACCEPTABLE, *args, **kwargs):

        super().__init__(message=message, code=code, *args, **kwargs)


class CustomUnsupportedMediaType(GenericException):

    def __init__(self, message="Unsupported Media Type ", code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, *args, **kwargs):

        super().__init__(message=message, code=code, *args, **kwargs)


class CustomBadRequest(GenericException):

    def __init__(self, message="Bad Request", code=status.HTTP_400_BAD_REQUEST, *args, **kwargs):

        super().__init__(message=message, code=code, *args, **kwargs)
