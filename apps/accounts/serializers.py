from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()
class CustomUserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'phone_number',
            'first_name',
            'last_name',
            'password',
        )



    def create(self, validated_data):
        if 'first_name' in validated_data and 'last_name' in validated_data:

            user = User.objects.create_user(
                username=validated_data['username'],
                email=validated_data['username'],
                phone_number=validated_data['phone_number'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
                password=validated_data['password']

            )
            return user
        else:
            user = User.objects.create_user(
                username=validated_data['username'],
                email=validated_data['username'],
                phone_number=validated_data['phone_number'],
                password=validated_data['password'],
            )
            return user

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'phone_number',
            'first_name',
            'last_name',
        )





