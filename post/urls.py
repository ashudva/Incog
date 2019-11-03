from django.urls import path
from . import views

urlpatterns = [
    path('<int:post_id>/', views.post_view, name='post'),
]
