from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.forms_view, name='form'),
]
