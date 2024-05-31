from django.shortcuts import render
from .models import Topic

def index(request):
    """The home page for Learning Center"""
    return render(request, 'learning_centers/index.html')

def topics(request):
    """Show all topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_centers/topics.html', context)
