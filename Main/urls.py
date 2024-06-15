from django.urls  import path
from . import views

urlpatterns = [
    path("", views.Home, name = "Main"),
    path("main/", views.Main, name="Main"),
    path("blogs/", views.blogList, name="blogs"),
    path("blogs/blog-<int:id>", views.blogDetail, name="blogDetail"),
]