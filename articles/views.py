from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import (
                                    ListView, 
                                    UpdateView, 
                                    DeleteView, 
                                    DetailView,
                                    CreateView)

from .models import Article

class ArticlesListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    template_name = 'list_articles.html'
    context_object_name = 'articles'
    model = Article


class ArticleDetail(LoginRequiredMixin, DetailView):
    login_url = 'login'
    template_name = 'article_detail.html'
    model = Article
    context_object_name = 'article'


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    template_name = 'article_update.html'
    model = Article
    fields = ['title', 'body']

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()

        if obj.author != request.user:
            raise PermissionDenied
        
        return super().dispatch(request, *args, **kwargs)
    


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    model = Article

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()

        if obj.author != request.user:
            raise PermissionDenied

        return super().dispatch(request, *args, **kwargs)


class ArticleNew(LoginRequiredMixin, CreateView):
    login_url = 'login'
    template_name = 'article_new.html'
    model = Article
    fields = ('title', 'body')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)