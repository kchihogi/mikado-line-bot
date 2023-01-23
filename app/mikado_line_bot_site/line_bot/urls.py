"""The setting of URLs.
"""
from django.urls import path

from line_bot import views

app_name = 'line_bot'
urlpatterns = [
    path('', views.index, name='callback'),
]
