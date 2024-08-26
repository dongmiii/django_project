from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

class PostList(ListView):   # post_list.html, post-list
    model = Post 
    # template_name = 'blog/index.html' 
    ordering = '-pk'
    context_object_name = 'post_list'


def index(request): # 함수를 만들고, 그 함수를 도메인 주소 뒤에 달아서 호출하는 구조
    posts = Post.objects.all()
    return render(
        request,
        'blog/index.html', # 없는 index.html을 호출하고 있음
        {
            'posts' : posts, 'my_list' : ["apple", "banana", "cherry"], 'my_text' : "첫번째 줄 \n 두번째 줄"
        }
    )

# ordering = '-pk' : 역순으로 정렬

def about_me(request): 
    return render(
        request,
        'blog/about_me.html'
    )
