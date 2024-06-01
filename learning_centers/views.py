from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm

def index(request):
    """The home page for Learning Center"""
    return render(request, 'learning_centers/index.html')

def topics(request):
    """Show all topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_centers/topics.html', context)

def topic(request, topic_id):
    """Show a single topic and all it's entries"""
    topic = Topic.objects.get(id = topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_centers/topic.html', context)

def new_topic(request):
    """Add a new topic"""
    if request.method != 'POST':
        #No data submitted; create a blank form.
        form = TopicForm()
    else:
        #POST Data submitted; process data
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_centers:topics')
    #Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'learning_centers/new_topic.html', context)
            
