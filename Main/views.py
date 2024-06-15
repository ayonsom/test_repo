from django.shortcuts import render
from django.http import HttpResponse
from django.template import context, loader
# Create your views here.

def Home(request):
    return render( request, "main/homepage.html", context=None)

def Main(request):
    return render(request, "main/MainPage.html", context=None)

def blogList(request):
    blogs = [
        {"id":1, "name":"Learn JS", "author":"James", "desc":"Welcome to JS Course by James"},
        {"id":2, "name":"Learn PY", "author":"Jonathan", "desc":"Welcome to Python Course by Jonathan"},
        {"id":3, "name":"Learn JAVA", "author":"Johannes", "desc":"Welcome to Java Course by Johannes"}
    ]
    return render(request, "main/blogList.html", {"data":blogs})

def blogDetail(request,id):
    blogs = [
        {"id":1, "name":"Learn JS", "author":"James", "desc":"Welcome to JS Course by James"},
        {"id":2, "name":"Learn PY", "author":"Jonathan", "desc":"Welcome to Python Course by Jonathan"},
        {"id":3, "name":"Learn JAVA", "author":"Johannes", "desc":"Welcome to Java Course by Johannes"}
    ]
    return render(request, "main/blogDetail.html", {"data":blogs[id-1]})