
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WatchListView, WatchDetailView, ReviewCreateView, ReviewListView, ReviewDetailView, StreamPlatformViewSet

# Setting up the router for the `StreamPlatform` viewset
router = DefaultRouter()
router.register(r'stream', StreamPlatformViewSet, basename='streamplatform')

# URL patterns
urlpatterns = [
    path('watchlist/', WatchListView.as_view(), name='watchlist'),                  # Lists all movies/shows
    path('watchlist/<int:pk>/', WatchDetailView.as_view(), name='watch-detail'),     # Details for a specific movie/show
    path('', include(router.urls)),                                                 # Includes `StreamPlatform` viewset routes

    # Reviews
    path('watchlist/<int:pk>/reviews/create/', ReviewCreateView.as_view(), name='review-create'),  # Create review for a specific watchlist item
    path('watchlist/<int:pk>/reviews/', ReviewListView.as_view(), name='review-list'),             # List all reviews for a specific watchlist item
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),                   # Details for a specific review
]
