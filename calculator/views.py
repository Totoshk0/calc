from django.shortcuts import render, redirect
from .forms import CalculatorForm
from datetime import datetime
import math
from .forms import CalculatorForm


def calculator_view(request):
    form = CalculatorForm()
    result = request.session.get('result')

    return render(request, 'calculator.html', {
        'form': form,
        'result': result
    })

def calculate(request):
    if request.method != 'POST':
        return redirect('calculator:calculator')

    form = CalculatorForm(request.POST)

    if not form.is_valid():
        request.session['form_errors'] = form.errors
        return redirect('calculator:calculator')

    a = form.cleaned_data['a']
    b = form.cleaned_data.get('b')
    op = form.cleaned_data['operation']

    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    elif op == '/':
        result = a / b
    elif op == '^':
        result = a ** b
    elif op == 'sqrt':
        result = math.sqrt(a)

    history = request.session.get('history', [])

    history.insert(0, {
        'a': a,
        'b': b,
        'operation': op,
        'result': result,
        'time': datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    })

    request.session['history'] = history[:10]
    request.session['result'] = result

    return redirect('calculator:calculator')

def history_view(request):
    history = request.session.get('history', [])
    return render(request, 'history.html', {
        'history': history
    })

def clear_history(request):
    request.session['history'] = []
    return redirect('calculator:history')
