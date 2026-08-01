from django.shortcuts import render
from rest_framework.views import APIView, Response

from exceptions.exception_handler import CustomAuthenticationFailed, CustomBadRequest, CustomPermissionDenied, GenericSuccessResponse
# Create your views here.


class test(APIView):
    def get(self, request):

        return CustomAuthenticationFailed(message="user is unauthorized")
        return GenericSuccessResponse({"message": "Hello, World!"})
