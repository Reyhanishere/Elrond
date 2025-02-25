from django.urls import path
from .views import  HomePageView, AboutPageView, article_list, create_article, article_detail

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("articles/", article_list, name="article_list"),
    path("articles/create/", create_article, name="create_article"),
    path("articles/<int:article_id>/", article_detail, name="article_detail"),
]

