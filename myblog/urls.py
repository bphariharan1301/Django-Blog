from django.urls import path
from .views import Home, ArticleDetail, AddPostView, UpdatePostView
# from . import views

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetail.as_view(), name='article_detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    # path('', views.home, name='home') in case if you are using function
]