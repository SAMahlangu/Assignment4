import statistics
from django.conf import settings
from django.urls import path
from .views import PostListView, PostDetailView ,PostCreateView,PostUpdateView, PostDeleteView, upload_article, home
from . import views

urlpatterns = [
    path('', home, name='blog-home'),
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('page/',views.page1,name = 'blog-page1'),    
    path('page2/',views.page2,name = 'blog-page2'),
    path('page3/',views.page3,name = 'blog-page3'),
     path('upload/', upload_article, name='upload-article'),

]
