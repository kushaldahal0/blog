from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from blog import views
app_name='blog'
urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", views.index,name='blogindex'),
    path("blogpost/", views.blogpost,name='blogpost'),
    path('blogpost<int:b_no>/', views.singleb, name='singleb'),
    path('comment', views.postcomment, name='comment'),
    path('search/', views.search_posts, name='search_posts'),
    path('category/<str:category_name>/', views.category, name='category_posts'),
]
