from django.urls import path, include

urlpatterns = [
    path("v1/", include("apps.teacher.api.v1.urls")),
]
