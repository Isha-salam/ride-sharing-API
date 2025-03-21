from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, RideViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'rides', RideViewSet,basename='ride')

urlpatterns = [
    path('', include(router.urls)),

]