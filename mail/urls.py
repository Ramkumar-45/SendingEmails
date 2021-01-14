from django.urls import path
from .views import *

urlpatterns = [
    path('', sendmail, name='mail')
]