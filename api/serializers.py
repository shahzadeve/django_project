from rest_framework import serializers
from .models import *



class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'


class WatchListSerializer(serializers.ModelSerializer):
    review = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Watchlist
        fields = '__all__'

    # data format is like this
#     {
#     "id": 1,
#     "name": "Inception",
#     "storyline": "A mind-bending thriller about dreams within dreams.",
#     "active": true,
#     "created": "2024-11-06T12:34:56Z"
#      }
    
class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    class Meta:
        model = StreamPlatform
        fields = '__all__'


































    # data format is lock like this 
    # {
    #     "id": 1,
    #     "name": "Netflix",
    #     "about": "A streaming platform offering various movies and TV shows.",
    #     "website": "https://www.netflix.com"
    # }


# def validate_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("name is too short new value")
#     return value


# class MoviesSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=100 ,validators=[validate_length] ) 
#     description = serializers.CharField(validators=[validate_length])
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movies.objects.create(**validated_data)
    
#     def update(self, instance, validated_data ):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("name and description should not be same")
#         return data
    
#     # def validate_name(self, value):
#     #     if len(value) < 2:
#     #         raise serializers.ValidationError("name is too short")
#     #     return value

#     def __str__(self):
#         return self.name
    
#     # define meta 
#     class Meta:
#         model = Movies
#         fields = '__all__'