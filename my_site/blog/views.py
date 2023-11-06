from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Post


class StartingPage(ListView):
    model = Post
    template_name = "blog/index.html"
    queryset = Post.objects.all().order_by("-date")[:3]
    context_object_name = "posts"


class AllPosts(ListView):
    model = Post
    template_name = "blog/all-posts.html"
    context_object_name = "posts"


class PostDetail(DetailView):
    model = Post
    context_object_name = "post"
    template_name = "blog/post-detail.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        post = super().get_object()
        context["post_tags"] = post.tags.all()
        return context
