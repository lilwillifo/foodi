from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import requests
from decouple import config
from django.template import loader
from foodi.food import FoodService

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

        response = requests.post(url, headers=headers, data=payload)
        search_result = response.json()
        food = FoodService(search_result['foods'][0])

        # import code; code.interact(local=dict(globals(), **locals()))
    template = loader.get_template('search.html')
    context = {
        'food': food
    }
    return HttpResponse(template.render(context))
