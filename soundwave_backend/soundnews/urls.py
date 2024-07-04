from django.urls import path, include

from soundnews import views

urlpatterns = [
    path('latest-storiess/', views.LatestStoriesList.as_view()),
    path('stories/search/', views.search),
    path('stories/<slug:category_slug>/<slug:product_slug>/', views.StoryDetail.as_view()),
    path('stories/<slug:category_slug>/', views.CategoryDetail.as_view()),
]