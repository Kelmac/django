from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView
# Create your views here.
class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 10
    template_name = 'news/list.html'


def post_list(request):
    posts = Post.published.all()
    return render(request,
                  'news/list.html',
                  {'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request, 'news/detail.html',
                  {'post': post})
