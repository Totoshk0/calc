from django.shortcuts import render
from .models import Operation

def calculator_view(request):
    result = None
    error = None

    if request.method == 'POST':
        try:
            a = float(request.POST.get('a'))
            b = float(request.POST.get('b'))
            operation = request.POST.get('operation')

            if operation == 'add':
                result = a + b
                op_symbol = '+'
            elif operation == 'sub':
                result = a - b
                op_symbol = '-'
            elif operation == 'mul':
                result = a * b
                op_symbol = '*'
            elif operation == 'div':
                if b == 0:
                    error = 'Деление на ноль запрещено'
                else:
                    result = a / b
                    op_symbol = '/'

            if result is not None:
                Operation.objects.create(
                    first_number=a,
                    second_number=b,
                    operation=op_symbol,
                    result=result
                )

        except:
            error = 'Введите корректные числа'

    history = Operation.objects.order_by('-created_at')

    return render(request, 'calculator.html', {
        'result': result,
        'error': error,
        'history': history
    })
