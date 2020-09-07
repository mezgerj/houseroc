from django.http import HttpResponse, HttpRequest


def worldview(request: HttpRequest):
    return HttpResponse(f"Hello, World! The request method was {request.method}",)
