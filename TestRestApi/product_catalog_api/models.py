from django.db import models


class Product(models.Model):
    SKU_LENGTH = 13

    SKU = models.CharField(
        verbose_name='Штрих код', primary_key=True, max_length=SKU_LENGTH)
    title = models.CharField(verbose_name='Название', max_length=50)
    date_creation = models.DateTimeField(
        verbose_name='Дата создания', auto_now_add=True)
    is_new = models.BooleanField(verbose_name='Новинка', default=True)
    image = models.ImageField(verbose_name='Картинка товара', blank=True)

    def __str__(self):
        return '({}) {}'.format(self.SKU, self.title)


class ProductRegister(models.Model):

    ACTIONS = (
        ('A', 'add'),
        ('R', 'remove')
    )

    date_operation = models.DateTimeField(
        verbose_name='Дата провередения операции', auto_now_add=True)
    user_email = models.EmailField(verbose_name='Email пользователя')
    count = models.IntegerField(verbose_name='Количество товара')
    action = models.CharField(
        max_length=1, choices=ACTIONS, verbose_name='Операция')
    product = models.ForeignKey(
        Product, verbose_name='Продукт', on_delete=models.CASCADE)
