from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import logout

def register(request):
    """Register a new user"""
    if request.method != 'POST':
        # Display blank registration form
        form = UserCreationForm()
    else:
        #Process completed form
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid():
            new_user = form.save()
            #log the user in and then redirect to home page.
            login(request, new_user)
            return redirect('learning_centers:index')
    #Display a blank or invalid form
    context = {'form': form}
    return render(request, 'registration/register.html', context)
    

def user_logout(request):
    """Log out a user"""
    logout(request)
    return render(request, 'registration/logged_out.html', {})

