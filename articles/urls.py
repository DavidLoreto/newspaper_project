from django.urls import path

from .views import (
    ArticlesListView,
    ArticleUpdateView,
    ArticleDeleteView,
    ArticleDetail,
    ArticleNew)

urlpatterns = [
    #List all articles
    path('', ArticlesListView.as_view(), name='article_list'),

    #Update an article
    path('<int:pk>/update/', ArticleUpdateView.as_view(), name='article_update'),

    #delete an article
    path('<int:pk>/delete', ArticleDeleteView.as_view(), name='article_delete'),

    #Article detail
    path('<int:pk>', ArticleDetail.as_view(), name='article_detail'),

    path('new/', ArticleNew.as_view(), name='article_new')
]
