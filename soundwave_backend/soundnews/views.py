from django.db.models import Q
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Story, Category
from .serializers import StorySerializer, CategorySerializer

class LatestStoriesList(APIView):
    def get(self, request, format=None):
        products = Story.objects.all()[0:4]
        serializer = StorySerializer(products, many=True)
        return Response(serializer.data)

class StoryDetail(APIView):
    def get_object(self, category_slug, story_slug):
        try:
            return Story.objects.filter(category__slug=category_slug).get(slug=story_slug)
        except Story.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, story_slug, format=None):
        product = self.get_object(category_slug, story_slug)
        serializer = StorySerializer(product)
        return Response(serializer.data)

class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        stories = Story.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = StorySerializer(stories, many=True)
        return Response(serializer.data)
    else:
        return Response({"products": []})