from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RoutineSerializer
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenVerifyView, token_verify
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.settings import api_settings


class CustomJWTAuthenticator(JWTAuthentication):
    def get_validated_token(self, raw_token):
        """
        Validates an encoded JSON web token and returns a validated token
        wrapper object.
        """
        messages = []
        for AuthToken in api_settings.AUTH_TOKEN_CLASSES:
            try:
                return AuthToken(raw_token)
            except TokenError as e:
                messages.append(
                    {
                        "token_class": AuthToken.__name__,
                        "token_type": AuthToken.token_type,
                        "message": e.args[0],
                    }
                )

        # raise InvalidToken(
        #     {
        #         "detail": _("Given token not valid for any token type"),
        #         "messages": messages,
        #     }
        # )



# todo: 사용자 인증 커스텀 해보기 (https://stackoverflow.com/questions/75108450/how-to-override-the-default-login-for-django-rest-framework-browsable-api)
class HelloView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        # authenitcate() verifies and decode the token
        # if token is invalid, it raises an exception and returns 401
        # JWT_authenticator = CustomJWTAuthenticator() # 상속 -> 오버라이드
        # response = JWT_authenticator.authenticate(request)
        # if response is not None:
        #     # unpacking
        #     user, token = response
        #     print("this is decoded token claims", token.payload)
        # else:
        #     print("no token is provided in the header or the header is missing")

        print(request)
        print(request.user) # USERNAME_FIELDS
        print(request.auth) # token값
        print(request.headers) # 헤더 값 가져오기
        print(request.headers['x-user-type']) # 사용자 정의 헤더 key값을 넣어서 값 가져오기
        # JWTAuthentication.get_user()
        # print(request.META.get('HTTP_AUTHORIZATION')['Authorization'])
        # user_email = authenticate(email=email, password=password)
        # https: // stackoverflow.com / questions / 32844784 / django - rest - framework - custom - authentication
        # access_token_obj = AccessToken()
        # user_id = access_token_obj['user_id']
        # user = User.objects.get(id=user_id)
        content = {'message': 'Hello, World!'}
        return Response(content)


# class CreateRoutine(APIView):
#     # 권한
#     permission_classes = [permissions.IsAuthenticated]
#
#     def post(self, request, pk):
#         # 인증
#         token_user_email = request.user.email
#         token_user_username = request.user.username
#         serializer = RoutineSerializer(data=request.data)
#         # if routine_serializer.is_valid():
#         #     routine_serializer.save()
#         #     return Response(routine_serializer.data, status=status.HTTP_201_CREATED)
#         # return Response(routine_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#         title = serializer.initial_data['title']
#         category = serializer.initial_data['category']
#         if 'MIRACLE' not in category and 'HOMEWORK' not in category:
#             return Response('Check your input form about category.', status=status.HTTP_400_BAD_REQUEST)
#         goal = serializer.initial_data['goal']
#         is_alarm = serializer.initial_data['is_alarm']
#         days = serializer.initial_data['days']
#         routine.objects.create(account_id=account_id, title=title, category=category, goal=goal,
#                                is_alarm=bool(is_alarm))
#         created_routine = routine.objects.last()
#         try:
#             if len(days) > 1:
#                 for day in days:
#                     routine_result.objects.create(routine_id=created_routine, result='NOT', is_deleted=False)
#                     routine_day.objects.create(day=day, routine_id=created_routine)
#             else:
#                 routine_day.objects.create(day=days[0], routine_id=created_routine)
#                 routine_result.objects.create(routine_id=created_routine, result='NOT', is_deleted=False)
#         except:
#             return HttpResponse("Check your input form", status=status.HTTP_400_BAD_REQUEST)
#         return Response({
#             'data': created_routine.routine_id,
#             'message': {
#                 'msg': 'You have successfully created the routine.',
#                 'status': 'ROUTINE_CREATE_OK'
#             }
#         })
