from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Speaker

#create views here

def speakers_list(request):
    speakers = [
        {'id': 1, 'name': 'Speaker 1', 'bio': 'Speaker 1 bio', 'location': 'City A'},
        {'id': 2, 'name': 'Speaker 2', 'bio': 'Speaker 2 bio', 'location': 'City B'},
        {'id': 3, 'name': 'Speaker 3', 'bio': 'Speaker 3 bio', 'location': 'City C'},
        {'id': 4, 'name': 'Speaker 4', 'bio': 'Speaker 4 bio', 'location': 'City D'},
        {'id': 5, 'name': 'Speaker 5', 'bio': 'Speaker 5 bio', 'location': 'City E'},
        # Add more dummy speaker information
    ]
    return render(request, 'speakers/speakers_list.html', {'speakers': speakers})
