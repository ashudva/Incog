from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('post/newpost/', views.new_post, name='post'),
    path('post/reply/', views.new_reply, name='reply'),
    path('post/comment/', views.new_comment, name='comment'),
]
