from django.urls import path

from .views import home, JobAPIView, UserTestAPIView


urlpatterns = [
    path('', home),
    path('api/jobs/', JobAPIView.as_view()),
    path('api/user-test/', UserTestAPIView.as_view()),
]