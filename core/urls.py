from django.urls import path
from django.urls import include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r"country_info", views.CountryViewSet, basename="country_info")

urlpatterns = [
    path("", include(router.urls)),
]
