from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone



# Create your views here.
def home(request):
    # 블로그 글들을 모조리 띄우는 코드
    # posts = Blog.objects.all()
    posts = Blog.objects.filter().order_by('-date')
    return render(request, 'home.html', {'posts':posts, 'user':request.user})


def new(request):
    return render(request, 'new.html')

def create(request):
    if(request.method == 'POST'):
        post = Blog()
        post.user = request.user
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        post.save()
    return redirect('home')

def detail(request, blog_id):
    # blog_id 번째 블로그 글을 데이터베이스로부터 갖고와서
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    # blog_id 번째 블로그 글을 detail.html로 띄우주는 코드

    return render(request, 'detail.html', {'blog_detail':blog_detail })

