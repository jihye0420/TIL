from django.urls import include, path
from users import views

# from rest_framework import routers
#
# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    path('signup', views.SignUp),
    path('login', views.Login),
]
