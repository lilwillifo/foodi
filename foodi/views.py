from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import requests
from decouple import config

def home(request):
    return render(request, 'home.html')

def dashboard(request):
    return render(request, 'users/dashboard.html')

def search(request):
    search_result = {}
    if 'query' in request.GET:
        food = request.GET['query']
        url = 'https://trackapi.nutritionix.com/v2/natural/nutrients'
        headers = {'x-app-id': config('NIX_APP_ID'),
                   'x-app-key': config('NIX_APP_KEY'),
                   'x-remote-user-id': '0'}
        payload = {'query': food}
        # import code; code.interact(local=dict(globals(), **locals()))

        response = requests.post(url, headers=headers, data=payload)
        search_result = response.json()


    return render(request, 'search.html', {'search_result': search_result})
