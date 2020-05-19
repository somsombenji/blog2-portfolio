from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

def home(request):
    blog_ob = Blog.objects
    return render(request, 'home.html', {'blog_content':blog_ob})

def detail(request, post_id):
    blog_detail = get_object_or_404(Blog, pk = post_id)
    return render(request, 'detail.html', {'detail':blog_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id)) #str은 int를 문자열로 형변환
