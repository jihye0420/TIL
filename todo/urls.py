from django.urls import path
from todo import views

urlpatterns = [
    # todo 조회, 등록, 수정, 삭제
    path('get', views.TodoView.as_view()),
    path('create', views.TodoView.as_view()),
    # path('update', views.UpdateTodoView.as_view()),
    # path('delete', views.DeleteTodoView.as_view()),
]
