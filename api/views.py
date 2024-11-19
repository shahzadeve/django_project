from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status, generics, viewsets
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from .models import Watchlist, StreamPlatform, Review
from .serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer
from .permissions import AdminOrOwnerOnly , IsAuthenticatedOrReadOnly , IsAdmin , IsReviewOwner
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import SAFE_METHODS




class WatchListView(generics.ListCreateAPIView):
    """
    Handles listing all watchlist items and creating new items.
    """
    queryset = Watchlist.objects.all()
    serializer_class = WatchListSerializer
    


    def delete(self, request, pk):
        watch_item = get_object_or_404(Watchlist, pk=pk)
        watch_item.delete()
        return Response({'message': 'Movie deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


class WatchDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles retrieving, updating, and deleting a specific watchlist item.
    """
    queryset = Watchlist.objects.all()
    serializer_class = WatchListSerializer


class StreamPlatformViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling StreamPlatform objects, using Django REST Framework's ViewSet
    to simplify the codebase.
    """
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer


class ReviewCreateView(generics.CreateAPIView):
    """
    Handles the creation of new reviews for a specific watchlist item.
    """
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs.get("pk")
        watchlist = get_object_or_404(Watchlist, pk=pk)

        if Review.objects.filter(watchlist=watchlist , user=self.request.user ).exists():
            raise ValidationError("Review already exists for this watchlist.")
        
        if watchlist.number_rating == 0:
            watchlist.avg_rating = serializer.validated_data['rating']
        else:
            watchlist.avg_rating = (watchlist.avg_rating + serializer.validated_data['rating']) / (watchlist.number_rating + 1)
        watchlist.number_rating += 1
        watchlist.save()

        serializer.save(watchlist=watchlist , user=self.request.user)

          


class ReviewListView(generics.ListCreateAPIView):
    """
    Handles listing and creating reviews for a specific watchlist item.
    """
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)
    
    def perform_create(self, serializer):
        watchlist_id = self.kwargs['pk']
        watchlist = get_object_or_404(Watchlist, pk=watchlist_id)
        serializer.save(watchlist=watchlist)





class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles retrieving, updating, and deleting a specific review.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_permissions(self):
        if self.request.method == "DELETE":
            return [IsAdmin() | IsReviewOwner()]  # Combine both permissions
        elif self.request.method in SAFE_METHODS:  # Read-only methods
            return []
        return [IsAuthenticated()]  # For update or other non-safe methods

