from rest_framework import serializers
from .models import Post, Categories

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    # categories = CategoriesSerializer(many=True)
    categories = serializers.StringRelatedField(many=True)
    class Meta:
        model = Post
        fields = '__all__'

    # def validate(self, data):
    #     description = data.get('description')
        
    #     print("description:", description)
    #     if len(description) < 10:
    #         raise serializers.ValidationError("Слишком короткое описание")

    #     return description