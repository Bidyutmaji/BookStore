from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .serializer import BookSerializer
from core.models import Book


class BookCreate(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class Bookupdate(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDelete(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
