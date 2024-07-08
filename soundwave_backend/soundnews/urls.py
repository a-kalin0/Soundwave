from django.urls import path, include

from soundnews import views

urlpatterns = [
    path('latest_articles/', views.LatestArticlesList.as_view()),
    path('articles/search/', views.search),
    path('articles/<slug:category_slug>/<slug:article_slug>/', views.ArticleDetail.as_view()),
    path('articles/<slug:category_slug>/', views.CategoryDetail.as_view()),
]