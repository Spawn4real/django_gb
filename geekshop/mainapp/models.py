from django.db import models


# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='Имя продукта', max_length=64, unique=True)
    discription = models.TextField(verbose_name='Описание', blank=True)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        verbose_name='имя продукта',
        max_length=64,
    )
    image = models.ImageField(
        upload_to='media',
        blank=True,
    )
    short_desc = models.CharField(
        verbose_name='короткое описание',
        max_length=60,
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
    )
    price = models.DecimalField(
        verbose_name='цена продукта',
        max_digits=8,
        decimal_places=2,
        default=0,
    )
    quantity = models.PositiveIntegerField(
        verbose_name='Количество на складе',
        default=0
    )

    def __str__(self):
        return f'{self.name} ({self.category.name})'
