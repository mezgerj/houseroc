from django.http import HttpRequest, HttpResponse
from .models import BlogPost


def worldview(request: HttpRequest):
    return HttpResponse(f"Hello, World! There are {BlogPost.objects.count()} blog posts")
