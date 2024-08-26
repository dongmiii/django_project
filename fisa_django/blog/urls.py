# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # blog 앱 내부의 경로를 지정할 부분
    path('', views.index), # localhost:8000/blog 경로, 경로를 호출하면 실행할 함수의 위치 호출하면 -> view.py 호출
    path('post-list', views.PostList.as_view()), # views.PostList.as_view => Class PostList를 view처럼 쓸거야 
    path('about-me', views.about_me) # path(이동하는 주소, )
]