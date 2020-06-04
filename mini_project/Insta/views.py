from django.views. generic import TemplateView, ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from django.contrib.auth.forms import UserCreationForm
from .models import Post

from django.contrib.auth.mixins import LoginRequiredMixin



class HelloWorld(TemplateView): #继承 templateview hello world is a templateview 
    template_name = 'test.html' # override template name 

class PostView(LoginRequiredMixin, ListView): #show all the post 

    model = Post 
    template_name = 'index.html'  # change url and create index.html
    login_url = 'login'

class PostDetailView(DetailView):
    model = Post 
    template_name = 'post_detail.html'

class PostCreateView(CreateView):
    model = Post 
    template_name = 'post_create.html'
    fields = '__all__' #django special grammar 

class PostUpdateView(UpdateView):
    model = Post 
    template_name = 'post_update.html'
    fields = ['title']

class PostDeleteView(DeleteView):
    model = Post 
    template_name = 'post_delete.html'
    success_url = reverse_lazy("helloworld")

class SignUp(CreateView):
    form_class = UserCreationForm 
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


