from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post, Enotes
from django.contrib.auth.models import User

from .filters import EnotesFilter

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 9




class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'blog_file']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)




class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'blog_file']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})



#enotes

class EnotesListView(ListView):
    # model = Enotes
    template_name = 'blog/enotes-home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'enotes'
    # ordering = ['-date_posted']
    paginate_by = 3

    def get_context_data(self,**kwargs):
        context = super(EnotesListView,self).get_context_data(**kwargs)
        context['filter'] = EnotesFilter(self.request.GET,queryset=self.get_queryset())
        return context

    def get_queryset(self):
        return Enotes.objects.all()

class EnotesDetailView(DetailView):
    model = Enotes

class EnotesCreateView(LoginRequiredMixin, CreateView):
    model = Enotes
    fields = ['topic', 'unit', 'notes_author', 'author_name', 'fileMy',
    'sub', 'branch', 'academic_year', 'desc']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_absolute_url(self):
        return "blog-home/"

class EnotesUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Enotes
    fields = ['topic', 'unit', 'notes_author', 'author_name', 'fileMy',
    'sub', 'branch', 'academic_year', 'desc']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        enotes = self.get_object()
        if self.request.user == enotes.author:
            return True
        return False

class EnotesDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Enotes
    success_url = '/'

    def test_func(self):
        model_name = self.get_object()
        if self.request.user == model_name.author:
            return True
        return False