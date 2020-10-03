from django.shortcuts import render, HttpResponse
from django.urls.base import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import EditForm, PostForm

# Create your views here.

# def home(request):
#     post = Post.objects.all
#     dict = {'posts':post}
#     return render(request, 'home.html', dict)
# Just to show that we can use function also 


class Home(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-published_date']

class ArticleDetail(DetailView):
    model = Post
    template_name = 'article_detail.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

    # fields = '__all__' # To fetch all the fields from the database of post for the add post form 
    # fields = ('title', 'author', 'body') # To fetch selected fields from database for the add post form

    # We dont need the fields var since the forms.py will take care of those froms stuffs

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    # fields = ('title', 'body')

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

