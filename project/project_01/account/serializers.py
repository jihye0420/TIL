from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User


class SignupSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = '__all__'

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({
                "password": "Pass word fields didn't match"
            })
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError("Already existed user")
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            # username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        token = RefreshToken.for_user(user)
        # user.set_password(validated_data['password'])
        user.refreshtoken = token
        user.save()

        return user


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'
#
#     def create(self, validated_data):
#         user = User.objects.create_user(
#             email=validated_data['email'],
#             password=validated_data['password']
#         )
#         return user


class SigninSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, write_only=True)
    password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password')

    def validate(self, data):
        if not User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError(
                "이미 있음..."
            )
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            # username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        token = RefreshToken.for_user(user)
        # user.set_password(validated_data['password'])
        user.refreshtoken = token
        user.save()

        return user
