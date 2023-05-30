from django.urls import path, include
from rest_framework import routers

from .viewsets.blog import BlogViewSet

app_name = "blog"

# URLs da API
router = routers.DefaultRouter()
router.register('', BlogViewSet, basename='blog')

# urlpatterns = [
#     path("blog/", ViewSet.as_view()),
# ]

urlpatterns = router.urls
