from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status, generics  
from .models import * 
from rest_framework import mixins
from .serializers import *
from rest_framework.exceptions import ValidationError


class Reviewcreate(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

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