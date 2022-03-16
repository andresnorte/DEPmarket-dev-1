from django import forms
from django.db import transaction

from applications.models import


class CompanyApplicationForm():
    currency = forms.ChoiceField(label='Выбор валюты депозита')
    summa_dep = forms.IntegerField(label='Сумма депозита')
    term = forms.IntegerField(label='Срок депозита в днях')
    deadline = forms.DateField(label='Время окончания приема предложений')
    open_account = forms.BooleanField(label='Требуется открытие расчетного счетета')
    time_belt = forms.ChoiceField(label='Часовой пояс возврата депозита')
    rating_bank = forms.CharField(label='Выбор банка по рейтингу')
    model_nda = forms.BooleanField(label='Требуется подписание NDA')