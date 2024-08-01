from django.shortcuts import render
from .jokes import JOKES
import random
# Create your views here.

def random_joke_view(request):
    joke = random.choice(JOKES)
    return render(request, 'joke.html', {'joke': joke})