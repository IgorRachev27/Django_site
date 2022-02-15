from django.db import models

# Create your models here.
class TeleSettings(models.Model):
    tg_token = models.CharField(max_length=200, verbose_name='Токен')
    tg_chat = models.CharField(max_length=200, verbose_name='Чат id')
    tg_date = models.DateField(auto_now=True,max_length=200, verbose_name='Дата')
    tg_message = models.TextField(verbose_name='Текст сообщения')
    tg_coming_date = models.DateField(auto_now=True,max_length=200, verbose_name='Дата приезда')

    def __str__(self):
        return self.tg_chat

    class Meta:
        verbose_name = 'Настройку'
        verbose_name_plural = 'Настройки'