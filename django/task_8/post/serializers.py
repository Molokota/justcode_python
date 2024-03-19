from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def validate(self, data):
        description = data.get('description')
        
        print("description:", description)
        if len(description) < 10:
            raise serializers.ValidationError("Слишком короткое описание")

        return data