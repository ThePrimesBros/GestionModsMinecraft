from django.urls import path
from django.contrib import admin
from . import views
urlpatterns=[
    path('admin', admin.site.urls),
    #path('listing', views.task_listing ,name="listing"),
]