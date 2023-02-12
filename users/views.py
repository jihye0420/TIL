from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.serializers import JWTSignupSerializer, JWTLoginSerializer
from .models import User
# from .response import response


# Create your views here.
@api_view(['GET'])
def hello_api(request):
    # test = Daehwan.objects.all()
    # print(test)
    # serializer = DaehwanSerializer(test, many=True)
    # print(serializer.data)
    return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")


class JWTSignupView(APIView):
    serializer_class = JWTSignupSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save(request)
            # res = response(status=200)
            # Response(
            #     {
            #         "user": serializer.data,
            #         "message": "register successs",
            #         "token": {
            #             "access": access_token,
            #             "refresh": refresh_token,
            #         },
            #     },
            #     status=status.HTTP_200_OK,
            # )
            return Response(status=status.HTTP_200_OK)
        else:
            # res = response(status=400)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JWTLoginView(APIView):
    serializer_class = JWTLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data['auth'])

        if serializer.is_valid():
            # print(serializer.data)

            user = serializer.validated_data['user']
            access = serializer.validated_data['access']
            refresh = serializer.validated_data['refresh']
            user = User.objects.filter(email=user).first()

            res = {
                "data": {
                    'id': user.id,
                    "type": 'users' if user.is_superuser == False else 'admin',
                    'attributes': {
                        'token': access,
                        'email': user.email,
                        'user': user.name,
                        # "name": user.firstName + ' ' + user.lastName,
                        # "country": user.country,
                        "createdAt": user.created_at,
                        "updatedAt": user.updated_at,
                    }

                }
            }
            return Response(
                data=res, status=status.HTTP_200_OK
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
