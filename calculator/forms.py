from django import forms
import math

class CalculatorForm(forms.Form):
    a = forms.FloatField(label='Первое число')
    b = forms.FloatField(label='Второе число', required=False)

    operation = forms.ChoiceField(choices=[
        ('+', '+'),
        ('-', '-'),
        ('*', '*'),
        ('/', '/'),
        ('^', 'xʸ'),
        ('sqrt', '√x'),
    ])

    def clean(self):
        cleaned = super().clean()
        a = cleaned.get('a')
        b = cleaned.get('b')
        op = cleaned.get('operation')

        if op == '/' and b == 0:
            raise forms.ValidationError('Деление на ноль запрещено')

        if op != 'sqrt' and b is None:
            raise forms.ValidationError('Введите второе число')

        return cleaned
