from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status, generics  
from .models import * 
from rest_framework import mixins
from .serializers import *
from rest_framework.exceptions import ValidationError
from rest_framework import viewsets


class Reviewcreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    def perform_create(self, serializer):
        pk = self.kwargs.get("pk")
        watchlist = Watchlist.objects.get(pk=pk)
        serializer.save(watchlist=watchlist)

    

class ReviewList(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)
    
    def perform_create(self, serializer):
        watchlist_id = self.kwargs['pk']
        try:
            watchlist = Watchlist.objects.get(pk=watchlist_id)
        except Watchlist.DoesNotExist:
            raise ValidationError("The specified watchlist item does not exist.")
        serializer.save(watchlist=watchlist)

class ReviewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class WatchList(APIView):

    def get(self, request):
        movies = Watchlist.objects.all()
        serializers = WatchListSerializer()
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializers = WatchListSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk):
        movie = get_object_or_404(WatchListSerializer, pk=pk)
        movie.delete()
        return Response({'message': 'Movie deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

class WatchDetails(APIView):

    def get(self, request, pk):
        movie = get_object_or_404(Watchlist, pk=pk)
        serializers = WatchListSerializer(movie)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        movie = get_object_or_404(Watchlist, pk=pk)
        serializers = WatchListSerializer(movie, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

   




class StreamPlatformViewSet(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer

    def list(self, request, *args, **kwargs):
        movies = self.get_queryset()
        serializer = self.get_serializer(movies, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None, *args, **kwargs):
        movie = get_object_or_404(StreamPlatform, pk=pk)
        serializer = self.get_serializer(movie)
        return Response(serializer.data)

    def update(self, request, pk=None, *args, **kwargs):
        """
        Handle PUT requests (complete update).
        Replace the entire resource with the provided data.
        """
        movie = get_object_or_404(StreamPlatform, pk=pk)
        serializer = self.get_serializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()  # This will replace the entire object
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None, *args, **kwargs):
        """
        Handle PATCH requests (partial update).
        Update only the fields provided in the request.
        """
        movie = get_object_or_404(Watchlist, pk=pk)
        serializer = self.get_serializer(movie, data=request.data, partial=True)  # `partial=True` allows partial updates
        if serializer.is_valid():
            serializer.save()  # This will only update the fields provided in the request
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None, *args, **kwargs):
        movie = get_object_or_404(StreamPlatform, pk=pk)
        movie.delete()
        return Response({'message': 'Movie deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
class StreamPlatformList(APIView):

    def get(self, request):
        movies = StreamPlatform.objects.all()
        serializers = StreamPlatformSerializer(movies, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializers = StreamPlatformSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
   
    

class StreamPlatformDetails(APIView):

    def get(self, request, pk):
        movie = get_object_or_404(StreamPlatform, pk=pk)
        serializers = StreamPlatformSerializer(movie)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        movie = get_object_or_404(StreamPlatform, pk=pk)
        serializers = StreamPlatformSerializer()
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie = get_object_or_404(StreamPlatform, pk=pk)
        movie.delete()
        return Response({'message': 'Movie deleted successfully'}, status=status.HTTP_204_NO_CONTENT)





# @api_view(['GET', 'POST', 'PUT'])
# def movieslist(request):
#     if request.method == 'GET':
#         movies = Movies.objects.all()
#         serializers = MoviesSerializer(movies, many=True)
#         return Response(serializers.data, status=status.HTTP_200_OK)

#     elif request.method == 'POST':
#         serializers = MoviesSerializer(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def moviedetails(request, pk):
#     movie = get_object_or_404(Movies, pk=pk)
    
#     if request.method == 'GET':
#         serializers = MoviesSerializer(movie)
#         return Response(serializers.data, status=status.HTTP_200_OK)

#     elif request.method == 'PUT':
#         serializers = MoviesSerializer(movie, data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         movie.delete()
#         return Response({'message': 'Movie deleted successfully'}, status=status.HTTP_204_NO_CONTENT)



# class ReviewDetails(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# class ReviewListView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)