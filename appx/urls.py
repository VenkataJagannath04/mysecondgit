from django.urls import path
from appx.views import *
app_name='jay'
urlpatterns=[
    path('jay/', jay, name='jay'),
]