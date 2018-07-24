from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import requests
from decouple import config
from django.template import loader
from foodi.models import Food
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    # import code; code.interact(local=dict(globals(), **locals()))
    return render(request, 'home.html')

def dashboard(request):
    return render(request, 'users/dashboard.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def search(request):
    search_result = {}
    if 'query' in request.GET:
        food = request.GET['query']
        url = 'https://trackapi.nutritionix.com/v2/natural/nutrients'
        headers = {'x-app-id': config('NIX_APP_ID'),
                   'x-app-key': config('NIX_APP_KEY'),
                   'x-remote-user-id': '0'}
        payload = {'query': food}

        response = requests.post(url, headers=headers, data=payload)
        search_result = response.json()
        food = FoodService(search_result['foods'][0])
        template = loader.get_template('search.html')
        context = {
            'food': food
        }
    # import code; code.interact(local=dict(globals(), **locals()))
    return render(request, 'search.html', context)
