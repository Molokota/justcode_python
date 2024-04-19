from rest_framework import  serializers
from accounts.models import User


# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','nickname','email','password','first_name', 'last_name', 'mobile_phone',)
        extra_kwargs = {
            'password':{'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['email'],
                nickname = validated_data['nickname'],
                password = validated_data['password'],
                first_name = validated_data['first_name'],
                last_name = validated_data['last_name'],
                mobile_phone = validated_data['mobile_phone']
                )
        return user

