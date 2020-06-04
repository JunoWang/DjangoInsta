from django.contrib import admin
from django.urls import include, path 

<<<<<<< HEAD
from Insta.views import HelloWorld, PostView, PostDetailView, PostCreateView,PostUpdateView, PostDeleteView, SignUp


urlpatterns=[
    path('', HelloWorld.as_view(), name = 'Home'),
    path('posts/', PostView.as_view(), name = 'posts'),
    path('posts/<int:pk>', PostDetailView.as_view(), name = 'post_detail'),
    path('posts/new', PostCreateView.as_view(), name = 'make_post'),
    path('posts/update/<int:pk>', PostUpdateView.as_view(), name = 'post_update'), # need to kown which one to update
    path('posts/delete/<int:pk>', PostDeleteView.as_view(), name = 'post_delete'),
    path('auth/signup', SignUp.as_view(), name = 'signup')
=======
from Insta.views import HelloWorld 

urlpatterns=[
    path('', HelloWorld.as_view(), name = 'Home')
>>>>>>> 439bcbfa53faf26e586e7babc2a1e0b79754cf87
]