from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_home, name="api_home"),
    # path('products/', views.drf_get_data, name="drf_get_data")
    path('products/', views.post_api, name="drf_get_data"),
    

]
