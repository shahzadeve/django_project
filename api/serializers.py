from rest_framework import serializers
from .models import *



class ReviewSerializer(serializers.ModelSerializer):
    # import user from models
    review_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        # fields = '__all__'
        exclude = ['watchlist']


class WatchListSerializer(serializers.ModelSerializer):
    review = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Watchlist
        fields = '__all__'

    
class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    class Meta:
        model = StreamPlatform
        fields = '__all__'
    def update(self, instance, validated_data):
        watchlist_data = validated_data.pop('watchlist', [])
        instance = super().update(instance, validated_data)

        for item_data in watchlist_data:
            watchlist_item = Watchlist.objects.get(id=item_data.get('id'))
            watchlist_item.storyline = item_data.get('storyline', watchlist_item.storyline)
            watchlist_item.save()
        
        return instance
