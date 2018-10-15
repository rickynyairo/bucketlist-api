from django.shortcuts import render
from rest_framework import generics
from .serializers import BucketlistSerializer
from .models import Bucketlist

class CreateView(generics.ListCreateAPIView):
    """Defines the create behaviour of the bucketlist api"""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a bucketlist"""
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """Get the details for the  bucketlist"""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    
