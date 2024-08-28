from django.urls import path, include

from soundnews import views

urlpatterns = [
    path('latest_articles/', views.LatestArticlesList.as_view()),
    path('articles/<slug:category_slug>/<slug:article_slug>/', views.ArticleDetail.as_view()),
]