from django.db import models
from django.contrib import admin


class Advert(models.Model):
    title = models.CharField('Название', max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    create_at = models.DateTimeField(auto_now_add=True)
    auction = models.BooleanField('Торг', help_text='Отметьте, уместен ли торг')

    def __str__(self):
        return f'Advertisement(id={self.id}, title={self.title}, price={self.price})'

    @admin.display(description='Дата создания')
    def created_time(self):
        from django.utils import timezone
        from django.utils.html import format_html
        if self.create_at.date() == timezone.now().date():
            created_time = self.create_at.time().strftime('%H:%M:%S')
            return format_html(
                "<span style='color: green; font-weight: bold;'>Сегодня в {}</span>", created_time
            )
        return self.create_at.strftime('%d.%m.%y')

    class Meta:
        db_table = 'advert'