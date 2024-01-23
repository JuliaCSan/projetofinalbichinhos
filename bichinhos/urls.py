from django.urls import path

from bichinhos import views
from bichinhos.views import index

urlpatterns = [
    path('', views.index, name='index'),
]