from django.urls import path, include

from detectFruits.views import detectFruits, detectFood

urlpatterns = [
    path('fruits', detectFruits),
    path('food', detectFood),
]