from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    #enotes
    EnotesCreateView,
    EnotesListView,
    EnotesDetailView,
    EnotesUpdateView,
    EnotesDeleteView,
    #ques paper
    QuesPaperListView,
    QuesPaperDetailView,
    QuesPaperCreateView,
    QuesPaperUpdateView,
    QuesPaperDeleteView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    #enotes
    path('enotes/new/', EnotesCreateView.as_view(), name='enotes-create'),
    path('enotes/', EnotesListView.as_view(), name='enotes-home'),
    path('enotes/<int:pk>/', EnotesDetailView.as_view(), name='enotes-detail'),
    path('enotes/<int:pk>/update/', EnotesUpdateView.as_view(), name='enotes-update'),
    path('enotes/<int:pk>/delete/', EnotesDeleteView.as_view(), name='enotes-delete'),
    #quespaper
    path('quespaper/new/', QuesPaperCreateView.as_view(), name='ques-paper-create'),
    path('quespaper/', QuesPaperListView.as_view(), name='ques-paper-home'),
    path('quespaper/<int:pk>/', QuesPaperDetailView.as_view(), 
        name='ques-paper-detail'),
    path('quespaper/<int:pk>/update/', QuesPaperUpdateView.as_view(), 
        name='ques-paper-update'),
    path('quespaper/<int:pk>/delete/', QuesPaperDeleteView.as_view(), 
        name='ques-paper-delete'),

]