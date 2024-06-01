"""Define URL patterns for learning_centers."""

from django.urls import path
from . import views

app_name = 'learning_centers'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    #Page that shows all topics.
    path('topics/', views.topics, name = 'topics'),
    #Detail page for a single topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    #Path for adding a new topic
    path('new_topic/', views.new_topic, name = 'new_topic'),
    #page for adding new entry
    path('new-entry/<int:topi_id>/', views.new_entry, name = 'new_entry'),
    
]