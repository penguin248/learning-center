from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

def index(request):
    """The home page for Learning Center"""
    return render(request, 'learning_centers/index.html')

@login_required
def topics(request):
    """Show all topics"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_centers/topics.html', context)

@login_required
def topic(request, topic_id):
    """Show a single topic and all it's entries"""
    topic = Topic.objects.get(id = topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_centers/topic.html', context)

@login_required
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

@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id = topic_id)
    
    if request.method != 'POST':
        #No data submitted; create a blank form
        form = EntryForm()
    else:
        #Post data submitted; process data
        form = EntryForm(data = request.POST)
        if form.is_valid():
            new_entry = form.save(commit = False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_centers:topic', topic_id=topic.id)
    #Display a blank or invalid form
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_centers/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Editing an existing entry"""
    entry = Entry.objects.get(id = entry_id)
    topic = entry.topic
    
    if request.method != 'POST':
        #Initial request; pre-fill form with the current entry
        form = EntryForm(instance=entry)
    else:
        #POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_centers:topic', topic_id=topic.id)
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_centers/edit_entry.html', context)
