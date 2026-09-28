# from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse


def home(request):
    return JsonResponse({
        "message": "Hello Zecpath Backend"
    })

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Job
from .serializers import JobSerializer

class JobAPI(APIView):
    def get(self,request):
        jobs=Job.objects.all()
        serializer=JobSerializer(jobs,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = JobSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()   
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)

class UserTestAPI(APIView):
    def get(self,request):
        return Response({
            "message":"User API is Working",
            "user":"Ananya"
        })