from django.db.models import Q
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Article, Category
from .serializers import ArticleSerializer, CategorySerializer

class LatestArticlesList(APIView):
    def get(self, request, format=None):
        articles = Article.objects.all()[0:4]
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

class ArticleDetail(APIView):
    def get_object(self, category_slug, article_slug):
        try:
            return Article.objects.filter(category__slug=category_slug).get(slug=article_slug)
        except Article.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, article_slug, format=None):
        product = self.get_object(category_slug, article_slug)
        serializer = ArticleSerializer(product)
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
        articles = Article.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    else:
        return Response({"stories": []})