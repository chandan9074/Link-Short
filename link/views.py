from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


from .models import Url
from accounts.models import UserProfile
from .serializer import URLSerializer, RenderPublicURLSerializer, EditURLSerializer, UrlListSerializer

# Create your views here.


class CreatePublicLinkAPIView(APIView):

    def post(self, request):
        serializer = URLSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateUserLinkAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = URLSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EditUserLinkAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        url_obj = Url.objects.get(id=pk)
        serializer = EditURLSerializer(url_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RenderPublicURLAPIView(APIView):

    def get(self, request, str):
        if(Url.objects.filter(short_link=str)).exists():
            serializer_data = Url.objects.get(short_link=str)
            final_serializer = RenderPublicURLSerializer(serializer_data)
            return Response(final_serializer.data)
        return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)

class UserUrlListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        if(Url.objects.filter(user_profile=pk)).exists():
            serializer_data = Url.objects.filter(user_profile=pk)
            serializer_peo = UrlListSerializer(serializer_data, many=True)
            return Response(serializer_peo.data)
        return Response(status=status.HTTP_204_NO_CONTENT)

class DeleteUserLinkAPIView(APIView):

    def delete(self, request, pk):
        if(Url.objects.filter(id=pk)).exists():
            serializer_del = Url.objects.get(id=pk)
            serializer_del.delete()
            return Response( {"msg":"delete Successfully"} ,status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)