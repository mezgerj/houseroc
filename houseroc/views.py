from django.http import HttpRequest, HttpResponse


def worldview(request: HttpRequest):
    return HttpResponse(f"Hello, World! The request method was {request.method}",)
