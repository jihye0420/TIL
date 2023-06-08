from django.urls import path

from .views import *

urlpatterns = [
    path("signup", SignupAPIView.as_view()),  # 회원가입
    path("signin", SigninAPIView.as_view()),  # 로그인
]
