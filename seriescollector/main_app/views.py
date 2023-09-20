from django.shortcuts import render

series = [
  {'title': 'You', 'seasons': 4, 'genre': 'Thriller', 'rating': 7.7 }, 
  {'title': 'Money Heist', 'seasons': 5, 'genre': 'Thriller', 'rating': 8.2 }, 
  {'title': 'Black Mirror', 'seasons': 6, 'genre': 'Sci-fi', 'rating': 8.7 }, 
  {'title': 'Inventing Anna', 'seasons': 1, 'genre': 'Drama', 'rating': 6.8 }, 
]

# Create your views here.

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def series_index(request):
  return render(request, 'series/index.html', {
    'series': series
  })