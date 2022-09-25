from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from blog.api.views import  TagViewSet, PostViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

router = DefaultRouter()
router.register("tags", TagViewSet)
router.register("posts", PostViewSet)

urlpatterns = [
    path("auth/", include("rest_framework.urls")),
    path("token-auth/", views.obtain_auth_token),
    path("", include(router.urls)),
]

urlpatterns = format_suffix_patterns(urlpatterns)

