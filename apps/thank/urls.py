from rest_framework.routers import DefaultRouter
from apps.thank.views import ThankViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'thank', ThankViewSet, basename="thank")


urlpatterns = [
    path('', include(router.urls))
]
