from django.urls import path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from tutorial import views

router = routers.SimpleRouter(trailing_slash=False)
router.register('snippets', views.SnippetViewSet)

# urlpatterns = [
#     path("fbv/snippets", views.snippet_list),
#     path("fbv/snippet/<int:pk>", views.snippet_detail),
#     path("cbv/snippets", views.SnippetList.as_view()),
#     path("cbv/snippet/<int:pk>", views.SnippetDetail.as_view()),
#     path("mixin/snippets", views.SnippetAPIMixins.as_view()),
#     path("mixin/snippet/<int:pk>", views.SnippetDetailAPIMixins.as_view()),
#     path('snippets', views.SnippetAPI.as_view()),
#     path('snippet/<int:pk>', views.SnippetDetailAPI.as_view()),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)  # http://127.0.0.1:8000/tutorial/snippets.json 과 같이 요청 가능
urlpatterns = router.urls