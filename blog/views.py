from django.views.generic import DetailView, ListView, UpdateView, DeleteView, CreateView
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Blog
# Create your views here.

# #doing the list operation using the fucntion based view


def all_post(request):
    posts = Blog.published.all()
    return render(request, 'blog/posts.html', {'posts': posts} )

def post_detail(request, id):
    # try:
    #     posts = Blog.published.get(id=id)
    # except Blog.DoesNotExist:
    #     raise Http404("No post found.")
    # return render(request, 'blog/post_detail.html', {'post': posts} )
    posts = get_object_or_404(Blog, id=id, choices=Blog.Status.PUBLISHED)
    return render(request, 'blog/post_detail.html', {'post': posts} )





# class Posts(ListView):
#     model = Blog
#     template_name = 'blog/posts.html'
#     context_object_name = 'posts'
#     ordering = ['-created_at']
#     paginate_by = 5 

#     def all_post(request):
#         query_set = Blog.objects.all()
            

# class Post(DetailView):
#     model = Blog
#     template_name = 'blog/post_detail.html'
#     context_object_name = 'post'
#     pk_url_kwarg = 'id'  #

# class PostUpdate(UpdateView):
#     model = Blog
#     template_name = 'blog/post_update.html'
#     context_object_name = 'post'
#     fields = ['title', 'body', 'tags']
#     pk_url_kwarg = 'id'
#     success_url = '/posts/'

# class PostDelete(DeleteView):
#     model = Blog
#     template_name = 'blog/post_delete.html'
#     context_object_name = 'post'
#     pk_url_kwarg = 'id'
#     success_url = '/posts/'

# class PostCreate(CreateView):
#     model = Blog
#     template_name = 'blog/post_create.html'
#     context_object_name = 'create_post'
#     fields = ['title', 'body', 'tags']
#     success_url = '/posts/'

    