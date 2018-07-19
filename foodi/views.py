from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def dashboard(request):
    return render(request, 'users/dashboard.html')
