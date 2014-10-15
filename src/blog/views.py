from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.filter(published_date__isnull=False).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_unpublished(request):
    posts = Post.objects.filter(published_date_isnull=True).order_by('published_date')

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
   if request.method == "POST":
       form = PostForm(request.POST)
       if form.is_valid():
           post = form.save(commit=False)
           post.author = request.user
           post.save()
           return redirect('blog.views.post_detail', pk = post.pk)
   else:
       form = PostForm()
   return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = form(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post = form.save()
            return redirect('blog.views.post_detail', pk = post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})