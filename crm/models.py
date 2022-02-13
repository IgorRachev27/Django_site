from django.db import models
# Create your models here.


class StatusCrm(models.Model): # должен быть раньше чтобы при наследовании в ForeignKey его было видно
    Status_name = models.CharField(max_length=200, verbose_name='Название статуса')

    def __str__(self):
        return self.Status_name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы '

class Order(models.Model):
    order_dt=models.DateTimeField(auto_now=True, verbose_name='Дата')
    order_name=models.CharField(max_length=200, verbose_name='Имя')
    order_phone=models.CharField(verbose_name='Телефон', max_length=200)
    order_status = models.ForeignKey(StatusCrm, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Статус')
    coming_date = models.DateField(auto_now=True, verbose_name='Дата приезда')
    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'



class ComentCrm(models.Model):
    coment_bimding=models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Заявка")
    coment_text = models.TextField(verbose_name='Текст комментария')
    coment_dt = models.DateTimeField(auto_now=True, verbose_name='Дата создания')

    def __str__(self):
        return self.coment_text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'