from django.shortcuts import render
from itsdangerous import Serializer
from rest_framework import generics

# Create your views here.
from .models import Snippet
from .serializers import SnippetSerializer

class SnippetList(generics.ListCreateAPIView):
    queryset= Snippet.object.all()
    Serializer_class = SnippetSerializer
    
class SnippetDetail(generics.RetrveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class= SnippetSerializer
 
    




    

    
    
    
    
    
    
