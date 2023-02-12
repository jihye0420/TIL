from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView
from users import views

# from rest_framework import routers
#
# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    # path('signup', views.SignUp),
    # path('login', views.Login),

    # 로그인/회원가입
    path('login', views.JWTLoginView.as_view()),
    path('signup', views.JWTSignupView.as_view()),
    # 토큰
    path('token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
