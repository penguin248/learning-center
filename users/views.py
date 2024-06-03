from django.shortcuts import render

from django.contrib.auth import logout

def user_logout(request):
    logout(request)
    return render(request, 'registration/logged_out.html', {})

