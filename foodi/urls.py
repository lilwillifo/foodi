from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('search/', views.search, name='search'),
    path('diary/', views.diary, name='diary'),
    path('api/chart/data/', views.ChartData.as_view(), name='api-chart-data')
]
