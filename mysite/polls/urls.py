from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('newengineer', views.new_engineer, name="new_engineer"),
    path('mypresence', views.my_presence, name="my presence")
    #path('newengineeradmin', views.new_engineer_admin, name="new_engineer_admin")
]
