from django.shortcuts import render

from django.http import HttpResponse

from .models import Blog


def blog(request):
    query = Blog.objects.all()

    lista_query = "<br>".join([str(item) for item in query])
    return HttpResponse(f"<h1> {lista_query}")
