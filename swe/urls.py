from django.contrib import admin
from django.urls import path

from api.views import ApiView

urlpatterns = [
    path('api', ApiView.as_view(), name='api'),
]
