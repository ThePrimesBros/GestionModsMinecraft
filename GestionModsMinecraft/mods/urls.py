from django.urls import path
from django.contrib import admin
from . import views

urlpatterns=[
    path('admin', admin.site.urls),
    path('', views.task, name='task'),
    path('listing', views.liste ,name="listing"),
    path('listing/', views.liste ,name="listing"),
    path('scrap', views.scrap ,name="scrap"),
    path('detail/<int:cid>', views.detail, name='detail'),
    path('edit/<int:pers_id>', views.edit, name='edite'),
    path('del/<int:pers_id>', views.delete, name='delete'),
]