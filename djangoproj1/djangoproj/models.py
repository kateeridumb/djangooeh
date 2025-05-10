from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Tag(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название тега')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название товара')
    description = models.TextField(verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')
    image = models.ImageField(upload_to='products/', null=True, blank=True, verbose_name='Картинка')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    is_deleted = models.BooleanField(default=False, verbose_name='Логическое удаление')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    tags = models.ManyToManyField(Tag, verbose_name='Теги')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        permissions = [
            ("can_logically_delete", "Can logically delete product"),
            ("can_undelete", "Can restore deleted product"),
            ("delete_product_physical", "Can physically delete product"),
        ]

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='orders',verbose_name='Пользователь',null=True, blank=True)
    unique_number = models.CharField(max_length=50, unique=True, verbose_name='Уникальный номер')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    delivery_address = models.TextField(verbose_name='Адрес доставки')
    client_phone = models.CharField(max_length=20, verbose_name='Телефон клиента')
    client_name = models.CharField(max_length=255, verbose_name='ФИО клиента')
    products = models.ManyToManyField(Product, through='OrderItem', verbose_name='Товары')
    
    def __str__(self):
        return f"Заказ #{self.unique_number}"
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
    
    @property
    def total_price(self):
        return sum(
            item.product.price * item.quantity - item.discount_per_item * item.quantity
            for item in self.orderitem_set.all()
        )

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')
    discount_per_item = models.FloatField(default=0, verbose_name='Скидка за единицу')
    
    def __str__(self):
        return f"{self.product.name} в заказе #{self.order.unique_number}"
    
    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказа'