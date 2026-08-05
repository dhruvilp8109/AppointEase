import traceback

from http.client import BAD_REQUEST

from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import render

from rest_framework.views import APIView, Response

from email_validator import validate_email, EmailNotValidError


from security.store_authorization import create_store_authentication_token
from common.constants import INCORRECT_PASSWORD, SERIALIZER_IS_NOT_VALID, STORE_EMAIL_ALREADY_EXISTS, STORE_REGISTERED_SUCCESSFULLY, USER_NOT_FOUND
from common.helper import validate_password
from store.models import Store
from store.serializers import StoreRegistrationSerializer
from exceptions.exception_handler import CustomAuthenticationFailed, CustomBadRequest, CustomPermissionDenied, GenericException, GenericSuccessResponse
# Create your views here.


class test(APIView):
    def get(self, request):

        return CustomAuthenticationFailed(message="user is unauthorized")
        return GenericSuccessResponse({"message": "Hello, World!"})


class Registration(APIView):

    def post(self, request):
        try:
            if ("store_name" not in request.data or request.data['store_name'] == "" or
                "store_email" not in request.data or request.data['store_email'] == "" or
                    "store_password" not in request.data or request.data['store_password'] == ""):

                return CustomBadRequest(message=BAD_REQUEST)

            if Store.objects.filter(store_email=request.data['store_email'], is_deleted=False).exists():
                print("hii")
                return CustomBadRequest(message=STORE_EMAIL_ALREADY_EXISTS)

            password_validation_response = validate_password(
                request.data["store_password"])

            if password_validation_response:
                return password_validation_response

            request.data["store_password"] = make_password(
                request.data["store_password"])

            store_registration_serializer = StoreRegistrationSerializer(
                data=request.data)

            if store_registration_serializer.is_valid():

                store = store_registration_serializer.save()
                token = create_store_authentication_token(store)
                return GenericSuccessResponse(token, message=STORE_REGISTERED_SUCCESSFULLY)

            else:
                return CustomBadRequest(message=SERIALIZER_IS_NOT_VALID)

        except Exception:
            return GenericException(traceback.print_exc())


class Login(APIView):
    def post(self, request):

        try:
            if ("store_email" not in request.data or request.data['store_email'] == "" or
                    "store_password" not in request.data or request.data['store_password'] == ""):
                return CustomBadRequest(message=BAD_REQUEST)

            store = Store.objects.get(
                store_email=request.data['store_email'], is_deleted=False)

            if not check_password(request.data['store_password'], store.store_password):
                return CustomBadRequest(message=INCORRECT_PASSWORD)

            token = create_store_authentication_token(store)
            return GenericSuccessResponse(token, message=STORE_REGISTERED_SUCCESSFULLY)

        except EmailNotValidError as e:
            return CustomBadRequest(message=str(e))

        except Store.DoesNotExist:
            return CustomBadRequest(message=USER_NOT_FOUND)

        except Exception:
            return GenericException()
