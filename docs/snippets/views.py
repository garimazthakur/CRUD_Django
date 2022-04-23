from django.shortcuts import render
from itsdangerous import Serializer
from rest_framework import generics

# Create your views here.
from .models import Snippet
from .serializers import SnippetSerializer


# # Using genraic class based view
# class SnippetList(generics.ListCreateAPIView):
# #Allow: GET, POST, HEAD, OPTIONS(create a read-write endpoint that lists all available Snippet instances)
#     queryset= Snippet.object.all()
#     Serializer_class = SnippetSerializer
    
# class SnippetDetail(generics.RetrveUpdateDestroyAPIView):
# #Allow: Retrieve, update or delete a snippet instance.
#     queryset = Snippet.objects.all()
#     serializer_class= SnippetSerializer

# Using mixins
from snippets.models import Snippet 
from snippets.serializers import SnippetSerializer
from rest_framework import mixins
from rest_framework import generics


 
    




    

    
    
    
    
    
    
