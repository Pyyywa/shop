import django.utils.timezone
from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Product(models.Model):
    product_name = models.CharField(max_length=50, verbose_name = 'наименование')
    desc = models.TextField(verbose_name = 'описание', **NULLABLE)
    image = models.ImageField(upload_to='products/', verbose_name = 'превью', **NULLABLE)
    category = models.CharField(max_length=50, verbose_name = 'категория')
    quantity_per_unit = models.PositiveIntegerField(verbose_name = 'цена за шт.', default='0')
    сreation_date = models.DateField(verbose_name = 'дата создания')
    last_change_date = models.DateTimeField(verbose_name = 'дата последнего изменения', **NULLABLE)


    def __str__(self):
        return f'{self.category} {self.product_name} '

    class Meta():
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name = 'наименование')
    description = models.TextField(verbose_name = 'описание', **NULLABLE)

    def __str__(self):
        return f'{self.id}. {self.category_name}'

    class Meta():
        verbose_name = 'категория'
        verbose_name_plural = 'категории'