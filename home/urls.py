from django.contrib import admin
from django.urls import path
from home import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.myCheck, name="check"),
    path('create', views.myCreate, name="create"),
    path('update/<str:i>', views.myUpdate, name="update"),
    path('update2/<str:i>', views.myUpdate2, name="update"),
    path('delete/<int:i>', views.myDelete, name="delete"),
    path('check1', views.myCheck1, name="create1"),

]