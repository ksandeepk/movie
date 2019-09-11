from django.urls import path
from .views import m1,m2,m3

urlpatterns = [
    path('m1/',m1),
    path('m2/',m2),
    path('m3/',m3),
]
