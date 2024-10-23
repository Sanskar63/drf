from django.urls import path
from .views import *

urlpatterns = [
    path("", ProductListCreateAPIView.as_view(), name=""),
    path('<int:pk>/', ProductDetailAPIView.as_view())
]
