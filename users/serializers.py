from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User


# User = get_user_model()


class JWTSignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

    def save(self, request):
        user = super().save()

        user.email = self.validated_data['email']
        user.password = self.validated_data['password']
        user.name = self.validated_data['name']
        user.set_password(self.validated_data['password'])
        user.save()
        return user

    def validate(self, data):
        email = data.get('email', None)
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("user already exists")
        return data


class JWTLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(allow_null=False)
    password = serializers.CharField(allow_null=False)

    def validate(self, data):
        print('data: ', data)
        email = data.get('email', None)
        password = data.get('password', None)
        user_email = authenticate(email=email, password=password)

        if User.objects.filter(email=user_email).exists():
            print('여기')
            user = User.objects.filter(email=user_email).first()
            print(user)
            if not user.check_password(password):
                raise serializers.ValidationError("wrong password")
        else:
            raise serializers.ValidationError("user account not exist")

        token = RefreshToken.for_user(user)
        refresh = str(token)
        access = str(token.access_token)

        data = {
            'user': user,
            'refresh': refresh,
            'access': access,
        }

        return data

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
