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
        article = self.get_object(category_slug, article_slug)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)