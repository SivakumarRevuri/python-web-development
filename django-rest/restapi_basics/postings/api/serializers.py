
from rest_framework import serializers

from postings.models import BlogPost

class BlogPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = [
            'pk',
            'user',
            'title',
            'content',
            'timestamp'
        ]    
        
        # converts to json
        # validations for data passed
        