from django.urls import path
from .views import *

app_name = 'userAuths'

urlpatterns = [
    path('register/', registerView, name='register'),
]
