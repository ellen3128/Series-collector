from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('series/', views.series_index, name='index'),
    path('series/<int:series_id>', views.series_detail, name='detail'),
    path('series/create/', views.SeriesCreate.as_view(), name='series_create'),
    path('series/<int:pk>/update/', views.SeriesUpdate.as_view(), name='series_update'),
    path('series/<int:pk>/delete/', views.SeriesDelete.as_view(), name='series_delete'),
]
