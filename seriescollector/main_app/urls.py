from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('series/', views.series_index, name='index'),
    path('series/<int:series_id>', views.series_detail, name='detail'),
]
