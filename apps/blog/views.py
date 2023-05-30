from django.shortcuts import render

from .models import Blog


def blog(request):
    query_blog = Blog.objects.all()

    return render(request, "blog/index.html", {"blogs": query_blog})
