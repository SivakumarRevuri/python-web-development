# Generic Views

from rest_framework import generics
from postings.models import BlogPost
from .serializers import BlogPostSerializers

class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    # queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializers
    
    def get_queryset(self):
        # return super().get_queryset()
        return BlogPost.objects.all()
    
    # def get_object(self):
    #     # return super().get_object()
    #     pk = self.kwargs.get('pk')
    #     return BlogPost.objects.get(pk=pk)