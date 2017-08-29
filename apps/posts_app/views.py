from django.shortcuts import render, HttpResponse, redirect
from models import *
from django.core import serializers
import json

def index(request):
    return render(request,'posts_app/index.html')

def create_post(request):
    Post.objects.create(content= request.POST['post'])
    posts = Post.objects.all()
    return render(request, 'posts_app/posts.html',{ "posts": posts})
