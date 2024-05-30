from django.shortcuts import render

def index(request):
    """The home page for Learning Center"""
    return render(request, 'learning_centers/index.html')
