from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:pk>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:pk>/vote/', views.vote, name='vote'),
    # added the world 'specifics'
    path('specifics/<int:pk>/', views.detail, name='detail'),
]
