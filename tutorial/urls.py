from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from tutorial import views

urlpatterns = [
    path('snippets', views.snippet_list),
    path('snippets/<int:pk>', views.snippet_detail),
]
urlpatterns = format_suffix_patterns(urlpatterns)  # http://127.0.0.1:8000/tutorial/snippets.json 과 같이 요청 가능
