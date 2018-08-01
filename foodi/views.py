import requests
from django.shortcuts import render, redirect
from django.contrib import auth
from decouple import config
from foodi.models import Food, Diary, Profile
from foodi.food_service import FoodService
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import DiaryForm
from django.contrib import messages
from IPython import embed
from django.db.models import Sum, Count
from collections import Counter
from django.contrib.auth.decorators import login_required


def home(request):
    # import code; code.interact(local=dict(globals(), **locals()))
    return render(request, 'home.html')

@login_required
def analytics(request):
    return render(request, 'analytics.html')

@login_required
def dashboard(request):
    user = auth.get_user(request)
    average_calories = 0
    average_protein = 0
    if user.profile.foods.count() > 0:
        total_calories = user.profile.foods.aggregate(Sum('calories'))['calories__sum']
        total_days = user.profile.diaries.values('date_eaten').distinct().count()
        average_calories = total_calories / total_days
        average_protein = user.profile.foods.aggregate(Sum('protein'))['protein__sum'] / total_days
    context = {'avg_cal': int(average_calories), 'avg_protein': int(average_protein) }
    return render(request, 'users/dashboard.html', context)

@login_required
def diary(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DiaryForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            servings = form.cleaned_data['servings']
            date = form.cleaned_data['date']
            food = Food.objects.get(name=form.cleaned_data['food'])
            # import code; code.interact(local=dict(globals(), **locals()))
            Diary.objects.create(food=food, user=auth.get_user(request).profile, servings=servings, date_eaten=date)

            # redirect to a new URL:
            return redirect('/diary/')

    # if a GET (or any other method) we'll create a blank form
    else:
        user = auth.get_user(request)
        foods = user.profile.top_5_foods()
        context = {"top_foods": foods}
        return render(request, 'users/diary.html', context)

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
    food = request.GET['query']
    try:
        food = Food.objects.get(name = food.capitalize())
    except Food.DoesNotExist:
        url = 'https://trackapi.nutritionix.com/v2/natural/nutrients'
        headers = {'x-app-id': config('NIX_APP_ID'),
                   'x-app-key': config('NIX_APP_KEY'),
                   'x-remote-user-id': '0'}
        payload = {'query': food}

        response = requests.post(url, headers=headers, data=payload)
        search_result = response.json()
        if 'foods' not in search_result:
            context = messages.error(request, 'No foods found.')
            return render(request, 'home.html', context)
        else:
            raw_food = FoodService(search_result['foods'][0])
            food  = Food(name = raw_food.name,
                           img = raw_food.img['thumb'],
                           serving_qty = raw_food.serving_qty,
                           serving_unit = raw_food.serving_unit,
                           calories = raw_food.calories,
                           total_fat = raw_food.total_fat,
                           sat_fat = raw_food.sat_fat,
                           cholesterol = raw_food.cholesterol,
                           sodium = raw_food.sodium,
                           carbs = raw_food.carbs,
                           fiber = raw_food.fiber,
                           sugar = raw_food.sugar,
                           protein = raw_food.protein)
            food.save()
        # end try

    context = {
        'food': food,
        'form': DiaryForm(initial={'food': food}),
    }
    # import code; code.interact(local=dict(globals(), **locals()))
    return render(request, 'search.html', context)


from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User

class DiaryData(APIView):
    def get(self, request, format=None):
        user = auth.get_user(request)
        date = request.GET['date']
        data = {}
        total_day_calories = 0
        for x in user.profile.diaries.filter(date_eaten=date):
            data[x.food.name] = x.servings

        return Response(data)

class ChartData(APIView):
# can change these two variables down the road to enhance security, but for now just leave them blank
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        calories = dict()
        food_count = dict()
        user = auth.get_user(request)
        total_fat = 0
        total_carbs = 0
        total_protein = 0
        total_calories = 0
        top_5 = []
        if user.profile.foods.count() > 0:
            total_fat = user.profile.foods.aggregate(Sum('total_fat'))['total_fat__sum']
            total_carbs = user.profile.foods.aggregate(Sum('carbs'))['carbs__sum']
            total_protein = user.profile.foods.aggregate(Sum('protein'))['protein__sum']
            total_calories = user.profile.foods.aggregate(Sum('calories'))['calories__sum']
            top_5 = user.profile.top_5_foods()
            for food in user.profile.foods.all():
                calories[food.name] = food.calories

        calories = sorted(calories.items(), key=lambda x: x[1])
        calories = dict(calories)

        data = {
            "calorie_labels": calories.keys(),
            "calorie_data": calories.values(),
            "average_calories": total_calories,
            "fat": total_fat,
            "carbs": total_carbs,
            "protein": total_protein,
            "top_5_foods": top_5
        }

        return Response(data)
