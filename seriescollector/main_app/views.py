from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Series 


# series = [
#   {'title': 'You', 'seasons': 4, 'genre': 'Thriller', 'rating': 7.7 }, 
#   {'title': 'Money Heist', 'seasons': 5, 'genre': 'Thriller', 'rating': 8.2 }, 
#   {'title': 'Black Mirror', 'seasons': 6, 'genre': 'Sci-fi', 'rating': 8.7 }, 
#   {'title': 'Inventing Anna', 'seasons': 1, 'genre': 'Drama', 'rating': 6.8 }, 
# ]

# Create your views here.

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def series_index(request):
  series = Series.objects.all()
  return render(request, 'series/index.html',
  {
    'series': series
  }
)

def series_detail(request, series_id):
  series = Series.objects.get(id=series_id)
  return render(request, 'series/detail.html', { 'series': series })

class SeriesCreate(CreateView):
  model = Series
  fields = '__all__'
  # Special string pattern Django will use
  success_url = '/series/{series_id}' # <--- must specify an exact ID
  # Or..more fitting... you want to just redirect to the index page
  # success_url = '/series'

class SeriesUpdate(UpdateView):
  model = Series
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['seasons', 'genre', 'rating']

class SeriesDelete(DeleteView):
  model = Series
  success_url = '/series'