from django.urls import path
from .views import home,JobAPI,UserTestAPI

urlpatterns = [
    path('', home),
    path('api/jobs/',JobAPI.as_view()),
    path('api/user-test/', UserTestAPI.as_view()),
]