from django.urls import path, include

from detectFruits.views import detectFruits

urlpatterns = [
    path('', detectFruits),
]