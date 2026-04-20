from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, './home.html')


def about(request):
    return render(request, './about.html')


def contact(request):
    return render(request, './contact.html')


def post_view(request, id):
    return render(request, './post.html', {'id': id})


def profile_view(request, username):
    return render(request, './profile.html', {'username': username})


def event_view(request, year, month, day):
    return render(request, './event.html', {
        'year': year,
        'month': month,
        'day': day
    })
