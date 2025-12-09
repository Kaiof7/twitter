from twitter_clone import views
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.http import HttpResponse

urlpatterns = [
    path("", lambda request: HttpResponse("API do Twitter Clone está funcionando.")),

    path('admin/', admin.site.urls),
    path('api/', include('tweets.urls')),
    path('api/users/', include('users.urls')),

    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    path("update_server/", views.update, name="update"),
    path("hello/", views.hello_world, name="hello_world"),
]
