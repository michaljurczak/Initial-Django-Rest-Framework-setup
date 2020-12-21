from django.urls import re_path

from .views import basic_response

urlpatterns = [
    re_path('^$', basic_response, name="basic_response"),
]
