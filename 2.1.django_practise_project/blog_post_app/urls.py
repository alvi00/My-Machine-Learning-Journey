from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("post/<int:pk>",views.post_details,name="post-detail"),
    path("post/new",views.PostCreateview.as_view(),name="post-create"),
    path("post/<int:pk>/edit/",views.PostUpdateview.as_view(),name="post-update"),
    path("post/<int:pk>/delete/",views.PostDeleteview,name="post-delete")
]
