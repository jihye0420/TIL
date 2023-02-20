from django.urls import path
from routine import views

urlpatterns = [
    # todo: 매 주별 해야할 일의 등록 / 수정 / 삭제 / 조회 기능
    path('test', views.HelloView.as_view()),
    # path('create', views.CreateRoutine.as_view()),
    # path('get', views.JWTSignupView.as_view()),
    # path('get/list', views.JWTSignupView.as_view()),
    # path('update', views.JWTSignupView.as_view()),
    # path('delete', views.JWTLoginView.as_view()),
]
