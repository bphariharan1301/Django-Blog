from django.http import request
from django.shortcuts import render, HttpResponse
from django.urls.base import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category, Post
from .forms import EditForm, PostForm # AddCategoryForm, 

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

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(Home, self).get_context_data(*args, **kwargs)
        context["cat_menu"] =  cat_menu
        return context

class ArticleDetail(DetailView):
    model = Post
    template_name = 'article_detail.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetail, self).get_context_data(*args, **kwargs)
        context["cat_menu"] =  cat_menu
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

    # fields = '__all__' # To fetch all the fields from the database of post for the add post form 
    # fields = ('title', 'author', 'body') # To fetch selected fields from database for the add post form

    # We dont need the fields var since the forms.py will take care of those froms stuffs

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddPostView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] =  cat_menu
        return context


def CategoryView(request, cats):
    category_post = Post.objects.filter(category = cats.replace('-', ' '))    
    return render(request, 'categories.html', {'cats':cats.title().replace('-', ' '), 'category_post':category_post})



class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddCategoryView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] =  cat_menu
        return context

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    # fields = ('title', 'body')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(UpdatePostView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] =  cat_menu
        return context

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(DeletePostView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] =  cat_menu
        return context

def CategoryListView(request, cats):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list})






    