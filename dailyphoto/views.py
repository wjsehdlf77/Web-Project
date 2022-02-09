from django.shortcuts import render, HttpResponse, get_object_or_404

from dailyphoto.models import Profile

from django.contrib.auth import get_user_model


# Create your views here.

def dailyphoto_preview(request, username):
    person = get_object_or_404(get_user_model(), username=username)

    return render(request, 'dailyphoto/profile.html', {'person': person})
