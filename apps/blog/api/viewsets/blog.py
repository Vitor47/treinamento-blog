from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from ...models import Blog
from ..serializers import BlogSerializer


class BlogViewSet(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Blog.objects.all().order_by("-id")

    def create(self, request, *args, **kwargs):
        return super(BlogViewSet, self).create(request, *args, **kwargs)

    def update(self, request, pk=None):
        instane = self.get_object()

        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK,
        )

    def partial_update(self, request, *args, **kwargs):
        return super(BlogViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(BlogViewSet, self).destroy(request, *args, **kwargs)
        