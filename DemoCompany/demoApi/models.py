from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=64, verbose_name='Наименование')
    PRODUCT_TYPE = (
        (1, 'Тип 1'),
        (2, 'Тип 2'),
        (3, 'Тип 3')
    )
    product_type = models.IntegerField(choices=PRODUCT_TYPE, db_index=True, verbose_name='Тип')
    price = models.FloatField(verbose_name='Цена', db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продуктов'
