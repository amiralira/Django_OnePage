from django.urls import path
from LandingPage.views import index_view

APP_NAME = 'LandingPage'

urlpatterns = [
    path('', index_view, name='index'),
]