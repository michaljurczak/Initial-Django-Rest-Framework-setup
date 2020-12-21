from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def basic_response(request):
    """
    Return response with 'Basic response!' message
    """
    response_message = {"message": "Basic response!"}
    return Response(response_message, status=status.HTTP_200_OK)
