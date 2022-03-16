from django.db import models
from datetime import timedelta, timezone

def in_three_days():
    return timezone.now() + timedelta(days=3)

class Application(models.Model):
    #Выбор валют
    CHOICES = (
        ('RUB', 'Рубль'),
        ('JPY', 'Йена'),
        ('CNY', 'Юань'),
        ('EUR', 'Евро'),
        ('USD', 'Доллар'),
    )
    TIMEBELT = (
        ('МСК−1', 'калининградское время'),
        ('MSK', 'московское время'),
        ('МСК+1', 'самарское время'),
        ('МСК+2', 'екатеринбургское время'),
        ('МСК+3', 'омское время'),
        ('МСК+4', 'красноярское время'),
        ('МСК+5', 'иркутское время'),
        ('МСК+6', 'якутское время'),
        ('МСК+7', 'владивостокское время'),
        ('МСК+8', 'магаданское время'),
        ('МСК+9', 'камчатское время'),
    )
    currency = models.ChoiceField(max_length=10, choices=CHOICES, verbose_name='Выбор валюты депозита')
    summa_dep = models.IntegerField(verbose_name='Сумма депозита')
    term = models.IntegerField(verbose_name='Срок депозита в днях')
    deadline = models.DateField(default=in_three_days(), verbose_name='Время окончания приема предложений')
    open_account = models.BooleanField(default=False, verbose_name='Требуется открытие расчетного счетета')
    time_belt = models.ChoiceField(choices=TIMEBELT, verbose_name='Часовой пояс возврата депозита')
   # rating_bank = models.ChoiceField(verbose_name='Выбор банка по рейтингу') - min рейтинг
    model_nda = models.BooleanField(default=False, verbose_name='Требуется подписание NDA')

    def __str__(self):
        return self.summa_dep

class Appl_visible_for_banc(models.Model):
    pass
# Create your models here.

