# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from decorapp.models import Document
from api.serializers import DocumentSerializer, UserSerializer


@api_view(['GET', 'POST'])
def upload(request):
    if request.method == 'GET':
        docs = Document.objects.all()
        serialized_docs = []
        for doc in docs:
            serializer = DocumentSerializer(doc)
            serialized_docs.append(serializer.data)
        return Response(serialized_docs)
    elif request.method == 'POST':
        print request.data
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print '[x] %s' % serializer.error_messages
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def auth(request):
    user = request.data.get('username', '')
    passwd = request.data.get('password', '')

    if authenticate(username=user, password=passwd):
        return Response({'auth': True, 'status': status.HTTP_200_OK})
    else:
        return Response({'auth': False, 'status': status.HTTP_401_UNAUTHORIZED})


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
