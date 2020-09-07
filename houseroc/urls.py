from django.urls import path

from houseroc.views import worldview

urlpatterns = [
    path("world/", worldview),
]
