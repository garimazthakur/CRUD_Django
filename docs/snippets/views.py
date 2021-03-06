from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework.views import APIView

# # # Using genraic class based view
# class SnippetList(generics.ListCreateAPIView):
# #Allow: GET, POST, HEAD, OPTIONS(create a read-write endpoint that lists all available Snippet instances)
#     queryset= Snippet.objects.all()
#     serializer_class = SnippetSerializer
    
# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
# #Allow: Retrieve, update or delete a snippet instance.
#     queryset = Snippet.objects.all()
#     serializer_class= SnippetSerializer


class SnippetList(APIView):
    def get(self, request, format=None):
        snippets=Snippet.objects.all()
        serializer=SnippetSerializer(snippets, many=True)
        return Response(serializer.data)


    def post(self, request,format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetDetail(APIView):
    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet=self.get_object(pk)
        serializer=SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk,format=None):
        snippet=self.get_object(pk)
        serializer= SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 
    




    

    
    
    
    
    
    
