from rest_framework import serializers

from .models import Category, Article

class ArticleSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Article
        fields = (
            "id",
            "title",
            "category",
            "author",
            "get_absolute_url",
            "content",
            "get_image",
            "get_thumbnail",
            "publication_date"
        )

class CategorySerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "articles",
        )