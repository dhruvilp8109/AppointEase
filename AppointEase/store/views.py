from django.shortcuts import render
from rest_framework.views import APIView, Response
# Create your views here.


class test(APIView):
    def get(self, request):
        return Response({"message": "Hello, World!"})
