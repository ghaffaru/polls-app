from django.contrib import admin
from django.urls import path, include
from .views import *
# from . import views

app_name  = 'polls'

urlpatterns = [
    path('', home, name='index'),
    path('<int:question_id>/', detail, name='detail'),
    path('<int:question_id>/results/', results, name='results'),
    path('<int:question_id>/vote/', vote, name='vote')
]
 
