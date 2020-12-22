from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ="index"),
    path('post/<slug:slug>/', views.post, name ="post"),
    path('posts/', views.posts, name ="posts"),
    path('about/', views.about, name ="about"),
    path('resume/', views.resume, name ="resume"),
    path('portfolio/', views.portfolio, name ="portfolio"),
    path('contact/', views.contact, name ="contact"),

    #CRUD 
    
    path('create_post/', views.createPost, name="create_post"),
    path('update_post/<slug:slug>/', views.updatePost, name="update_post"),
    path('delete_post/<slug:slug>/', views.deletePost, name="delete_post"),

    path('send_email/', views.sendEmail, name="send_email"),
]

