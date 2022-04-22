from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views


urlpatterns= [
                path('snippets/', views.SnippetList.as_view()) ,
                path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
                 
]

urlpatterns= format_suffix_patterns(urlpatterns)

#  format_suffix_patterns is an optional choice that provides a simple, DRY way to refer to a specific file format for a URL endpoint