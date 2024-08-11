from django.urls import path
from LandingPage.views import *

app_name = 'LandingPage'

urlpatterns = [
    path('', index_view, name='index'),
    path('index/en/', index_view_en, name='index_en'),
]