import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status
from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from .models import Ride
from .serializers import UserSerializer, RideSerializer
from .utils import find_best_driver

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@method_decorator(csrf_exempt, name='dispatch')
class RideViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
    permission_classes = [AllowAny]

    @action(detail=True, methods=["patch"])
    def update_status(self, request, pk=None):
        ride = self.get_object()
        new_status = request.data.get("status")

        if new_status not in dict(Ride.STATUS_CHOICES):
            return Response({"error": "Invalid status"}, status=400)

        ride.status = new_status
        ride.save()
        return Response({"message": f"Ride status updated to {ride.status}"})

    def create(self, request, *args, **kwargs):
        data = request.data
        pickup_location = data.get("pickup_location")


        best_driver = find_best_driver(pickup_location)

        if not best_driver:
            return Response({"error": "No available drivers"}, status=status.HTTP_400_BAD_REQUEST)


        data["driver"] = best_driver.id
        serializer = self.get_serializer(data=data)

        if serializer.is_valid():
            serializer.save()
            best_driver.is_available = False  
            best_driver.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
