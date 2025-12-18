from django.urls import path
from .views import calculator_view, calculate, history_view, clear_history

app_name = 'calculator'

urlpatterns = [
    path('', calculator_view, name='calculator'),
    path('calculate/', calculate, name='calculate'),
    path('history/', history_view, name='history'),
    path('clear/', clear_history, name='clear'),
]
